import os
import unittest
from contextlib import contextmanager

from django.conf import settings
from django.test import LiveServerTestCase
from django.urls import ResolverMatch, resolve, reverse
from selenium.webdriver import Firefox, Remote
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.ui import WebDriverWait


@unittest.skipUnless(settings.SELENIUM is True or 'CI' in os.environ,
                     'Selenium test cases are only run in CI or if configured explicitly.')
class SeleniumTestCase(LiveServerTestCase):

    def setUp(self):
        if 'CI' in os.environ:
            self.driver = self.sauce_chrome_webdriver()
        elif settings.SELENIUM is True:
            options = FirefoxOptions()
            options.add_argument('-headless')
            self.driver = Firefox(firefox_options=options)
        self.driver.implicitly_wait(10)

    def sauce_chrome_webdriver(self):
        class_name = self.__class__.__name__
        method_name = self._testMethodName
        tunnel_id = os.environ.get("TRAVIS_JOB_NUMBER")
        capabilities = {
            'platform': "Mac OS X 10.9",
            'browserName': "chrome",
            'version': "31",
            'name': '{}.{}'.format(class_name, method_name),
            'tunnel-identifier': tunnel_id,
        }

        executor = "http://{}:{}@ondemand.saucelabs.com:80/wd/hub".format(
            os.environ["SAUCE_USERNAME"],
            os.environ["SAUCE_ACCESS_KEY"],
        )
        return Remote(
            command_executor=executor,
            desired_capabilities=capabilities,
        )

    def navigate(self, view_name: str):
        path = reverse(view_name)
        self.driver.get(self.live_server_url + path)

    def assert_view(self, view_name: str):
        path: str = self.driver.current_url.replace(self.live_server_url, '')
        resolved: ResolverMatch = resolve(path)
        self.assertEqual(resolved.view_name, view_name)

    @contextmanager
    def load(self, timeout=1):
        page = self.driver.find_element_by_tag_name('html')
        yield
        WebDriverWait(self.driver, timeout).until(
            staleness_of(page)
        )

    @contextmanager
    def wait(self, timeout=1):
        condition = _UrlHasChanged(self.driver.current_url)
        yield
        WebDriverWait(self.driver, timeout).until(condition)

    def tearDown(self):
        WebDriverWait(self.driver, 10)
        self.driver.quit()


class _UrlHasChanged(object):

    def __init__(self, url):
        self.old_url = url

    def __call__(self, driver):
        return driver.current_url != self.old_url