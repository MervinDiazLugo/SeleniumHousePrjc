# -*- coding: utf-8 -*-
import unittest
from functions.functions import Selenium
from selenium.webdriver.common.keys import Keys
import time

class tst_001(unittest.TestCase, Selenium):

    def setUp(self):

        Selenium.open_browser(self)

    def test_something(self):
        URL = "https://alt-torrent.com/"
        self.driver.execute_script(f'''window.open("{URL}","_blank");''')
        Selenium.ventanas["altTorrens"] = self.driver.window_handles[1]
        print(Selenium.ventanas)

        self.driver.switch_to.window(Selenium.ventanas["Principal"])
        print("ESTAS EN VENTANA PRINCIPAL")
        print(Selenium.ventanas)

        self.driver.switch_to.window(Selenium.ventanas["altTorrens"])
        print("ESTAS EN VENTANA ALTORRENTS")

        URL = "https://news.google.com/topstories?hl=es-419&gl=AR&ceid=AR:es-419"
        self.driver.execute_script(f'''window.open("{URL}","_blank");''')
        Selenium.ventanas["noticias"] = self.driver.window_handles[2]
        print(Selenium.ventanas)

        self.driver.switch_to.window(Selenium.ventanas["noticias"])
        print("ESTAS EN VENTANA NOTICIAS")
        time.sleep(10)

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main()
