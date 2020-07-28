
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as OpcionesChrome
from functions.conf import configuration
class Selenium:
    ##########################################################################
    ##############   -=_INICIALIZAR DRIVERS_=-   #############################
    ##########################################################################
    def open_browser(self, URL=configuration.URL, navegador=configuration.browser):
        self.ventanas = {}
        print("----------------")
        print(navegador)
        print(URL)
        print(configuration.basedir)
        print("---------------")


        if navegador == ("CHROME"):
            options = OpcionesChrome()
            options.add_argument('start-maximized')
            self.driver = webdriver.Chrome(
                chrome_options=options,
                executable_path=configuration.basedir + "\\drivers\\chromedriver.exe"
            )
            self.driver.implicitly_wait(10)
            self.driver.get(URL)
            self.principal = self.driver.window_handles[0]
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            return self.driver

        if navegador == ("CHROME_headless"):
            options = OpcionesChrome()
            options.add_argument('headless')
            options.add_argument('--start-maximized')
            self.driver = webdriver.Chrome(chrome_options=options,
                                           executable_path=configuration.basedir + "\\drivers\\chromedriver.exe")
            self.driver.implicitly_wait(10)
            self.driver.get(URL)
            self.principal = self.driver.window_handles[0]
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            self.nWindows = 0
            return self.driver

        if navegador == ("FIREFOX"):
            self.driver = webdriver.Firefox(executable_path=configuration.basedir + "\\drivers\\geckodriver.exe")
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get(URL)
            self.principal = self.driver.window_handles[0]
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            self.nWindows = 0
            return self.driver