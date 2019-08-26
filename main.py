import threading
from queue import Queue
from spider import *
from general import *
from domain import *


def create_job():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    while True:
        url = queue.get()
        try:
            Spider.crawl_page(threading.current_thread().name, url)
            queue.task_done()
        except UnicodeEncodeError:
            print('Unicode Errors')
            pass


def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_job()


if __name__ == '__main__':
    PROJECT_NAME = 'howkteam'
    HOME_PAGE = 'https://www.howkteam.vn'
    DOMAIN_NAME = get_domain_name(HOME_PAGE)
    QUEUE_FILE = PROJECT_NAME + '/queue.txt'
    CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
    NUMBER_OF_THREADS = 8
    queue = Queue()
    Spider(PROJECT_NAME, HOME_PAGE, DOMAIN_NAME)
    create_workers()
    crawl()
