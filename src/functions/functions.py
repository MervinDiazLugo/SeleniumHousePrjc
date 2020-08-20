# -*- coding: utf-8 -*-
import allure
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException, NoSuchWindowException, UnexpectedAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options as OpcionesChrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import re
import os

from functions.conf import configuration
import pytest
import json
import time
horaGlobal = time.strftime("%H%M%S")  # formato 24 houras


class Selenium:
    ventanas = {}
    ##########################################################################
    ##############   -=_INICIALIZAR DRIVERS_=-   #############################
    ##########################################################################
    def open_browser(self, URL=configuration.URL, navegador=configuration.browser):
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
            Selenium.ventanas = {'Principal': self.driver.window_handles[0]}

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
            Selenium.ventanas = {'Principal': self.driver.window_handles[0]}
            self.nWindows = 0
            return self.driver

        if navegador == ("FIREFOX"):
            self.driver = webdriver.Firefox(executable_path=configuration.basedir + "\\drivers\\geckodriver.exe")
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get(URL)
            self.principal = self.driver.window_handles[0]
            Selenium.ventanas = {'Principal': self.driver.window_handles[0]}
            self.nWindows = 0
            return self.driver


    def openJson(self, file):
        json_path = configuration.Json + "\\" + file + '.json'
        try:
            with open(json_path, encoding='utf-8') as read_file:
                self.json_strings = json.loads(read_file.read())
                print ("openJson: "+ json_path)
                return self.json_strings
        except FileNotFoundError:
            self.json_strings = False
            pytest.skip(u"get_json_file: No se encontro el Archivo " + json_path)

    def get_entity(self, entity):
        try:
            self.json_ValueToFind = self.json_strings[entity]["ValueToFind"]
            self.json_GetFieldBy = self.json_strings[entity]["GetFieldBy"]
            return True

        except KeyError:
            self.msj = u"get_entity: No se encontro la key a la cual se hace referencia: " + entity
            #Functions.tearDown(self, "fail")
            pytest.skip(self.msj)
            #self.driver.close()

        except AttributeError:
            self.msj = u"get_entity: Debes ejecutar openJson para establecer un valor en  json_strings"
            pytest.skip(self.msj)


    def webElement(self, entity):
        Selenium.get_entity(self, entity)

        if self.json_GetFieldBy.lower() == "id":
            element =(By.ID, self.json_ValueToFind)

        if self.json_GetFieldBy.lower() == "name":
            element = (By.NAME, self.json_ValueToFind)

        if self.json_GetFieldBy.lower() == "xpath":
            element = (By.XPATH, self.json_ValueToFind)

        if self.json_GetFieldBy.lower() == "link":
            element = (By.PARTIAL_LINK_TEXT, self.json_ValueToFind)

        if self.json_GetFieldBy.lower() == "css":
            element = self.driver.find_element(By.CSS_SELECTOR, self.json_ValueToFind)

        if self.json_GetFieldBy.lower() == "class":
            element = (By.CLASS_NAME, self.json_ValueToFind)

        print("get_elements: " + self.json_ValueToFind)
        return element

    def get_elements(self, entity, MyTextElement=None):
        Selenium.get_entity(self, entity)
        try:
            if self.json_GetFieldBy.lower() == "id":
                elements = self.driver.find_element(By.ID, self.json_ValueToFind)
                print(elements)

            if self.json_GetFieldBy.lower() == "name":
                elements = self.driver.find_element(By.NAME, self.json_ValueToFind)
                print(elements)

            if self.json_GetFieldBy.lower() == "xpath":
                if MyTextElement is not None:
                    self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                    print(self.json_ValueToFind)
                elements = self.driver.find_element(By.XPATH, self.json_ValueToFind)
                print(elements)

            if self.json_GetFieldBy.lower() == "link":
                elements = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind)

            if self.json_GetFieldBy.lower() == "css":
                elements = self.driver.find_element(By.CSS_SELECTOR, self.json_ValueToFind)
                print(elements)

            if self.json_GetFieldBy.lower() == "class":
                elements = self.driver.find_element(By.CLASS_NAME, self.json_ValueToFind)
                print(elements)

            print("get_elements: " + self.json_ValueToFind)
            return elements

        except NoSuchElementException:
            self.msj = ("get_elements NoSuchElementException: No se encontró el elemento: " + self.json_ValueToFind)
            #Functions.tearDown(self, "fail")
        except TimeoutException:
            self.msj = ("get_elements TimeoutException: No se encontró el elemento: " + self.json_ValueToFind)
            #Functions.tearDown(self, "fail")


    def select_elements(self, locator):
        element = Selenium.get_elements(self, locator)
        select = Select(element)
        return select

    def wait(self, seconds=8):
        time.sleep(int(seconds))

    def tearDown(self):
        self.driver.quit()

    def waitElement(self, entity):
        wait = WebDriverWait(self.driver, 30)
        element = Selenium.webElement(self, entity)
        wait.until(EC.visibility_of_element_located(element))
        wait.until(EC.element_to_be_clickable(element))

    def isPresent(self, entity):
        wait = WebDriverWait(self.driver, 30)
        element = Selenium.webElement(self, entity)
        try:
            wait.until(EC.visibility_of_element_located(element))
            wait.until(EC.element_to_be_clickable(element))
            return True
        except NoSuchElementException:
            print(f"Element {entity} is not present")
            return False
        except TimeoutException:
            print(f"Element {entity} is not present")
            return False

    def scrollIntoView(self, elements):
        element  = Selenium.get_elements(self, elements)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        print(f"... scrolling to {elements}")

    def clickWithJs(self, elements):
        element = Selenium.get_elements(self, elements)
        self.driver.execute_script("arguments[0].click(); ", element)
        print(f"... click in {elements}")

##############   -=_CAPTURA DE PANTALLA_=-   #############################
    ##########################################################################
    def create_path(self, descripcion='cucumber'):
        dia = time.strftime("%d-%m-%Y")  # formato aaaa/mm/dd

        GeneralPath = configuration.path_evidencias
        BrowserTest = configuration.browser
        self.TestCase = self.__class__.__name__
        horaAct = horaGlobal
        x = re.search("Context", self.TestCase) #True
        if (x):
            path = GeneralPath + "/" + dia + "/" + descripcion + "/" + BrowserTest + "/" + horaAct + "/"
        else:
            path = GeneralPath + "/" + dia + "/" + self.TestCase + "/" + BrowserTest + "/" + horaAct + "/"

        if not os.path.exists(path):  # si no existe el directorio lo crea
            os.makedirs(path)

        print(path)
        return path


    def screenshot(self, descripcion='cucumber'):
        def hora_Actual():
            hora = time.strftime("%H%M%S")  # formato 24 horas
            return hora
        path = Selenium.create_path(self, descripcion)
        x = re.search("Context", self.TestCase)  # False

        if (x):
            img = f'{path}{descripcion}_(' + str(hora_Actual()) + ')' + '.png'
        else:
            img = f'{path}{self.TestCase}_(' + str(hora_Actual()) + ')' + '.png'

        try:
            self.driver.get_screenshot_as_file(img)
            print(img)
            return img
        except UnexpectedAlertPresentException:
            pass

    def allureScreenshot(self, descripcion):
        allure.attach(self.driver.get_screenshot_as_png(), descripcion, attachment_type=allure.attachment_type.PNG)


    def alert_windows(self, accept="accept", time = 8):
        try:
            wait = WebDriverWait(self.driver, time)
            wait.until(EC.alert_is_present(), print(f"Esperando alerta {time} seg."))
            alert = self.driver.switch_to.alert

            if accept.lower()== "accept":
                alert.accept()
                print(alert.text)
                print ("Click in Accept")
            else:
                alert.dismiss()
                print ("Click in Dismiss")

        except NoAlertPresentException:
            print('Alerta no presente')
            pass
        except NoSuchWindowException:
            print('Alerta no presente')
            pass
        except TimeoutException:
            print('Alerta no presente')
            pass

    def page_has_loaded(self):
        print("Checking if {} page is loaded.".format(self.driver.current_url))
        page_state = self.driver.execute_script('return document.readyState;')
        #while (page_state != 'complete'):
            #print("Checking if {} page is loaded.".format(self.driver.current_url))
            #page_state = self.driver.execute_script('return document.readyState;')
            #break;
        yield
        WebDriverWait(self.driver, 10).until(lambda driver: page_state == 'complete')
        assert page_state == 'complete', "No se completo la carga"
        print("site {} is loaded".format(self.driver.current_url))


    def switch_to_windows_name(self, ventana):
        if ventana in Selenium.ventanas:
            Selenium.wait(self, 5)
            self.driver.switch_to.window(Selenium.ventanas[ventana])
            Selenium.page_has_loaded(self)
            print ("volviendo a " + ventana + " : " + Selenium.ventanas[ventana])
        else:
            try:
                Selenium.wait(self)
                wtime = 0
                self.nWindows = len(self.driver.window_handles) - 1
                EXIST = self.driver.window_handles[int(self.nWindows)] in Selenium.ventanas.values()
                while EXIST:
                    self.nWindows = 0
                    while (self.nWindows <= len(self.driver.window_handles)):
                        EXIST = self.driver.window_handles[int(self.nWindows)] in Selenium.ventanas.values()
                        if EXIST == False:
                            break
                        wtime = wtime + 1
                        self.nWindows = self.nWindows + 1
                        Selenium.wait(self, 1)

                        if wtime == 30:
                            break
                        continue
                if EXIST == False:
                    Selenium.ventanas[ventana] = self.driver.window_handles[int(self.nWindows)]
                print(Selenium.ventanas)
                self.driver.switch_to.window(Selenium.ventanas[ventana])
                Selenium.page_has_loaded(self)
                Selenium.alert_windows(self, "accept", 1)
                self.driver.maximize_window()
                print ("Estas en " + ventana + " : " + Selenium.ventanas[ventana])
                print(self.driver.current_url)
                #Selenium.is_not_404(self)

            except KeyError:
                self.msj = f"KeyError: La ventana: {ventana} no existe en {Selenium.ventanas}"
                Selenium.tearDown(self, "fail")
            except IndexError:
                self.msj = f"IndexError: No se encontro la ventana: {ventana}"
                print(self.msj)
                pass
                #Functions.tearDown(self, "fail")
            except NoSuchWindowException:
                self.msj = f"NoSuchWindowException: Error retrieving window"
                Selenium.tearDown(self, "fail")
            except UnexpectedAlertPresentException as e:
                self.msj = "switch_to_windows_name: " + str(e)
                Selenium.tearDown(self, "fail")

    def actionChainsMove(self, element):
        localizador = Selenium.get_elements(self, element)
        action = ActionChains(self.driver)
        action.move_to_element(localizador)
        action.perform()

    def actionChainsClick(self, element):
        localizador = Selenium.get_elements(self, element)
        action = ActionChains(self.driver)
        action.click(localizador)
        action.perform()

