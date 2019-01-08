# -*- coding:utf-8 -*-

import urllib
import urllib.request
url = "http://www.baidu.com"
html = urllib.request.urlopen(url)
#content = html.read()
#html.read()数据类型为 bytes 类型，经过 decode 解码转换成 string 类型
#默认是string类型，可以decode('utf-8')来指定解码格式。
content = html.read().decode()
print(content)



