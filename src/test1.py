import unittest
from functions.functions import Selenium

class MyTestCase(unittest.TestCase, Selenium):
    def test_something(self):
        self.open_browser()

    def test_something(self):
        self.open_browser("https://www.toolsqa.com/cucumber/behavior-driven-development/")



if __name__ == '__main__':
    unittest.main()
