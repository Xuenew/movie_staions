#Author:xue yi yang
import requests
import re
from lxml import etree
import html
import json
class serch_movies_new_big():
    def __init__(self,ckey="",vid=""):

        self.ck = ckey
        self.vid = vid
        self.head  ={
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
    # "referer": "https://v.qq.com/x/cover/6sj522tgplnw8no.html",
    "referer": "",
    "origin":"https://v.qq.com",
    "Host":"vd.l.qq.com",
    "Content-Type": "text/plain",
    "Content-Length": "998",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Connection": "keep-alive",
    # "cookie":"pgv_pvi=6886795264; RK=gXTYpKgRwG; ptcz=840f92f9f159c3df7426ee93de8db40f2aac5846024c670da50da72b38a86f57; tvfe_boss_uuid=262d9f7357466816; pgv_pvid=8810885929; appuser=2C6DD715C20A4FB4; o_minduid=Noo0SV5hPDmrM_BmezZCjIcb4bNOwtc4; pt2gguin=o1287986063; eas_sid=c1g5k3c8d5z7F5C4i3B53815G4; _ga=GA1.2.1401926032.1538576269; o_cookie=1287986063; pac_uid=1_1287986063; pgv_info=ssid=s8691309488; psessionid=753b52bb_1550913690_1287986063_12868; cm_cookie=V1,110061&f1288a4ca44809f&AQEBReuUsErVKO8APUl7x9H9JoazHP3ft5Ph&180512&180512,10008&86DB7F117302411B942DE9A135EFFC3C-&AQEB3hf315d9Rk3WQmRWuNyG_YZXovagHuzH&180713&180731,10027&1531474496603987&AQEB2ESdf26LlMkv98aJjckezs8GkNRPG7Z7&180804&180804,110055&s0187af75df41bf1e2d&AQEBU7cLHFaTfVzcidOZUVYR0gzgFzFMxGyg&180805&181107,110120&5766185851548174655&AQEBECEEbOnrSf1NHv6oSmOUJwqPHG0-KQ2N&181108&181108,10016&G1LIOs21cjIy&AQEBpTlkJymSFeYmP6Y6TXNrKSbRVBImQJEY&180805&181111,110080&EC38C46F0E2D575B42BED2&AQEBECEEbOnrSf1GI3MmVjN-WLK_w9arUl_U&190120&190223,110066&64zAf0jc0750&AQEBECEEbOnrSf27J43ybvHWRCigUfy8hBaX&180820&190223,110065&6sNjZU62Wq&AQEBECEEbOnrSf3IL-0efraLbw9tW67oyrkk&180820&190223; adid=1287986063; LHTturn=582; image_md5=3c32a8e53f5bdbc2652e06e3aaa9cb3e; ufc=r47_1_1551002765_1550916545; LZTturn=49; lv_play_indexl.=72; psessiontime=1550916479; Lturn=217; LPLFturn=10; LKBturn=749; LPVLturn=84; LVMturn=508; LPSJturn=156; LBSturn=273; LZIturn=665; LZCturn=258; LCZCturn=914; LVINturn=660",
    # "cookie":"_ga=GA1.2.14667918.1524406512; __gads=ID=b26888be49e4c6af:T=1524580403:S=ALNI_MbLwqEU4XzIsYFo1MQKkcJIvPN7RQ; CNZZDATA5381190=cnzz_eid%3D1257551626-1536491116-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1536491116; CNZZDATA1000071539=1428688293-1537862959-http%253A%252F%252Fwww.so.com%252F%7C1537874288; CNZZDATA5897703=cnzz_eid%3D1230882625-1538949237-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1538949237; UM_distinctid=166af1da0e3342-057658bb02ce61-43480620-100200-166af1da0e5913; CNZZDATA1257640778=736722757-1540535658-https%253A%252F%252Fwww.baidu.com%252F%7C1540535658; CNZZDATA1262954991=2062276517-1540807324-https%253A%252F%252Fwww.baidu.com%252F%7C1540807324; CNZZDATA1255738818=1516147091-1541040528-https%253A%252F%252Fwww.baidu.com%252F%7C1541038258; CNZZDATA1258351730=681502932-1541513254-https%253A%252F%252Fwww.baidu.com%252F%7C1541513254; sc_is_visitor_unique=rx10072214.1543370402.62B6230E88DE4F6F44AAD6EBCB5DF484.1.1.1.1.1.1.1.1.1; CNZZDATA1261691463=873270962-1543298841-https%253A%252F%252Fwww.baidu.com%252F%7C1545130319; gr_user_id=59e52343-6192-43aa-951e-b34e52338dfd; Hm_lvt_d8d668bc92ee885787caab7ba4aa77ec=1547596877; .CNBlogsCookie=32CC485709EB76E4EA77FC16CD6A333DC098FA970677893B8A3D2F7C4B75065AAAFC399AE8A786003354A105A65DFEC62B03A556A86E67584AF6E3DB953479FE28121012909E5F496A6F475AFFB61F898037424A; .Cnblogs.AspNetCore.Cookies=CfDJ8KlpyPucjmhMuZTmH8oiYTMC0xm3gjISmk0CqY6NNk9VRh6Z15GgP9dqMY1zy4X-NDcV8RRqXIjVgX2_bTBqSA3qMFCwpPhV-sRWqu9xxWtFXuOsBNwRPe4KHhGGMPO9JFKdlVAxGVIrIwLYSNVV22edA4szkHYzY6VMQlYq5vy99FYk6dKhJHIvLpqh-LtaduEAxjcRHksVd5j0Edctx-NQmLlUt2RVVmyeq0TyWKsXYKBmBE33VwcDw_Az2rZGHXAjvdLfHWsSdDZCJYpcbMXvwwzsTzJ4WXVrBcguhyoo5V0oqj87lEZnOdXvojYNjQ; _gid=GA1.2.732182647.1550912329"
}

        self.data = {
            "adparam": ""
            ,"buid": "vinfoad"
         ,   "vinfoparam": "charge=1&defaultfmt=auto&otype=ojson&guid=c3ed01ec03a21050db27858ad6cd8f20&platform=10201&sdtfrom=v1010&defnpayver=1&appVer=3.5.57&host=v.qq.com&ehost=https://v.qq.com/x/cover/6sj522tgplnw8no.html&refer=v.qq.com&sphttps=1&tm=1550987972&spwm=4&logintoken=%7B%22main_login%22%3A%22wx%22%2C%22openid%22%3A%22ox8XOvie1TjyS7CvgWw4vKcr0jDM%22%2C%22appid%22%3A%22wx5ed58254bc0d6b7f%22%2C%22access_token%22%3A%2218_k1LQbnBi5if5-OPDCTi7AP2B2xNyNxZK0MhU1l692sE38PGkJohJdegmque2YTBgvO6n8bKADEt6TArP_GhadA%22%2C%22vuserid%22%3A%221363393582%22%2C%22vusession%22%3A%22d9cd3df1d13f9a48cb624e03eda0%22%7D&unid=7d523775a45e11e89d19a0429186d00a&vid={}&defn=&fhdswitch=0&show1080p=1&isHLS=1&dtype=3&sphls=2&spgzip=1&dlver=2&drm=32&hdcp=0&spau=1&spaudio=15&defsrc=1&encryptVer=8.1&cKey={}&fp2p=1&spadseg=1".format(self.vid,self.ck)

        }
        # self.proxies = {'http': '114.249.116.88:9000',}  ,proxies = self.proxies
    def get_paly_url(self):
        res = requests.get(url="https://vd.l.qq.com/proxyhttp",headers=self.head, data=self.data).text
        # print(json.loads(res)["vinfo"])
        null = ""
        # print(res)
        # print(type(json.loads(res)))
        x=json.loads(json.loads(res)["vinfo"])
        # print(x)
        # print(type(x))
        # print(x["vl"]["vi"][0]["ul"]["ui"][0]["url"])
        # print(x["vl"]["vi"][0]["ul"]["ui"][0]["hls"]["pt"])
        # print(json.loads(res)["vinfo"]["vl"]["vi"][0]["ul"]["ui"][0]["url"])
        # print(json.loads(res)["vinfo"]["vl"]["vi"][0]["ul"]["ui"][0]["hls"]["pt"])
        play_url = x["vl"]["vi"][0]["ul"]["ui"][0]["url"] + x["vl"]["vi"][0]["ul"]["ui"][0]["hls"]["pt"]
        # print(play_url)
        return play_url
        # return x
if __name__ == '__main__':
    s = serch_movies_new_big(ckey="5978479087DA7CB437AEF8020262BB7C73B9775E68150310CFBAD09C15C0FCE7C69E988D2FDC98571CBED165D8D2E2F81C5A9ADF194EE1CD12DA5CC57887B6C5CC2C003A01BAB0F8E58BD25393326BCD5AFF39B90F75A14D77909771D954AC8D42580E3FC0D0904800BE2B4BB134E2E05EE9F1C1CA832C1CA6783867E88E3F823D20AF1C6797CA054FD06DAD22B589F740862FBF6734B2922402DBEE452EAA493A6E50658906A0EE67099DFC87776E22EB476C4ED49725017BF156BC5F1F076558408CD32B8E0880E6365593D43AD33C31FAFCF7D07E055DF223A367173A643316A4006E6DC3E8DBDDE80935F35AFDDD",vid="h0027agjqb1")
    s.get_paly_url()