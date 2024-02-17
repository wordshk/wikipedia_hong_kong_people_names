Downloads SQL files from Chinese wikipedia dumps, converts them into
sqlite-compatible format, and queries the database for popular fictional
characters.

This is based off of earlier work in the main branch that queries for Hong Kong
people's names.

To start, see `extract`. It will generate a `zhwiki.fictional-characters.txt` file.

You can modify the query in query.sql to query for something you want. The categorylinks self-join is just to specify two conditions for matching, if you only want to match one category, just remove the join like this:

```
SELECT count(page_title) as cc, page_title from page as pg JOIN pagelinks AS pl ON pl.pl_title = pg.page_title where pg.page_id IN (
    SELECT c1.cl_from
        from categorylinks as c1
        WHERE c1.cl_to LIKE '%唐朝%'
) group by pg.page_title order by cc desc;
```
