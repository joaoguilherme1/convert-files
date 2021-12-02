from selenium.webdriver import firefox
from selenium.webdriver.firefox import options
import pytest
import os
import time
from django.test import LiveServerTestCase
from selenium import webdriver

class TestBrowser1(LiveServerTestCase):
    def test_admin_browser_open(self):
        driver = webdriver.Firefox()
        driver.get(('%s%s' % (self.live_server_url, '/admin/')))
        assert 'Acessar | Site de administração do Django' in driver.title
        driver.close()

class TestBrowser2(LiveServerTestCase):
    def test_admin_browser_headless(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
        driver.get(('%s%s' % (self.live_server_url, '/admin/')))
        assert 'Acessar | Site de administração do Django' in driver.title
        driver.close()

def take_screenshot(driver, name):
    time.sleep(1)
    os.makedirs(os.path.join('screenshots', os.path.dirname(name)), exist_ok=True)
    driver.save_screenshot(os.path.join('screenshots', name))

def test_admin_screenshot(live_server):
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    firefox_driver = webdriver.Firefox(options=options)
    firefox_driver.get(('%s%s' % (live_server.url, '/admin/')))
    take_screenshot(firefox_driver, 'admin.png')

def test_home_screenshot(live_server):
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    firefox_driver = webdriver.Firefox(options=options)
    firefox_driver.get(('%s%s' % (live_server.url, '/')))
    take_screenshot(firefox_driver, 'home.png')