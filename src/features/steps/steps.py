
from functions.functions import Selenium
from behave import *


class stepsDefinitions():

    @given('I go to main site app')
    def step_impl(self):
        Selenium.open_browser(self)

    @given("I open the app in (.*)")
    def step_impl(self, url):
        Selenium.open_browser(self, url)

    @step("I open with (.*) the app (.*)")
    def step_impl(self, navegador, URL):
        Selenium.open_browser(self, URL, navegador)

    @step("close all windows")
    def step_impl(self):
        self.driver.quit()