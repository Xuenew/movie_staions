#Author:xue yi yang
import requests
from lxml import etree
import html
class serch_html():
    def __init__(self,name=""):

        self.url = "https://v.qq.com/x/search/?q="+name
        self.head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
    }

    def get_html(self):
        res = requests.get(url=self.url, headers=self.head).text
        selector = etree.HTML(res)
        url = selector.xpath("//a[@_stat='video:poster_v']/@href")[0]
        url_img = selector.xpath("//a[@_stat='video:poster_v']/img/@src")[0]
        url_h2 = selector.xpath("//a[@_stat='video:poster_v']/../h2")[0]
        url_div = selector.xpath("//a[@_stat='video:poster_v']/../div")[0]
        url_h2 = etree.tostring(url_h2).decode()
        url_div = etree.tostring(url_div).decode()
        # print("******", url, url_img, html.unescape(url_h2), html.unescape(url_div))
        data = {"url":url,"url_img":url_img,"url_h2":html.unescape(url_h2),"url_div":html.unescape(url_div)}
        return data