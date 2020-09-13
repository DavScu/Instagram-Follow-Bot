from selenium import webdriver
import time #need time to allow us to wait for pages to load.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random

# chrome_options = webdriver.ChromeOptions(); 
# chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
# driver = webdriver.Chrome(options=chrome_options);  

#type in the hashtag thatu r interested in
hashtag = "#guitar"

class instafollow:
    def __init__(self, email, pw):
        # Open FB and get us to the fb page. Also maximises window.
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com")
        self.driver.maximize_window()
        time.sleep(2)
        # Login Phase
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(email) #passing in our variable.
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(pw)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]').click()
        time.sleep(2)
        # we are in and it says no notifications.
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        # enters our hashtag into the top search bar and presses enter. (Enter 2x)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(hashtag + Keys.ENTER)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div').click()
        time.sleep(4)
        #finds the first image in the grid and selects it.
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]').click()
        time.sleep(2)

        #This will like and then click forward for the first image, then it can enter the while loop.
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click() #1st like button
        self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a').click() #first moving forward button
        time.sleep(2)
        while True:
            try:
                sleeptime = random.uniform(1,2) # so insta doesn't think im a bot.
                #click like button
                self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click()  #2nd like button and so on
                time.sleep(sleeptime) 
                print("Slept for " + str(sleeptime))
                #click next button
                self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()
                time.sleep(sleeptime)
                print("Slept for " + str(sleeptime))
            except:
                print("It has failed. I am going to automatically restart this. ctrl z if you wouldn't like that.")
                self.driver.close()
                instafollow('','')
        
        
# You have to type your own account and password here
instafollow(account, password)
#enter your account and password