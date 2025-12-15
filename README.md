Downloads SQL files from Chinese wikipedia dumps, converts them into
sqlite-compatible format, and queries the database for Hong Kong people names.

To start, run `./extract`. It will generate a `extracted.txt` file.

To fix other issues with extracted.txt, including simplified characters,
non-name components of the page title, run `./post_processing`.
