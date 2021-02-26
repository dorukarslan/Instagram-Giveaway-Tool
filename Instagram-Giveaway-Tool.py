from selenium import webdriver

import time

browser = webdriver.Firefox()
""" login part """
browser.get("https://www.instagram.com/")
time.sleep(2)
idm = browser.find_element_by_name("username")
passw = browser.find_element_by_name("password")


# Fill the log and pas areas with your username and password
log = "your username here"
pas = "your password here"
idm.send_keys(log)
passw.send_keys(pas)
buton = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
buton.click()
time.sleep(7)
""" login end """



""" related post url """

# Write the URL of the post that you want to use.
browser.get("giveaway post's URL here ")
time.sleep(2)



area = browser.find_element_by_css_selector(".Ypffh")
area.click()
time.sleep(1)
area = browser.find_element_by_css_selector(".Ypffh")
area.click()
commentbutton = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button")
""" openning the file that contains followers"""



#In order to tag your whole followers three by three you need to use first project in gitHub(List of all Instagram followers.) --
#then you need to write its path down here.
# Note that if you do not want to tag your whole followers, you can create your own text file that contains your followers you want to tag, and use its path.
#However, your text files concepts must be similar(One name in every line).
""" r to make it raw string """
file = open(r"your path here", "r")
lines = file.readlines()
c = 0
for line in lines:
    area.send_keys("@",line)
    c +=1
    if (c%3 == 0):
        commentbutton.click()
        time.sleep(10)
        area = browser.find_element_by_css_selector(".Ypffh")
        area.click()
        time.sleep(2)
        area = browser.find_element_by_css_selector(".Ypffh")
        area.click()
        time.sleep(5)
commentbutton.click()     
time.sleep(1)
browser.close()
