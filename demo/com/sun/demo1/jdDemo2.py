import urllib.request
import http.cookiejar
"""
设置cookie绕过登录
"""


url = "http://bdp.jd.com/jrdw/jdqClient/jdqClientManage/jdqClientList.html?jdqVersion=3"
#http.cookijar，用于获取cookie以及存储cookie
cookie = http.cookiejar.CookieJar()

html = urllib.request.urlopen(url)
#content = html.read()
#html.read()数据类型为 bytes 类型，经过 decode 解码转换成 string 类型
#默认是string类型，可以decode('utf-8')来指定解码格式。
content = html.read().decode()
#返回登录界面代码，需要登录，通过设置cookie绕过登录
print(content)
