#模拟浏览器
from selenium import webdriver
from time import sleep
dr = webdriver.Chrome()
dr.get("https://yeah.net/")
dr.implicitly_wait(100)
#选择密码登录
passwdlogin = dr.find_element_by_id("lbNormal")
passwdlogin.click()

#定位框架：
Iframe = dr.find_element_by_css_selector("#loginDiv > iframe")
#切换到框架
dr.switch_to.frame(Iframe)

#定位账号和密码并输入账号和密码值
account = dr.find_element_by_name('email').send_keys("shelly_sz")
password = dr.find_element_by_name('password').send_keys("wushili19970329")

login = dr.find_element_by_link_text("登  录")
login.click()

#写信
writter = dr.find_element_by_xpath(".//*[@id='_mail_component_149_149']/span[2]")
writter.click()

sleep(2)
#信件内容
#定位收件人
accept = dr.find_element_by_xpath('//*[@aria-label="收件人地址输入框，请输入邮件地址，多人时地址请以分号隔开"]').send_keys('408265178@qq.com')
#定位主题
theme = dr.find_element_by_xpath('//*[@class="nui-ipt-input" and @type="text"and @tabindex ]').send_keys('我来测试了')

#定位框架：
OneIframe = dr.find_element_by_xpath('//*[@frameborder="0" and @class="APP-editor-iframe" ]')
#切换到框架
dr.switch_to.frame(OneIframe)

#定位发送内容
content = dr.find_element_by_xpath('//*[@class="nui-scroll" and @contenteditable="true"  ] ').send_keys("hello，world")
dr.switch_to.default_content()#跳出文本框
#定位发送
Send = dr.find_element_by_css_selector('[tabindex="1"]').click()