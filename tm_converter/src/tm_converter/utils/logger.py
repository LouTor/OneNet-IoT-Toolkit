# 暂未启用
import logging
from pathlib import Path


def setup_logger(name=__name__, log_file="app.log", level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # 避免重复添加handler
    if not logger.handlers: 
        # 文件日志
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(file_formatter)

        # 控制台日志
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter('%(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
