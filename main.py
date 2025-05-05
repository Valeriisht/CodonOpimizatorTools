from src.optimizer import CodonOptimizator
from src.config import OptimizationConfig

import argparse
from loguru import logger
import sys
from pathlib import Path


# Вызов данной функции приведёт к изменению свойств root logger
logs_format = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
logger.add(  # Добавляем Handler для записи в stdout
    sys.stdout, level="DEBUG", format=logs_format, colorize=True, 
    filter=lambda record: record["extra"].get("source") == "main" # отключение распространения
)

logger.add(
    "errors_logs.log",
    level="ERROR",
    format=logs_format,
    colorize=False,
    rotation="500 KB",  # ограничиваем по памяти
)


def main():
        #  example
        try:

            logger.info("Starting main function")

            optimizer = CodonOptimizator(OptimizationConfig) 
            logger.info("Inizialization of CodonOptimizator") # инизиализация конфига 

            protein = "GIVEQCCTSICSLYQLENYCN" # инсулин

            opt_seq = optimizer.optimize(protein)

            logger.info("Success of CodonOptimizator working")# оптимизация 
            logger.info("Ending main function")

            print(f"Optimization Sequence : {opt_seq.sequence}, type: {opt_seq.type}")
        
        except Exception as e:
             logger.critical(f"Failed with {e}")
             sys.exit(1)  # 1 - общепринятый код ошибки


if __name__ == "__main__":
    main()
