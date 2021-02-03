'''
scrape.py
A program designed to scrape yahoo finance pages to look for price drops.
Written by Nick Pandelakis
'''

import requests
from bs4 import BeautifulSoup
from pages import pages
from proxy_config import proxies


def get_page_list(list: pages):
    page_list = []
    for page in pages:
        page_list.append(requests.get(page))

    return page_list

def get_page_soup_list():
    page_list = get_page_list(pages)
    page_soup_list = []
    for page in page_list:
        print(page)
        page_soup_list.append(BeautifulSoup(page.content, 'html.parser'))
    
    return page_soup_list

def get_price_drop_list():
    page_soup_list = get_page_soup_list()
    price_drop_list = []
    for page_soup in page_soup_list:
        try:
            #both classes are currently only used once on the page.
            name = page_soup.find(class_="D(ib) Fz(18px)").get_text()
            price_drop = page_soup.find(class_="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)").get_text()
            price_drop_list.append([name, price_drop])
        except:
            pass

    return price_drop_list

def main():
    price_drop_list = get_price_drop_list()
    print(price_drop_list)



if __name__ == '__main__':
    main()
