from flask import Flask,redirect,render_template,url_for,request
from get_info_vip_list import get_vip_info_list
from get_serch_html import serch_html
from get_movies_src import get_movie_index
class Config():
    #表单 的配置
    WTF_CSRF_ENABLE=True
    SECRET_KEY="www.xueyiyang.top"
app = Flask(__name__)
app.config.from_object(Config)

@app.route('/',methods=["GET","POST"])
def index():
    from forms import form_serch
    c = get_vip_info_list()
    info = c.get_items_info()
    # print(info)
    form = form_serch()
    if form.validate_on_submit():
        name = form.name.data
        return redirect(url_for("serch_movie",name = name))
    return render_template("/index.html",info_list = info,form = form)
@app.route('/serch_movie')
def serch_movie():
    name = request.args.get("name")
    s = serch_html(name)
    data = s.get_html()
    #        data = {"url":url,"url_img":url_img,"url_h2":html.unescape(url_h2),"url_div":html.unescape(url_div)}
    # print("*****",data)
    return render_template("/serch_movie_data.html",data = data,name = name)
@app.route('/play_movie')
def play_movie():
    url = request.args.get("url")
    print(url)
    s = get_movie_index(url=url)
    print("pk")
    src_url = s.run()
    # return "ok"
    # 默认 /ppvod/316F2512E37A26725B3B703D2AEDF36E.m3u8
    print("**********",src_url)
    # html_text = '<source src= "{}" type="application/x-mpegURL">'
    try:
        if src_url == "/hls/index.m3u8":
            src_url = s.if_not_success()
            print(src_url)
            return render_template("/player.html", src_r= src_url)
        return render_template("/player.html",src_r = "//cn2.zuidadianying.com"+src_url)
    except :
        src_url = "//jx.api.163ren.com/vod.php?url="+url
        return render_template("/player.html",src_r = src_url)


if __name__ == '__main__':
    app.run()
