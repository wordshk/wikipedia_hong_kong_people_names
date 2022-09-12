#!/usr/bin/env python3

# The wikimedia sql files are mysql format, which isn't the big problem. It's
# that they are just slightly longer than the default SQLITE_MAX_SQL_LENGTH
# limit (10^6), which forces us to chop them apart before we do anything more
# with it. Without really parsing the data, we'll use some heuristics to try to
# break it apart, and hopefully it will work. Otherwise sqlite should give a
# syntax error...

import sys
import re

# 300k, substantially smaller than the default 1MB SQLITE_MAX_SQL_LENGTH for
# some margin. The speedup with less cuts isn't that great anyway.

max_length = 300 * 1000
orig_sql_file = sys.argv[1]
table_name = sys.argv[2]
out_file_path = orig_sql_file + ".fixed"

def fix_slashes(s):
    temp = b'!~@!$'
    return s.replace(b'\\\\', temp).replace(b'\\\'', b"''").replace(temp, b'\\')

creating_table = False
column_names = []
# probably UTF-8? I am getting some UTF-8 errors if using text mode though!
# binary mode is good for ensuring lengths are in bytes also
with open(out_file_path, "wb") as out_file:
    with open(orig_sql_file, 'rb') as in_file:
        line_num = 0
        while line := in_file.readline():
            line_num += 1

            if line.startswith(b"CREATE TABLE "):
                creating_table = True
                continue

            if creating_table:
                if line.startswith(b')'):
                    creating_table = False
                    out_file.write(b'CREATE TABLE ')
                    out_file.write(table_name.encode("utf-8"))
                    out_file.write(b' (')
                    out_file.write(",".join(column_names).encode("utf-8"))
                    out_file.write(b' );\n')
                else:
                    sline = line.decode("utf-8")
                    if m := re.match('\s+`([^`]+)`\s+', sline):
                        # print(m.group(1))
                        column_names.append(m.group(1))


            # We need to manually create the tables
            if not line.startswith(b"INSERT INTO "): continue

            N = len(line)
            # print(line_num, N)
            sys.stdout.write('.')
            sys.stdout.flush()

            start_idx = 0

            while N - start_idx > max_length:
                new_idx = line.rfind(b'),(', 0, start_idx + max_length) + 2
                out_file.write(fix_slashes(line[start_idx:new_idx-1])) # -1 for omitting comma ',', mysql escape to sqlite double quote escape
                out_file.write(b';\n') # should be just \n, no \r i think?
                out_file.write(f'INSERT INTO `{table_name}` VALUES '.encode("utf-8"))
                start_idx = new_idx
                # print(line_num, start_idx)


            out_file.write(fix_slashes(line[start_idx:]))

sys.stdout.write('\n')
