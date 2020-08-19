# -*- coding: utf-8 -*-
import unittest

from functions.functions import Selenium as Selenium
from selenium.webdriver.common.keys import Keys
import allure
import pytest


@allure.feature(u'Busqueda Trivago')
@allure.story(u'002: verify query results for Bahia Blanca in Trivago')
@allure.testcase(u"Caso de Prueba 00001", u'http://my.tms.org/browse/TESTCASE-39')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""The PO gives us the following specification:</br>
We want to look for “RAET” word in google main page and check if amount of results is bigger than 100000  </br>

1- Access to https://www.trivago.com.ar/. </br>
2- Set Bahia Blanca in the Trivago textbox. </br>
3- Verify query results</br>
 </br></br>""")

class tst_002(unittest.TestCase, Selenium):

 
    def setUp(self):
        #ABRIR LA APP
        with allure.step(u'PASO 1: Ingresar a spotyfy register'):
            Selenium.open_browser(self)

    def test_02(self):
        #ESPERAR EL INICIO DE LA APP
        with allure.step(u'PASO 2: Ingresar un correo ya utilizado'):
            Selenium.openJson(self, "spotify")
            Selenium.get_elements(self, "email").clear()
            Selenium.get_elements(self, "email").send_keys("mervindiazlugo@gmail.com")
            Selenium.get_elements(self, "email").send_keys(Keys.TAB)
            Selenium.waitElement(self, "email error")
            mensaje = Selenium.get_elements(self, "email error").text
            assert "Este correo electrónico ya está conectado a una cuenta" in mensaje, f"El mensaje no coincide :  {mensaje}"
            Selenium.allureScreenshot(self, "Whats uuuuuuupppppp")

    def tearDown(self):
        with allure.step(u'PASO 3: Salir de la aplicación.'):
            Selenium.tearDown(self)


if __name__ == "__main__":
    unittest.main()