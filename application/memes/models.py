from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class YoutubeController(object):
    def __init__(self):
        self.driver = None
        self.url_check = 'youtube.com'
        self.timeout = 3
        self.play_button = None
        self.popup_path = '/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/ \
            div[4]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a/tp-yt-paper-button/yt-formatted-string'
    
    def start_driver(self):
        try:
            self.driver.quit() #quit driver if already exists
        except:
            self.driver = webdriver.Chrome(ChromeDriverManager().install()) #setup new driver
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    
    def open_url(self, url: str): #probably need a refactor xD
        if self.url_check not in url:
            raise Exception('Controller is supposed to run youtube urls!')
        self.start_driver()
        self.play_button = None #if there is already stored button delete it
        self.driver.get(url)
        self.close_popup() #closing annoying popup on YT without login
        self.play_button = self.get_play_button() #assigning new play button
        
    def close_popup(self):
        try:
            #Wait until annoying popup pop and fuckin close it, thanks
            WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((By.XPATH, self.popup_path))).click()
        except:
            pass
        
    def get_play_button(self):
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'ytp-play-button'))
            WebDriverWait(self.driver, self.timeout).until(element_present)
            return self.driver.find_element_by_class_name('ytp-play-button')
        except:
            pass
        
    def pause_play_video(self):
        if self.play_button is not None:
            self.play_button.click() #click to pause and unpause if button is there
        else:
            print('play button is not assigned yet!')
            
    def close_video(self):
        self.driver.quit()
            
    