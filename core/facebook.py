from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time 
from core import models as core_model
from django.http import HttpResponse
# webdriver path set 
def post(request):
    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-notifications")

    browser = webdriver.Chrome(options=chrome_options)
  
    browser.maximize_window() 
      
    browser.get('https://www.facebook.com/') 
      
    # Enter your user name and password here. 
    username = "username"
    password = "password"
     
    a = browser.find_element_by_id('email')  
    a.send_keys(username) 
      
    # password send 
    b = browser.find_element_by_id('pass')  
    b.send_keys(password) 
      
    # submit button clicked 
    browser.find_element_by_id('loginbutton').click() 

    browser.get('https://www.facebook.com/') 

    msg = "WelCome to Webllisto Family ,We provide expert web advancement solutions to overpass the gap between you and your audience. Our service is straight forward, and We focus on satisfaction with our customers all over the world by helping them to accomplish their goals most cost-effectively. As one of the best digital agencies, We have more than 6+ years of industry experience in development and been supporting multiple companies." 

    # auto post on facebook
    try:
        browser.find_element_by_xpath("//textarea[@name='xhpc_message']").send_keys(msg)
        time.sleep(5)
        browser.find_element_by_xpath("//*[text()='Post']").click()
        time.sleep(5)
    except :
        pass
    # auto comment on facebook post
    try:
        browser.find_element_by_xpath("//div [@data-testid='UFI2CommentsList/root_depth_0']").click()
        time.sleep(5)
        browser.find_element_by_class_name("_1mf").send_keys("fantastic")
        time.sleep(5)
        browser.find_element_by_class_name("_1mf").send_keys(Keys.ENTER)
    except:
        pass

    try:
        posts = browser.find_elements_by_xpath("//div [@data-testid='post_message']")
        for post in posts:
            post1 = post.text
            ids = post.id
            obj = core_model.Facebook.objects.create(post_id=ids, post=post1)
    except :
        pass  
    browser.close() 
    return HttpResponse('scraped successfully')



