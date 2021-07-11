# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time 
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC

# class twitterBot:
#     def __init__(self,username,password):
#         self.username = username
#         self.password = password
#         self.bot = webdriver.Firefox(executable_path="./geckodriver")

#     def login(self):
#         bot = self.bot
#         bot.get("https://instagram.com/")
#         time.sleep(3)
#         email=bot.find_element_by_name('username')
#         password=bot.find_element_by_name('password')

#         email.clear()
#         password.clear()
#         email.send_keys(self.username)
#         password.send_keys(self.password)
#         password.send_keys(Keys.RETURN)
#         time.sleep(3)

#     def remove_followers(self):
#         bot=self.bot
#         bot.get("https://www.instagram.com/wildfellow2021/following/")
        
#         time.sleep(3)

#         # button = bot.find_elements_by_class_name("aOOlW.HoLwm")
#         # print(button)
#         # button[0].click()
#         # button = bot.find_elements_by_class_name("_6q-tv")
#         # print(button)
#         # button[0].click()
#         # button = bot.find_elements_by_class_name("_7UhW9.xLCgt.MMzan.KV-D4.fDxYl");
#         # print(button)
#         # button[0].click()
#         button = bot.find_elements_by_class_name("g47SY");
#         print(button)
#         button[2].click()
#         # time.sleep(10)
#         xpath = "/html/body/div[5]/div/div/div[3]/ul/div/li["
#         xpath1 = "]/div/div[3]/button"
#         i=1
#         while(True):
#             button = WebDriverWait(bot, 20).until(EC.element_to_be_clickable((By.XPATH, xpath+str(i)+xpath1))).click()
#             button = bot.find_elements_by_class_name("aOOlW.-Cab_")
#             print(button)
#             button[0].click()
#             i+=1
#             # if(i==7):
#             #     self.remove_followers()
            
#         # button = WebDriverWait(bot, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='sqdOP  L3NKy    _8A5w5    ']"))).click()
#         # button = bot.find_elements_by_class_name("sqdOP.L3NKy._8A5w5")
#         # print("Unfollow buttons",": ", button)
#         # button[0].click()
        
#         # for i in range(1,4):
#         #     bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
#         #     time.sleep(2)
#         #     tweets=bot.find_elements_by_class_name('tweet')
#         #     links= [elem.get_attribute('data-permalink-path') for elem in tweets]
#         #     print(links)
#         #     for link in links:
#         #         bot.get("https://twitter.com"+ link)
#         #         try:
#         #             bot.find_element_by_class_name('HeartAnimation').click()
#         #             time.sleep(10)
#         #         except Exception as ex:
#         #             time.sleep(60)
# wr=twitterBot('wildfellow2021' , 'Sunil@fake')
# wr.login()
# wr.remove_followers()

from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

class InstaUnfollowers:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://instagram.com")
        sleep(2)
        # instagram login
        username_type = self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        username_type.send_keys(username)
        password_type = self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
        password_type.send_keys(password)
        # password_type.send_keys(Keys.RETURN)
        ad = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        ad.click()
        sleep(5)
        log_in = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        log_in.click()
        sleep(2)

    def get_unfollowers(self):
        # change to your username
        self.driver.get("https://www.instagram.com/grayjoy203/")
        sleep(3)
        Following = self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")
        Following.click()
        sleep(10)
        xpath = "/html/body/div[5]/div/div/div[3]/ul/div/li["
        xpath1 = "]/div/div[3]/button"
        i=1
        while(True):
            button = self.driver.find_element_by_xpath(xpath+str(i)+xpath1)
            button.click()
            sleep(1)
            button = self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[1]")
            button.click()
            i+=1
            sleep(3)
            if(i==6):
                self.get_unfollowers()
                
my_bot = InstaUnfollowers(<your_username> , <your_password>)
my_bot.get_unfollowers()
my_bot.driver.close()