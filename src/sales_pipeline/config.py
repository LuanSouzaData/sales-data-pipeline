from pathlib import Path

# Diretório raiz do projeto
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Diretórios principais
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

DATABASE_DIR = BASE_DIR / "database"
LOGS_DIR = BASE_DIR / "logs"
DOCS_DIR = BASE_DIR / "docs"
DATABASE_PATH = DATABASE_DIR / "sales.db"
SCHEMA_PATH = DATABASE_DIR / "schema.sql"

# Garante que os diretórios existam
for directory in (
    DATA_DIR,
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    DATABASE_DIR,
    LOGS_DIR,
    DOCS_DIR,
):
    directory.mkdir(parents=True, exist_ok=True)

# Banco de dados
DATABASE_FILE = DATABASE_DIR / "sales.db"

# Arquivo de log
LOG_FILE = LOGS_DIR / "pipeline.log"