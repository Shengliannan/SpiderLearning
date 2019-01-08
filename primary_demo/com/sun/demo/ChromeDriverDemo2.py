import time
from selenium import webdriver
"""
refer:
https://sites.google.com/a/chromium.org/chromedriver/getting-started
eg：通过chrome自动搜索周杰伦
"""
#chromedriver.exe的路径
driver = webdriver.Chrome('C:\\Users\\suntiansheng2\\Downloads\\chromedriver_win32\\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('http://www.baidu.com');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_id('kw')
search_box.send_keys('周杰伦')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()