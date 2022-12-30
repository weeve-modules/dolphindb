from os import getenv

PARAMS = {
    "HOST": getenv("HOST", ""),
    "PORT": int(getenv("PORT", "")),
    "USERNAME": getenv("USERNAME", ""),
    "PASSWORD": getenv("PASSWORD", ""),
    "DB_PATH": getenv("DB_PATH", ""),
    "TABLE_NAME": getenv("TABLE_NAME", ""),
    "COLUMNS": getenv("COLUMNS", ""),
    "LABELS": getenv("LABELS", ""),
    "DATE_COLUMN": getenv("DATE_COLUMN", "")
}

PARAMS['DATE_COLUMN'] = PARAMS['DATE_COLUMN'].strip()

# parse columns and labels
if PARAMS['COLUMNS']:
    PARAMS['COLUMNS'] = [header.strip() for header in PARAMS['COLUMNS'].split(',')]
else:
    PARAMS['COLUMNS'] = None

if PARAMS['LABELS']:
    PARAMS['LABELS'] = [label.strip() for label in PARAMS['LABELS'].split(',')]
else:
    PARAMS['LABELS'] = None
