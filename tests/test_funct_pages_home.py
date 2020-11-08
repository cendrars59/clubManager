import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('window-size=1920x1080')


class TestHomePage(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Chrome(
            executable_path='/mnt/c/webdrivers/chromedriver.exe',
            options=chrome_options,
        )
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.driver.quit()

    def test_verify_elements_in_home(self):
        self.driver.get(self.live_server_url)
        time.sleep(5)
        # user opens the page and sees header section
        # verify that logo is loaded
        logo = self.driver.find_element_by_id("logo")
        source = logo.get_attribute("src")
        self.assertEqual(
            source,
            self.live_server_url
            + '/static/dist/assets/img/logo/logo.svg',
        )
        # verify page H1 title
        title = self.driver.find_element_by_id("home-title").text
        self.assertEqual(title, 'PROCHAINES SCÉANCES')

    def test_redirection_to_logout(self):
        mentions_url = self.live_server_url + reverse("logout")
        self.driver.get(self.live_server_url)
        time.sleep(5)
        self.driver.find_element_by_id("selections-logout").click()
        self.assertEqual(self.driver.current_url, mentions_url)
        time.sleep(5)

    def test_redirection_to_mentions(self):
        mentions_url = self.live_server_url + reverse("mentions")
        self.driver.get(self.live_server_url)
        time.sleep(5)
        self.driver.find_element_by_id("legal-link").click()
        self.assertEqual(self.driver.current_url, mentions_url)
        time.sleep(5)

    def test_redirection_to_official(self):
        official = "https://www.rugby-tourcoing.com/"
        self.driver.get(self.live_server_url)
        time.sleep(5)
        self.driver.find_element_by_id("official-link").click()
        self.assertEqual(self.driver.current_url, official)
        time.sleep(5)
