import urllib.request
import http.cookiejar
"""
设置cookie绕过登录
"""


#url = "http://bdp.jd.com/jrdw/jdqClient/jdqClientManage/consumeTopic.html"
url = "http://bdp.jd.com/jrdw/topicManager/getClientListAjax.ajax?queryStr=&csId=&heartBeatCheck=0%2C1%2C2&type=2&masterStr=0&status=0&jsdAppGroupId=&proposer=&_search=false&nd=1546950743820&rows=10&page=1&sidx=&sord=asc"

#http.cookijar，用于获取cookie以及存储cookie
#cookie = http.cookiejar.CookieJar()
#cookie.add_cookie_header()
#handler=urllib.HTTPCookieProcessor(cookie)

html = urllib.request.urlopen(url)

#content = html.read()
#html.read()数据类型为 bytes 类型，经过 decode 解码转换成 string 类型
#默认是string类型，可以decode('utf-8')来指定解码格式。
content = html.read().decode()
#返回登录界面代码，需要登录，通过设置cookie绕过登录
print(content)
