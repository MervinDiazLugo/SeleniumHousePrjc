# -*- coding: utf-8 -*-
from functions.functions import Selenium
from selenium.webdriver.common.keys import Keys
from behave import *

class stepsDefinitions():
    use_step_matcher("re")

    @given('I go to main site app')
    def step_impl(self):
        self.driver = Selenium.open_browser(self)
        Selenium.page_has_loaded(self)

    @given("I open the app in (.*)")
    def step_impl(self, url):
        self.driver = Selenium.open_browser(self, url)
        Selenium.page_has_loaded(self)

    @step("I open with (.*) the app (.*)")
    def step_impl(self, navegador, URL):
        self.driver = Selenium.open_browser(self, URL, navegador)
        Selenium.page_has_loaded(self)

    @step("close all windows")
    def step_impl(self):
        self.driver.quit()

    @step("I set (.*) as DOM")
    def step_impl(self, dom):
        Selenium.openJson(self, dom)

    @step("I click in element (.*)")
    def step_impl(self, element):
        Selenium.get_elements(self, element).click()

    @step("I set (.*) in element (.*)")
    def step_impl(self, text, element):
        Selenium.get_elements(self, element).clear()
        if text == 'TAB':
            Selenium.get_elements(self, element).send_keys(Keys.TAB)
        elif text == 'ENTER':
            Selenium.get_elements(self, element).send_keys(Keys.ENTER)
        else:
            textContext = Selenium.ReplaceWithContextValues(self, text)
            Selenium.get_elements(self, element).send_keys(textContext)

    @step("I set (.*) in dropdown (.*)")
    def step_impl(self, text, element):
        select = Selenium.select_elements(self, element)
        select.select_by_visible_text(text)

    @step("set by index (.*) in dropdown (.*)")
    def step_impl(self, index, element):
        select = Selenium.select_elements(self, element)
        select.select_by_index(index)

    @step("wait (.*) seconds")
    def step_impl(self, time):
        Selenium.wait(self, time)

    @then("Wait element (.*)")
    def step_impl(self, element):
        Selenium.waitElement(self, element)


    @step("Assert (.*) is equal to element (.*)")
    def step_impl(self, text, element):
        message = Selenium.get_elements(self, element).text
        context = Selenium.ReplaceWithContextValues(self, text)
        assert context in message, f"El mensaje no coincide :  {message}"

    @then("Validate if this (.*) is present")
    def step_impl(self, element):
        isPresent = Selenium.isPresent(self, element)
        assert isPresent, f"isPresent: el {element} no esta presente"

    @then("Validate if this (.*) is not present")
    def step_impl(self, element):
        isPresent = Selenium.isPresent(self, element)
        assert isPresent == False, f"isPresent: el {element} no esta presente"

    @step("scroll to element (.*)")
    def step_impl(self, element):
        Selenium.scrollIntoView(self, element)

    @step("click in element (.*) with JS")
    def step_impl(self, element):
        Selenium.clickWithJs(self, element)


    @then("Take a ScreenShot: (.*)")
    def step_impl(self, descripcion):
        Selenium.screenshot(self, descripcion)

    @then("Take allure ScreenShot: (.*)")
    def step_impl(self, descripcion):
        Selenium.allureScreenshot(self, descripcion)


    @step("I switch to Frame: (.*)")
    def step_impl(self, element):
        frame  = Selenium.get_elements(self, element)
        self.driver.switch_to.frame(frame)

    @step("I switch to parent frame")
    def step_impl(self):
        self.driver.switch_to.parent_frame()


    @step("Accept alert present")
    def step_impl(self):
        Selenium.alert_windows(self)


    @given("I open new tab in: (.*)")
    def step_impl(self, url):
        self.driver.execute_script(f'''window.open("{url}","_blank");''')
        print("Estas en : " + self.driver.current_url)


    @step("I go to (.*) tab")
    def step_impl(self, ventana):
        Selenium.switch_to_windows_name(self, ventana)

    @step("I move to (.*)  with actionChains")
    def step_impl(self, element):
        Selenium.actionChainsMove(self, element)\

    @step("I click in (.*) with actionChains")
    def step_impl(self, element):
        Selenium.actionChainsClick(self, element)


    @given("Read data from cell (.*)")
    def step_impl(self, cell):
        Selenium.scenario[cell] = Selenium.leer_celda(self, cell)
        print(Selenium.scenario[cell])

    @given("Read cell (.*) from sheet (.*)")
    def step_impl(self, cell, sheet):
        Selenium.scenario[cell] = Selenium.leer_celda(self, celda = cell, wSheet=sheet)
        print (Selenium.scenario[cell])


    @step("get text in element (.*) and save in scenario context")
    def step_impl(self, element):
        Selenium.scenario[element] = Selenium.get_elements(self, element).text
        print(Selenium.scenario[element])
        print(Selenium.scenario)

