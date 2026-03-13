import logging

def get_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler("logs/test.log")
    logger.addHandler(handler)

    return logger




# import logging
# import os
#
# def get_logger(name):
#
#     log_dir = "logs"
#     os.makedirs(log_dir, exist_ok=True)
#
#     logger = logging.getLogger(name)
#     logger.setLevel(logging.INFO)
#
#     file_handler = logging.FileHandler(f"{log_dir}/test.log")
#     formatter = logging.Formatter(
#         "%(asctime)s - %(levelname)s - %(message)s"
#     )
#
#     file_handler.setFormatter(formatter)
#     logger.addHandler(file_handler)
#
#     return logger