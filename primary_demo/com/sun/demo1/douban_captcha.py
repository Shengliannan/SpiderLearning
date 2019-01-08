import urllib
import urllib.request
"""
UserWarning: Selenium support for PhantomJS has been deprecated, please use headless versions of Chrome or Firefox instead
  warnings.warn('Selenium support for PhantomJS has been deprecated, please use headless '

selenium已经放弃PhantomJS，了，建议使用火狐或者谷歌无界面浏览器。
新版的 selenium已经放弃PhantomJS改用Chorme headless
解决办法参考：
https://www.jianshu.com/p/d2f1b05aa79e
"""

URL = 'https://movie.douban.com/'
username = '1066219863@qq.com'
password = 'mRhACKER1993'
#movie = '后来的我们‎'
from selenium import webdriver

#使用PhantomJS
brower = webdriver.PhantomJS(executable_path=r"C:\Users\suntiansheng2\Downloads\phantomjs-2.1.1-windows\bin\phantomjs.exe")
#wait = ui.WebDriverWait(brower,10)

# 登录
def login(url, username, password):
    brower.get(url)
    brower.find_element_by_css_selector('[class="nav-login"]').click()
    name = brower.find_element_by_id('email')
    name.clear()
    name.send_keys(username)
    pwd = brower.find_element_by_id('password')
    pwd.clear()
    pwd.send_keys(password)
    #有的时候第一次登陆或者登陆不频繁，不需要输入验证码，页面就弹出验证码的控件
    try:
        pic_src = brower.find_element_by_id('captcha_image').get_attribute('src')
        # 调用获取验证码的方法
        cap_value = get_yzm(pic_src)
        yan_zheng_ma = brower.find_element_by_id('captcha_field')
        yan_zheng_ma.clear()
        yan_zheng_ma.send_keys(cap_value)
    except:
        print("不用输入验证码！！！")

    brower.find_element_by_css_selector('[class="btn-submit"]').click()
    print(brower.page_source)
    print('登陆成功')
    #print(urllib.request.urlopen(url).read().decode())
    #print(brower.find_element_by_css_selector('[class="nav-login"]'))
    #生成新的页面快照
    brower.save_screenshot('itcast.png')
# 获取验证码
def get_yzm(src):
    print("正在保存验证码图片")
    captchapicfile = "D:\spiderTest\SpiderLearning\demo\com\sun\demo1\captcha.png"
    #urlretrieve函数是将远程数据
    urllib.request.urlretrieve(src, filename=captchapicfile)
    print("请打开图片文件，查看验证码，输入单词......")
    captcha_value = input()
    return captcha_value

if __name__=="__main__":
    login(URL,username,password)