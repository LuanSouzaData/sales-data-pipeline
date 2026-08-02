import logging

from sales_pipeline.config import LOG_FILE


def setup_logger() -> logging.Logger:
    """
    Configura e retorna o logger da aplicação.
    """

    logger = logging.getLogger("sales_pipeline")

    # Evita adicionar handlers duplicados
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.info("Logger initialized successfully.")

    return logger