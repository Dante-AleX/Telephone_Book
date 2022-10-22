import logging

logging.basicConfig(
    level=logging.INFO,
    filename='phonebook.log',
    format='[%(asctime)s] [%(levelname)s] [%(module)s] => %(message)s',
    datefmt='%d.%m.%Y %H:%M:%S ',
)
