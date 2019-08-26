import threading
from queue import Queue
from spider import *
from general import *
from domain import *

if __name__ == '__main__':
    PROJECT_NAME = 'chinhem'
    HOME_PAGE = 'https://chinhem.com'
    DOMAIN_NAME = get_domain_name(HOME_PAGE)
    QUEUE_FILE = PROJECT_NAME + '/queue.txt'
    CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
    NUMBER_OF_THREADS = 8
    queue = Queue()
    Spider(PROJECT_NAME, HOME_PAGE, DOMAIN_NAME)
