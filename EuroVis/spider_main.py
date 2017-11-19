#coding:utf-8
from EuroVis import html_downloader, html_parser, html_outputer
class SpiderMain(object):

    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutput()
    def craw(self,root_url):
        try:
            html_cont = self.downloader.download(root_url)
            self.new_data = self.parser.parse(root_url, html_cont)
            #self.outputer.collect_data(new_data)
        except:
            print('craw failed')

if __name__=="__main__":
    year = 2013
    while year<=2017:
        root_url="http://www.cad.zju.edu.cn/home/vagblog/vispapers/eurovis"+ str(year) +".html"
        obj_spider = SpiderMain()
        obj_spider.craw(root_url)
        year = year+1