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
            "adparam": "pf=in&ad_type=LD%7CKB%7CPVL&pf_ex=pc&url=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Ffgqtuu38z91hfyw%2Fh0027agjqb1.html&refer=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Ffgqtuu38z91hfyw%2Fh0027agjqb1.html&ty=web&plugin=1.0.0&v=3.5.57&coverid=fgqtuu38z91hfyw&vid=h0027agjqb1&pt=&flowid=cd7021b1f780f9822a630a4ea6863993_10201&vptag=www_baidu_com&pu=-1&chid=0&adaptor=2&dtype=1&live=0&resp_type=json&guid=c3ed01ec03a21050db27858ad6cd8f20&req_type=1&from=0&appversion=1.0.139&uid=241119669&tkn=47730947ee6695f300000000f0802b89a3468aa32c62&lt=qq&platform=10201&opid=96A774A2ACC02EBD09BFB659E5419832&atkn=17E8253E83CDCF818F97F93068F55F23&appid=101483052&tpid=1&rfid=11bb3527365ee03b120933b36539c21b_1550995743"
            ,"buid": "vinfoad"
            ,"vinfoparam":"charge=1&defaultfmt=auto&otype=ojson&guid=c3ed01ec03a21050db27858ad6cd8f20&flowid=cd7021b1f780f9822a630a4ea6863993_10201&platform=10201&sdtfrom=v1010&defnpayver=1&appVer=3.5.57&host=v.qq.com&ehost=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Ffgqtuu38z91hfyw%2Fh0027agjqb1.html&refer=v.qq.com&sphttps=1&tm=1551083974&spwm=4&logintoken=%7B%22main_login%22%3A%22qq%22%2C%22openid%22%3A%2296A774A2ACC02EBD09BFB659E5419832%22%2C%22appid%22%3A%22101483052%22%2C%22access_token%22%3A%2217E8253E83CDCF818F97F93068F55F23%22%2C%22vuserid%22%3A%22241119669%22%2C%22vusession%22%3A%2247730947ee6695f300000000f0802b89a3468aa32c62%22%7D&unid=7d523775a45e11e89d19a0429186d00a&vid={}&defn=&fhdswitch=0&show1080p=1&isHLS=1&dtype=3&sphls=2&spgzip=1&dlver=2&drm=32&hdcp=0&spau=1&spaudio=15&defsrc=1&encryptVer=8.1&cKey={}&fp2p=1&spadseg=1".format(self.vid,self.ck)

        }
        # self.proxies = {'http': '114.249.116.88:9000',}  ,proxies = self.proxies
    def get_paly_url(self):
        res = requests.get(url="https://vd.l.qq.com/proxyhttp",headers=self.head, data=self.data).text
        # print(json.loads(res)["vinfo"])
        null = ""
        print(res)
        # print(type(json.loads(res)))
        x=json.loads(json.loads(res)["vinfo"])
        # print(x)
        # print(type(x))
        # print(x["vl"]["vi"][0]["ul"]["ui"][0]["url"])
        # print(x["vl"]["vi"][0]["ul"]["ui"][0]["hls"]["pt"])
        # print(json.loads(res)["vinfo"]["vl"]["vi"][0]["ul"]["ui"][0]["url"])
        # print(json.loads(res)["vinfo"]["vl"]["vi"][0]["ul"]["ui"][0]["hls"]["pt"])
        # print(x)
        play_url = x["vl"]["vi"][0]["ul"]["ui"][0]["url"] + x["vl"]["vi"][0]["ul"]["ui"][0]["hls"]["pt"]
        # print(play_url)
        return play_url
        # return x
if __name__ == '__main__':
    s = serch_movies_new_big(ckey="0284615FC2D67889B822380F9B078E47A35354F764767C4CA3AE8255DB3FF795AAAFA601FF23696F65071FA4E7F21749DFA5A62B9EBC193809E1D9B34343CBCB59AFC14FCF5B512C9823CB27DEA615FDF9A33D8082628E30456E218D1A15B871EEB843617DF7AC32B05B3FACB5DA36C7327C509CB23FB91C0296356E3C0519E3AE739FBC8D22E319BDF8C7EB6A5FA9CB2A8B7D451CF4AC56203D9404A413C440B9413ADE57C9003202D9C6728EF7095CCDDABB194FAA86545F3E1F6FB333E5643B8FADED05B2A024B148EAF936ACA47BA0D38A0812394450EF1351058768B305",vid="h0027agjqb1")
    s.get_paly_url()