# -*- coding: utf-8 -*-
import unittest

from functions.functions import Selenium as Selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure
import pytest

@allure.feature(u'Excels')
@allure.story(u'005: Read-Write Excels')
@allure.testcase(u"Caso de Prueba 00005", u'http://my.tms.org/browse/TESTCASE-39')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Read-Write Excels</br>""")

class tst_005(unittest.TestCase, Selenium):
    def setUp(self):
        #ABRIR LA APP
        with allure.step(u'PASO 1: Data desde Excel'):
            self.driver = Selenium.open_browser(self, URL = 'https://www.tripadvisor.com.ar/Attractions-g34439-Activities-Miami_Beach_Florida.html')
            self.email = Selenium.leer_celda(self, 'C2')
            self.text = Selenium.leer_celda(self, 'A1', 'test2')
            #Selenium.escribir_celda(self, 'A2', self.email, 'test2')

    def test_02(self):
        with allure.step(u'PASO 2: Extraer desde Trivago'):
            Listado = self.driver.find_elements(By.XPATH, "//span[contains(@class, '_2e_OvRJN')]")
            n = 2
            for item in Listado:
                posicion = "A" + str(n)
                Selenium.escribir_celda(self, posicion, item.text, 'test2')
                n += 1


    def tearDown(self):
        with allure.step(u'PASO 3: Salir de la aplicación.'):
            pass


if __name__ == "__main__":
    unittest.main()