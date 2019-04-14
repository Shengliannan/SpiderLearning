# SpiderLearning

***

### 一、python环境

#### 1. python安装和多版本控制

#### 2. python常见错误总结

python版本：Python 3.7.1

操作系统：windows 10

##### 2.1. 安装scrapy出错：（pip install scrapy）
```powershell
   building 'twisted.test.raiser' 
   extensionerror: Microsoft Visual C++ 14.0 is required. 
   Get it with "Microsoft Visual C++ Build Tools":             https://visualstudio.microsoft.com/downloads/
```

解决方案：
```
在http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted 下载**twisted**对应版本的whl文件（如我的Twisted-18.9.0-cp37-cp37m-win_amd64.whl），cp后面是python版本，amd64代表64位，
运行命令：
pip install Twisted-18.9.0-cp37-cp37m-win_amd64.whl
然后再运行pip intall srapy
成功。
```

##### 2.2.    ModuleNotFoundError: No module named 'win32api'
问题描述：安装配置scrapy后，编写了爬虫程序，执行***scrapy crawl 蜘蛛名*** 提示：    

import win32api
ModuleNotFoundError: No module named 'win32api'

问题原因：

因为Python没有自带访问windows系统API的库的，需要下载第三方库。库的名称叫pywin32，可以从网上直接下载，下载链接：http://sourceforge.net/projects/pywin32/files%2Fpywin32/ （下载适合你的Python版本）

解决办法

（1）pip install pywin32(亲测可以)

（2）库的名称叫pywin32，可以从网上直接下载，下载链接：http://sourceforge.net/projects/pywin32/files%2Fpywin32/ （下载适合你的Python版本）（适合的python版本不好对应）

##### 2.3.  TypeError: can't concat str to bytes

问题描述：pipelines.py 处理数据，写入文件,代码如下：

```python
class MoviePipeline(object):
    def process_item(self, item, spider):
        with open("my_meiju.txt",'a') as fp:
            fp.write(item['name'].encode("utf8") + '\n')
```

报错：

```
fp.write(item['name'].encode("utf8") + '\n')
TypeError: can't concat str to bytes
```

分析原因：

encode是编码，编码后是bytes类型的，bytes不能转化为str类型。

举个栗子：

```python
# 注：utf8和utf-8都可以，没有区别
print("你好".encode("utf8"))
print(type("你好".encode()))
print("你好".encode().decode())
print(type(("你好".encode().decode())))

输出：
b'\xe4\xbd\xa0\xe5\xa5\xbd'
<class 'bytes'>
你好
<class 'str'>
```

***

### 二、python 语法学习
#### 读写CSV文件
#### python数据结构的常见用法以及转换
#### 读写excel文件
#### 路径
#### 常见库介绍及其用法
- os
- sys
- random
- data
- datatime
- 

##### 3.1. urllib库

> 参考：https://www.cnblogs.com/xiaoxi-3-/p/7586072.html

(1) get方式提交

(2) post方式提交

(3) 设置cookie登录

***登录前后页面Request Headers显示的Cookie不同。***

cookie流程

![cookie流程](https://raw.githubusercontent.com/Shengliannan/SpiderLearning/master/image/Http%E8%AF%B7%E6%B1%82%E5%93%8D%E5%BA%94cookie.PNG)

（1）设置header,构建一个已经登录过的用户的headers信息

```python
import urllib.request

# 构建一个已经登录过的用户的headers信息
headers = {
"Cookie":
    """
    k:v;...
    """,
"Host": "XXX",
"Upgrade-Insecure-Requests":
"User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
url="xxx"
# 通过headers里的报头信息（主要是Cookie信息），构建Request对象
request = urllib.request.Request(url, headers = headers)
# 直接访问renren主页，服务器会根据headers报头信息（主要是Cookie信息），判断这是一个已经登录的用户，并返回相应的页面
response = urllib.request.urlopen(request)
# 打印响应内容
print (response.read().decode())
```

（2）

##### 3.2. urllib3库

##### 3.3 requests库

> [requests学习](http://docs.python-requests.org/zh_CN/latest/user/quickstart.html)

requests是用python语言基于urllib编写的，采用的是Apache2 Licensed开源协议的HTTP库，Request比urllib库方便些，requests库是python实现的最简单易用的HTTP库。

##### 3.4. BeautifulSoup库

***


### 四、框架学习

##### 1. Scrapy

学习资源

> [Scrapy中文网](http://www.scrapyd.cn/)
>
> [Scrapy简单入门及实例讲解](https://www.cnblogs.com/kongzhagen/p/6549053.html)

scrapy简介

Scrapy是一个为了爬取网站数据，提取结构性数据而编写的应用框架。其可以应用在数据挖掘，信息处理或存储历史数据等一些列的程序中。其最初是为了页面抓取（更确切来说，网络抓取）所设计的，也可以应用在获取API所返回的数据（例如Amazon Associates Web Services）或者通用的网络爬虫。

Scrapy使用了***Twisted异步网络***来处理网络通讯。整体架构大致如下

![Scrapy架构](https://raw.githubusercontent.com/Shengliannan/SpiderLearning/master/image/Scrapy%E6%A1%86%E6%9E%B6%E6%9E%B6%E6%9E%84.png)

Scrapy主要包括了以下组件：

- 引擎(Scrapy)

  用来处理整个系统的数据流，触发事务（框架核心）

- 调度器(Scheduler)

  用来接受引擎发过来的请求，压入队列中，并在引擎再次请求的时候返回。可以想象成一个URL（抓取网页的网址或者说是链接）的优先队列，由它来决定下一个要抓取的网址是什么，同时去除重复的网址。

- 下载器(Downloader)

  用于下载网页的内容，并将网页内容返回给蜘蛛（***Scrapy下载器时候建立在twisted这个高效的异步模型上的***）

- 爬虫(Spiders)

  爬虫是主要干活的，用于从特定的网页中提取自己需要的信息，即所谓的实体(Item)。用户也可以从中提取出链接，让Scrapy继续抓取下一个页面

- 项目管道(Pipeline)

  负责处理爬虫从网页中抽取到的实体，主要的功能是持久化实体、验证实体的有效性、清除不需要的信息。当页面被爬虫解析后，将被发送到项目管道，并经过几个特定的次序处理数据。

- 下载器中间件(Downloader Middlewares)

  位于Scrapy引擎和下载器之间的框架，主要是处理Scrapy引擎与下载器之间的请求及响应。

- 爬虫中间件(Spider Middlewares)

  介于Scrapy引擎和爬虫之间的框架，主要工作是处理蜘蛛的响应输入和请求输出。

- 调度中间件(Scheduler Middlewares)

  基于Scrapy引擎和调度之间的中间件，从Scrapy引擎发送到调度的请求和响应。

Scrapy运行流程大致如下：

1. 引擎从调度器中取出一个链接(URL)用于接下来的抓取
2. 引擎把URL封装成一个请求(Request)传给下载器
3. 下载器把资源下载下来，并封装成应打包(Response)
4. 爬虫解析Response
5. 解析出实体(Item)，则交给实体管道进行进一步的处理
6. 解析出的是链接(URL)，则把URL交给调度器等待抓取

一个Scrapy项目

（1）新建虚拟环境

```powershell
virtualenv scrapy
```
（2）新建scrapy项目
```
scrapy startproject scrapyDemo
```

（3）新建蜘蛛

```
# meiju是spider目录下的爬虫文件，meijutt.com是爬虫名字
scrapy genspider meiju meijutt.com
```

firstSpider.py

目录结构
|—scrapyDemo
| |—spiders
| | |—_init_.py
| | |—firstSpider.py


（4）运行蜘蛛
```
# 这个命令需要和scrapy.cfg同一目录下执行
scrapy crawl 蜘蛛名
```
注意：蜘蛛名是firstSpider.py文件总定义的name属性，不是文件名

四、scrapy的常用语法

4.1 scrapy数据提取

- css选择器
- XPath选择器

> [XPath学习资源](http://www.runoob.com/xpath/xpath-tutorial.html)

XPath比较复杂，若想快速开发可以使用XPath Helper(一种快速定位页面元素并返回Xpath路径的可视化工具：chrome插件)，安装使用方法：

> 参考：[XPath Helper 安装使用教程](https://blog.csdn.net/Cayny/article/details/81396711)

（1）css选择器

```python
# 提取的一个Selector的列表
>>> response.css('title')
# extract() 函数提取标签的列表
>>> response.css('title').extract()
# 提取标签
>>>  response.css('title').extract()[0]
# extract_first()就提取标签列表第一个标签
>>> response.css('title::text').extract_first()
# 提取标签中的内容
>>> response.css('title::text').extract_first()
# 提取标签中的属性
# 提取属性我们是用：“标签名::attr(属性名)”，比如我们要提取url表达式就是：# a::attr(href)，要提取图片地址的表达式就是：img::attr(src)
>>> response.css("a::attr(href)")

```

> [css高级用法](http://www.scrapyd.cn/doc/185.html)

五、scrapy断点调试

> [scrapy断点调试](https://www.cnblogs.com/weixuqin/p/9074448.html)

***

### 必备知识：

一、JSON
JSON(JavaScript Object Notation)



> [JSON官网](http://json.org)

二、正则表达式



三、编码&解码

（1）JS编码&解码

- encodeURIComponent()/decodeURIComponent()

  ```html
  <html>
  <body>
  <script type="text/javascript">
  <!-- 编码：以父为名 编码结果：%E4%BB%A5%E7%88%B6%E4%B8%BA%E5%90%8D -->
  document.write(encodeURIComponent("以父为名"))
  document.write("<br/>")
  <!-- 解码：%E4%BB%A5%E7%88%B6%E4%B8%BA%E5%90%8D 解码结果: 以父为名 -->
  document.write(decodeURIComponent("%E4%BB%A5%E7%88%B6%E4%B8%BA%E5%90%8D"))
  </script>
  </body>
  </html>
  ```

（2）python编码解码

* urllib中的编码&解码 

  quote/unquote

  ```python
  >>> import urllib.parse as parse
  >>> print(parse.quote("以父为名"))
  %E4%BB%A5%E7%88%B6%E4%B8%BA%E5%90%8D
  >>> print(parse.unquote("%E4%BB%A5%E7%88%B6%E4%B8%BA%E5%90%8D"))
  以父为名
  ```




（3）js前端和后台python交互




四、爬虫攻防

![爬虫攻防](https://raw.githubusercontent.com/Shengliannan/SpiderLearning/master/image/%E7%88%AC%E8%99%AB%E6%94%BB%E9%98%B2.jpg)

五、 python对excel文件的操作
涉及库：xlrd、xlwt
> [用python读写excel（xlrd、xlwt）](https://www.cnblogs.com/MrLJC/p/3715783.html)
***

### 五、爬虫进阶：

##### 5.1. 关于phantomJs
***PhantomJS：无界面的浏览器***
很多网站通过客户端渲染，直接读取源码根本读不到最终展现出来的html元素。
网页渲染可分为服务端渲染和客户端渲染，前者是指你在浏览器地址栏输入一个网址，Web服务器处理请求过程就将所有需要呈现的html元素都构造好了，浏览器收到响应就直接reader出页面，客户端工作量少；后者是指Web服务器仅仅将必要的信息作为响应传到浏览器，浏览器需要根据响应进行二次处理，比如ajax请求，在根据ajax请求的结果构造html。

***urllib不具备js执行能力，自然不能模拟浏览器执行js请求ajax的效果，于是，所谓无头浏览器phthomJs就出现了，借助这个工具可以模拟webkit执行，还可以包含更多js库比如JQuery等对页面的js进行扩展***。

***PhantomJS是一个而基于WebKit的服务端JavaScript API***,支持Web而不需要浏览器支持，其快速、原生支持各种Web标准：Dom处理，CSS选择器，JSON等等。PhantomJS可以用用于页面自动化、网络监测、网页截屏，以及无界面测试

参考：
>https://www.jianshu.com/p/0254391918f7
>http://www.fly63.com/article/detial/960

##### 5.2 Selenium

>[Selenium官网](https://www.seleniumhq.org/)

什么是硒？
Selenium自动化浏览器。它主要用于自动化Web应用程序已进行测试。
Selenium 是一套完整的web应用程序测试系统，包含了测试的录制（selenium IDE）,编写及运行（Selenium Remote Control）和测试的并行处理（Selenium Grid）。Selenium的核心Selenium Core基于JsUnit，完全由JavaScript编写，因此可以用于任何支持JavaScript的浏览器上。
Selenium可以模拟真实浏览器，自动化测试工具，支持多种浏览器，***爬虫中主要用来解决JavaScript渲染问题。Selenium基于Javascript并结合其WebDriver来模拟用户的真实操作，它有很好的处理Ajax的能力，并且支持多种浏览器（Safari，IE，Firefox，Chrome），可以运行在多种操作系统上面。***

##### 5.3. 关于chrom无头浏览器

>[chromdriver官网](https://sites.google.com/a/chromium.org/chromedriver/getting-started)

随着越来越多的web数据都是经过js处理的，对于爬虫来说有很大的难度，一般情况使用selenium+phathomJs来解析执行js，但是2017年4月份后selenium不再维护pathomJs接口，可以用headless chrom或 firefox。Chrome从59版本开始 推出了 headless mode（当时仅支持Mac和Linux），而目前最新的Chrome63版已经开始在windows上支持headless mode。
```python
'Selenium support for PhantomJS has been deprecated, please use headless versions of Chrome or Firefox instead'
```

解决办法：

1. 使用低版本的Selenium
2. 使用headless version of Chrom or Firefox

>参考：https://blog.csdn.net/u010358168/article/details/79749149


使用第二种方法：

前提条件： 

- 本地安装Chrome浏览器 
- 本地需要[chromedriver](https://sites.google.com/a/chromium.org/chromedriver/home)驱动器文件，如果不配置环境变量的话，需要手动指定`executable_path`参数。

python代码：（Selenium+chromedriver）

```python

import time
from selenium import webdriver
"""
refer:
https://sites.google.com/a/chromium.org/chromedriver/getting-started
eg：通过chrome自动搜索周杰伦
"""
# 创建chrome参数对象
opt = webdriver.ChromeOptions()
# 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
opt.headless = True
#chromedriver.exe的路径
driver = webdriver.Chrome('C:\\Users\\suntiansheng2\\Downloads\\chromedriver_win32\\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('http://www.baidu.com');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_id('kw')
search_box.send_keys('周杰伦')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()
```

#####  5.4. Selenium 之 操作 ChromeDriver 可配置项

> 参考：https://www.meiwen.com.cn/subject/fzudgxtx.html

在使用Selenium过程中，我们需要对Chrome做一些初始化设置，以便浏览器完成我们期望的行为。

ChromeOptions 可以在浏览器启动之前设置加载的选项。

ChromeOoptions 主要提供以下功能：

- 设置 chrome 文件位置（binary_location）
- 添加启动配置(arguments)
- 添加插件(add_extension)
- 添加设置参数(add_experimental_options)

##### 5.5 IP代理

西刺代理、快代理

##### 5.6. 多线程爬虫

##### 5.7. 分布式爬虫

##### 5.8. 打码平台接入

##### 5.9. 不同验证码的识别（输入数字，文字或字母、 滑动验证码 、 点击特定的标识）
