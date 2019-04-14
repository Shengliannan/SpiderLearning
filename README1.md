# SpiderLearning

### 爬虫库学习

##### 一、urllib库

> 参考：https://www.cnblogs.com/xiaoxi-3-/p/7586072.html

1.get方式提交

2.post方式提交

3.设置cookie登录

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

##### 二、urllib3库

##### 三、requests库

##### 四、BeautifulSoup库

***


### 框架学习

##### Scrapy

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



### 爬虫进阶：

##### 一、关于phantomJs
***PhantomJS：无界面的浏览器***
很多网站通过客户端渲染，直接读取源码根本读不到最终展现出来的html元素。
网页渲染可分为服务端渲染和客户端渲染，前者是指你在浏览器地址栏输入一个网址，Web服务器处理请求过程就将所有需要呈现的html元素都构造好了，浏览器收到响应就直接reader出页面，客户端工作量少；后者是指Web服务器仅仅将必要的信息作为响应传到浏览器，浏览器需要根据响应进行二次处理，比如ajax请求，在根据ajax请求的结果构造html。

***urllib不具备js执行能力，自然不能模拟浏览器执行js请求ajax的效果，于是，所谓无头浏览器phthomJs就出现了，借助这个工具可以模拟webkit执行，还可以包含更多js库比如JQuery等对页面的js进行扩展***。

***PhantomJS是一个而基于WebKit的服务端JavaScript API***,支持Web而不需要浏览器支持，其快速、原生支持各种Web标准：Dom处理，CSS选择器，JSON等等。PhantomJS可以用用于页面自动化、网络监测、网页截屏，以及无界面测试

参考：
>https://www.jianshu.com/p/0254391918f7
>http://www.fly63.com/article/detial/960



##### 二、Selenium

>[Selenium官网](https://www.seleniumhq.org/)

什么是硒？
Selenium自动化浏览器。它主要用于自动化Web应用程序已进行测试。
Selenium 是一套完整的web应用程序测试系统，包含了测试的录制（selenium IDE）,编写及运行（Selenium Remote Control）和测试的并行处理（Selenium Grid）。Selenium的核心Selenium Core基于JsUnit，完全由JavaScript编写，因此可以用于任何支持JavaScript的浏览器上。
Selenium可以模拟真实浏览器，自动化测试工具，支持多种浏览器，***爬虫中主要用来解决JavaScript渲染问题。Selenium基于Javascript并结合其WebDriver来模拟用户的真实操作，它有很好的处理Ajax的能力，并且支持多种浏览器（Safari，IE，Firefox，Chrome），可以运行在多种操作系统上面。***



##### 三、关于chrom无头浏览器

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

#####  四、 Selenium 之 操作 ChromeDriver 可配置项

> 参考：https://www.meiwen.com.cn/subject/fzudgxtx.html

在使用Selenium过程中，我们需要对Chrome做一些初始化设置，以便浏览器完成我们期望的行为。

ChromeOptions 可以在浏览器启动之前设置加载的选项。

ChromeOoptions 主要提供以下功能：

- 设置 chrome 文件位置（binary_location）
- 添加启动配置(arguments)
- 添加插件(add_extension)
- 添加设置参数(add_experimental_options)


##### 五、 IP代理

##### 六、 多线程爬虫

##### 七、打码平台接入

##### 八、不同验证码的识别（输入数字，文字或字母、 滑动验证码 、 点击特定的标识）

