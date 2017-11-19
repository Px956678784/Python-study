#coding: utf-8
import re
from bs4 import BeautifulSoup


def _get_new_data(page_url, soup):
     keywords = soup.find_all('td', class_ = 'topic')
     for keyword in keywords:
         table = keyword.parent.find_next_sibling()
         papers = table.find_all('p')
         for paper in papers:
             print(keyword.get_text())
             title_node = paper.find('span', class_ = 'projecttitle' )
             print("title:"+ title_node.get_text())
             url_node = paper.find('img', src = re.compile(r"paper")).find_parent()
             if(url_node is not None):
                 print('url:'+url_node['href'])
             links = paper.find_all('a')
             for link in links:
                 if link is not None:
                     print("author:"+link.get_text())

class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_data = _get_new_data(page_url, soup)
        return new_data