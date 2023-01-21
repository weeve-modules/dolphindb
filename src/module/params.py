from os import getenv

PARAMS = {
    "HOST": getenv("HOST", ""),
    "PORT": int(getenv("PORT", "")),
    "USERNAME": getenv("USERNAME", ""),
    "PASSWORD": getenv("PASSWORD", ""),
    "DB_PATH": getenv("DB_PATH", ""),
    "TABLE_NAME": getenv("TABLE_NAME", ""),
    "COLUMNS": [column.strip() for column in getenv("COLUMNS").split(',')],
    "LABELS": [label.strip() for label in getenv("LABELS").split(',')],
    "DATE_COLUMN": getenv("DATE_COLUMN", "").strip()
}
