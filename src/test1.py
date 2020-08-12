# -*- coding: utf-8 -*-
import unittest
from functions.functions import Selenium
from selenium.webdriver.common.keys import Keys
import time

class tst_001(unittest.TestCase, Selenium):

    def setUp(self):
       Selenium.open_browser(self)

    def test_something(self):
        Selenium.openJson(self, "spotify")
        Selenium.get_elements(self, "email").clear()
        Selenium.get_elements(self, "email").send_keys("mervindiazlugo@gmail.com")
        Selenium.get_elements(self, "email").send_keys(Keys.TAB)
        #time.sleep(3)
        Selenium.waitElement(self, "email error")
        mensaje = Selenium.get_elements(self, "email error").text
        assert "Este correo electrónico ya está conectado a una cuenta" in mensaje, f"El mensaje no coincide :  {mensaje}"

    def test_something2(self):
        Selenium.openJson(self, "spotify")
        Selenium.get_elements(self, "email").clear()
        Selenium.get_elements(self, "email").send_keys("mervindiazlugo2222@gmail.com")
        Selenium.get_elements(self, "email").send_keys(Keys.TAB)
        isPresent = Selenium.isPresent(self, "email error")

        assert isPresent == False, "isPresent: el objeto no esta presente"

    def test_something3(self):
        Selenium.screenshot(self)
        time.sleep(1)
        Selenium.screenshot(self)



    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main()
