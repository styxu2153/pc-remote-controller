from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

twitch_windows = {}

class TwitchController(object):
    def __init__(self, twitch_username):
        self.url = f'https://twitch.tv/{twitch_username}'
        self.name = twitch_username
        self.timeout = 5
        self.volume = 0
        
        #Driver Setup on Init
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.player = self.get_player()
        self.unmute_stream()
    
    def decrease_volume(self, value: int):
        try:
            self.volume = max(-47, self.volume - value)
            element = self.driver.find_element(By.CLASS_NAME, "ScRangeInput-sc-1qrd37x-0")
            move = ActionChains(self.driver)
            move.click_and_hold(element).move_by_offset(self.volume, 0).release().click().perform()
        except:
            print('Failed to decrease volume')

    def increase_volume(self, value: int):
        try:
            self.volume = min(47, self.volume + value)
            element = self.driver.find_element(By.CLASS_NAME, "ScRangeInput-sc-1qrd37x-0")
            move = ActionChains(self.driver)
            move.click_and_hold(element).move_by_offset(self.volume, 0).release().click().perform()
        except:
            print('Failed to increase volume')
    
    def unmute_stream(self):
        try:
            self.player.click()
        except:
            print('Failed!')
        
    def get_player(self):
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'persistent-player'))
            WebDriverWait(self.driver, self.timeout).until(element_present)
            return self.driver.find_element_by_class_name('persistent-player')
        except:
            print('Couldnt find element!')
            
    def close_video(self):
        self.driver.quit()
        



