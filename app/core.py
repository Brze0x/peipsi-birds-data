import re
from time import sleep
from app.models import FuncPeipsiBirds
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Parser:
    def __init__(self, arg: str, driver_path: str):
        """Initialize Parser class.\n
        Arguments:
            arg {str} -- chromium command line switch
            driver_path {str} -- chromium driver path
        Example:
            Parser('--headless', 'D:\chromedriver.exe'), 
            Parser('--window-size=800,600', 'D:\chromedriver.exe')), 
            Parser('--start-maximized', 'D:\chromedriver.exe')
        """
        self.url = 'https://birds.peipsi.org/'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(arg)
        self.options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
        self.options.add_experimental_option("useAutomationExtension", False)
        self.service = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
    

    def get_bird_data(self, bird_url: str, order: str, family: str) -> dict:
        """Get bird data from bird page.\n
        Arguments:
            bird_url {str} -- bird page url
            order {str} -- bird order
            family {str} -- bird family
        Returns:
            dict -- bird data
        """
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(url=bird_url)

        # content = driver.find_element(by=By.TAG_NAME, value='article')
        birds_info = self.driver.find_elements(By.CSS_SELECTOR, '.main>article p')
        bird_names = self.driver.find_element(by=By.TAG_NAME, value='h1')
        name_rus = re.match('^\w+(\s|-)?\w+\s([а-я]+)?\s?(\([а-яА-Я]+\s?[а-я]+\))?', bird_names.text).group(0)
        name_lat = re.findall('[a-zA-Z]+\s?[a-z]+', bird_names.text)[0]
        signs = birds_info[0].text.replace('Признаки.', '').strip()
        habitat = birds_info[1].text.replace('Местообитание.', '').strip()

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        return {
            'order': order,
            'family': family,
            'name_rus': name_rus,
            'name_lat': name_lat,
            'signs': signs,
            'habitat': habitat
        }


    def run(self):
        self.driver.get(self.url)
        self.driver.execute_script(
            "elements = document.getElementsByClassName('sym');"\
            "for (let elem of elements) {elem.click()}"
            )
        for link in self.driver.find_elements(by=By.TAG_NAME, value='a'):
            if re.findall('(reference)\/\w+\/$', link.get_attribute('href')):
                order = link.get_attribute('title').split(' ')[-1]
            elif re.findall('(reference)\/\w+\/[a-z-]+\/$', link.get_attribute('href')):
                family = link.get_attribute('title').split(' ')[-1]
            elif re.findall('\/(?!reference|en)[a-z]+\/\w+\/[a-z-0-9]+?\/$', link.get_attribute('href')):
                bird_data = self.get_bird_data(link.get_attribute('href'), order, family)
                FuncPeipsiBirds.add_bird(bird_data)
        sleep(5)
        self.driver.quit()

