from base_classes.crawler import crawler
from base_classes.data_base import data_base
from base_classes.notifier import notifier
from crawlers.faults import faults as fault_crawler
from notifiers.whatsapp import whatsapp
from data_bases.firebase import firebase
from domains.fault import fault
from typing import List

def main(self) -> None:
    url: str = ''
    usr: str = ''
    psw: str = ''
    msg_origin: str = ''
    msg_txt: str = ''
    msg_destination: str = ''

    crawler_aux: crawler = fault_crawler(url, usr, psw)
    notifier_aux: notifier = whatsapp()
    data_base_aux: data_base = firebase()

    ## Processing
    lst_faults: List[fault] = crawler_aux.start()

    for f in lst_faults:
        if f.is_notify_required():
            msg_txt = f.parse_message()
            notifier_aux.notify(msg_origin, msg_destination, msg_txt)
        pass

        # Even though an item has not to be notified to some one, it's important to be persisted to database
        data_base_aux.save(f)
    pass