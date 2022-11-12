# 目前支持的浏览器：
# Chrome
# Edge
# Opera
# IE

# 需要另外安装库：
# Selenium 4
# webdriver-manager


# 上次更新-暂停处
# 展开评论-循环事件
# 公开评论-未知



# 导入库
print("正在尝试导入库")
import os
import sys
import time

# 尝试引入Selenium库。
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.firefox.service import Service
    from selenium.webdriver.firefox.options import Options
except:
    # 如果没有安装Selenium库则会退出。
    print("请先安装Selenium库，该程序将会终止。")
    os.system('pause')
    sys.exit()
try:
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.microsoft import EdgeChromiumDriverManager
    from webdriver_manager.firefox import GeckoDriverManager
    from webdriver_manager.opera import OperaDriverManager
    from webdriver_manager.microsoft import IEDriverManager
except:
    # 如果没有安装webdriver-manager库则会警告。
    print("警告：您可能未安装webdriver-manager库")
    print("请注意，您可能未安装webdriver-manager库，如果您已安装webdriver-manager库，可能是您正在使用编辑器运行此程序的远古，如果尚未安装webdriver-manager库，您则需要另外配置webDriver，webdriver-manager库仅用作自动 配置/安装 webDriver。")
    print("按任意键将会在无webdriver-manager库的状态下运行，可能会导致程序无法在预期内运行。")
    os.system('pause')
# 初始化
print("正在初始化")
webDrivers = []
i = 1
print("定义函数中")
# function
def clickElement(Xpath):
    while len(driver.find_elements(By.XPATH,Xpath)) < 1:
        print(len(driver.find_elements(By.XPATH,Xpath)))
        print(driver.find_elements(By.XPATH,Xpath))
        time.sleep(1)
    try:
        driver.find_element(By.XPATH,Xpath).click()
    except:
        button = driver.find_element(By.XPATH,Xpath)
        driver.execute_script("$(arguments[0]).click()",button)
def send_keys_to_Element(Xpath, keys):
    while len(driver.find_elements(By.XPATH,Xpath)) < 1:
        print('寻找输入框中')
    driver.find_element(By.XPATH,Xpath).send_keys(keys)

def publicComments():
    driver.execute_script("setInterval(() => {document.querySelectorAll('.comment_handleBtn_hP56Y>*').forEach(item => {if (item.innerHTML == '公开' && Blockey.Utils.getContext().targetType != 'ForumPost') {item.click();}});}, 1000)")

def publicAllComments():
    while True:
        try:
            eles = driver.find_elements(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[4]/div")
            ele = eles[0]
            driver.execute_script("arguments[0].scrollIntoView();",ele)
        except:
            pass
        if len(driver.find_elements(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[4]/div/div[2]/div[2]/div[2]/ul/li[1]/div/div[2]/div[1]/span[2]")) >= 1:
            print("找到评论")
            break
        elif len(driver.find_elements(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[4]/div/div[2]/div[3]/span")) >= 1:
            print("找到展开按钮")
            while len(driver.find_elements(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[4]/div/div[2]/div[2]/div[2]/ul/li[1]")) < 1:
                clickElement("/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[4]/div/div[2]/div[3]/span")
            break
    print("开始公开评论")
    i = i + 1
    while True:
        if len(driver.find_elements(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[4]/div/div[2]/div[2]/div[2]/ul/li[" + str(i) + "]")) < 1:
            if len(driver.find_elements(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[4]/div/div[2]/div[3]/span")) == 1:
                clickElement("/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[4]/div/div[2]/div[3]/span")
                while len(driver.find_elements(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[4]/div/div[2]/div[2]/div[2]/ul/li[" + str(i) + "]")) == 1:
                    pass
            else:
                time.sleep(4)
                publicComments()
                if len(driver.find_elements(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[4]/div/div[2]/div[3]/span")) < 1:
                    break
        else:
            i = i + 1
        publicComments()

os.system('cls')
agree = None
while True:
    agree = input('该程序会检测并安装这个系统所有可用的浏览器的webDriver，你同意安装吗？（Y/N）:')
    if agree == "Y" or agree == "N":
        break
if agree == "Y":
    print('检测中')
    # Chrome
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    except:
        try:
            driver = webdriver.Chrome()
        except:
            pass
        else:
            webDrivers.append('Chrome')
    else:
        webDrivers.append('Chrome')
    # EdgeDriver
    try:
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    except:
        try:
            driver = webdriver.Edge()
        except:
            pass
        else:
            webDrivers.append('Edge')
    else:
        webDrivers.append('Edge')
    # OperaDriver
    try:
        driver = webdriver.Opera(executable_path=OperaDriverManager().install())
    except:
        try:
            driver = webdriver.Opera()
        except:
            pass
        else:
            webDrivers.append('Opera')
    else:
        webDrivers.append('Opera')
    # IEDriver
    try:
        driver = webdriver.Ie(IEDriverManager().install())
    except:
        try:
            driver = webdriver.Ie()
        except:
            pass
        else:
            webDrivers.append('IE')
    else:
        webDrivers.append('IE')
    driver.quit()
wd = -2333
while True:
    while isinstance(wd, int) and wd <= -1 or wd > len(webDrivers) + 1:
        if agree == "Y":
            print('当前可用浏览器如下')
            for x in range(len(webDrivers)):
                print(str(x + 1) + "," + webDrivers[x])
            print("输入序号以选择您想使用的webDriver")
        else:
            print('你想 安装/使用 哪些浏览器的webDriver?')
            print("1、Chrome")
            print("2、Edge")
            print("3、Opera")
            print("4、IE")
            webDrivers = ['Chrome','Edge','Operra','IE']
        wd = input()
        wd = int(wd)
        nikeName = input('输入你的用户名:')
        psw = input('输入你的用户密码:')
    print("正在尝试启动webDriver")
    if webDrivers[int(wd) - 1] == 'Chrome':
        try:
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        except:
            driver = webdriver.Chrome()
    elif webDrivers[int(wd) - 1] == 'Edge':
        try:
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        except:
            driver = webdriver.Edge()
    elif webDrivers[int(wd) - 1] == 'Opera':
        try:
            driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        except:
            driver = webdriver.Opera()
    elif webDrivers[int(wd) - 1] == 'IE':
        try:
            driver = webdriver.Ie(IEDriverManager().install())
        except:
            driver = webdriver.Ie()
    try:
        driver.find_elements(By.XPATH,"/html/body")
    except:
        os.system('cls')
        print("启动失败，请尝试更换浏览器")
        wd = -2333
    else:
        break

# - - - - - -

# 自动操作
# 登录
driver.get("https://gitblock.cn/#")
while len(driver.find_elements(By.XPATH,"/html/body/div[3]/div/div/div/div[2]/form/div[1]/input")) < 1:
    try:
        clickElement("/html/body/div[2]/div[1]/div/div/div[2]/div[1]/ul/li[2]/a")
    except:
        pass
send_keys_to_Element("/html/body/div[3]/div/div/div/div[2]/form/div[1]/input",nikeName)
send_keys_to_Element("/html/body/div[3]/div/div/div/div[2]/form/div[2]/input",psw)
clickElement("/html/body/div[3]/div/div/div/div[2]/form/div[3]/button")
while driver.get_cookie("gitblock-auth") == None:
    pass
# 自动公开个人主页评论
clickElement("/html/body/div[2]/div[1]/div/div/div[2]/div[2]")
clickElement("/html/body/div[2]/div[1]/div/div/div[2]/div[3]/div/ul/li[1]/a")
publicAllComments()


print("成功公开所有评论！")
os.system('pause')
