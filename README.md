Downloads SQL files from Chinese wikipedia dumps, converts them into
sqlite-compatible format, and queries the database for Hong Kong people names.

To start, see `extract`. It will generate a `extracted.txt` file.

To fix other issues with extracted.txt, including simplified characters,
non-name components of the page title, see `post_processing`.

`hong_kong_people_names.txt` is the post_processed result.
