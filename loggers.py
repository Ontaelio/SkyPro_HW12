import logging

logging.basicConfig(level=logging.INFO)

page_logger = logging.getLogger('pages')
file_logger = logging.getLogger('files')

page_handler = logging.FileHandler('page_log.txt')
file_handler = logging.FileHandler('file_log.txt')

formatter = logging.Formatter("%(asctime)s : %(message)s")
page_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

page_logger.addHandler(page_handler)
file_logger.addHandler(file_handler)