"""
from selenium import webdriver
# selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home
# 需要指定定chromedriver.exe的路径
browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
print(browser.page_source)
browser.close()
"""

from selenium import webdriver

# 创建chrome参数对象
opt = webdriver.ChromeOptions()
# 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
"""
DeprecationWarning: use setter for headless property instead of set_headless
opt.set_headless()
因为opt.set_headless()已经弃用了，所以使用opt.headless = True
可以用 opt.headless = False
也可以这样写：opt.add_argument('--headless')
opt.headless = False 会打开一个Chrome浏览器，True不会打开浏览器
"""
opt.headless = True
# 创建chrome无界面对象
driver = webdriver.Chrome(executable_path='C:\\Users\\suntiansheng2\\Downloads\\chromedriver_win32\\chromedriver.exe',options=opt)
# 访问百度
driver.get('https://baidu.com/')
#打印内容
print(driver.page_source)
