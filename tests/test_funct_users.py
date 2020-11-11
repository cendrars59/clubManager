import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('window-size=1920x1080')


class TestRegisterPage(StaticLiveServerTestCase):

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

    def test_valid_registration(self):
        self.driver.get(self.live_server_url + reverse("register"))
        time.sleep(1)
        self.driver.find_element_by_name("username").send_keys("elvis")
        self.driver.find_element_by_name("email").send_keys(
            "elvis@isnotdead.com"
        )
        self.driver.find_element_by_name("password1").send_keys("Dickrivers76")
        self.driver.find_element_by_name("password2").send_keys("Dickrivers76")
        self.driver.find_element_by_id("btn-register").click()
        time.sleep(5)
        redirection_url = self.live_server_url + reverse("login")
        self.assertEqual(self.driver.current_url, redirection_url)

    def test_invalid_registration_missing_login(self):
        self.driver.get(self.live_server_url + reverse("register"))
        time.sleep(1)
        self.driver.find_element_by_name("email").send_keys(
            "jojo@labuvette.com"
        )
        self.driver.find_element_by_name("password1").send_keys("Dickrivers76")
        self.driver.find_element_by_name("password2").send_keys("Dickrivers76")
        self.driver.find_element_by_id("btn-register").click()
        time.sleep(5)
        self.assertEqual(
            self.driver.current_url, self.live_server_url + reverse("register")
        )

    def test_invalid_registration_missing_email(self):
        self.driver.get(self.live_server_url + reverse("register"))
        time.sleep(1)
        self.driver.find_element_by_name("username").send_keys("jojo")
        self.driver.find_element_by_name("password1").send_keys("Dickrivers76")
        self.driver.find_element_by_name("password2").send_keys("Dickrivers76")
        self.driver.find_element_by_id("btn-register").click()
        time.sleep(5)
        self.assertEqual(
            self.driver.current_url, self.live_server_url + reverse("register")
        )

    def test_invalid_registration_missing_pwd1(self):
        self.driver.get(self.live_server_url + reverse("register"))
        time.sleep(1)
        self.driver.find_element_by_name("username").send_keys("jojo")
        time.sleep(1)
        self.driver.find_element_by_name("email").send_keys(
            "jojo@labuvette.com"
        )
        time.sleep(1)
        self.driver.find_element_by_name("password2").send_keys("Dickrivers76")
        time.sleep(1)
        self.driver.find_element_by_id("btn-register").click()
        time.sleep(5)
        self.assertEqual(
            self.driver.current_url, self.live_server_url + reverse("register")
        )


class TestLoginPage(StaticLiveServerTestCase):

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

    def test_valid_login(self):
        self.driver.get(self.live_server_url + reverse("register"))
        time.sleep(1)
        self.driver.find_element_by_name("username").send_keys("bobby")
        time.sleep(1)
        self.driver.find_element_by_name("email").send_keys(
            "bobby@isnotdead.com"
        )
        time.sleep(1)
        self.driver.find_element_by_name("password1").send_keys("Dickrivers76")
        time.sleep(1)
        self.driver.find_element_by_name("password2").send_keys("Dickrivers76")
        time.sleep(1)
        self.driver.find_element_by_id("btn-register").click()
        time.sleep(5)
        redirection_url = self.live_server_url + reverse("login")
        self.assertEqual(self.driver.current_url, redirection_url)
        self.driver.find_element_by_name("username").send_keys("bobby")
        time.sleep(1)
        self.driver.find_element_by_name("password").send_keys("Dickrivers76")
        self.driver.find_element_by_id("btn-login").click()
        time.sleep(5)
        self.assertEqual(self.driver.current_url, self.live_server_url + '/')


class TestUserInformationPage(StaticLiveServerTestCase):

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

    def test_access_to_profile(self):
        self.driver.get(self.live_server_url + reverse("register"))
        time.sleep(1)
        self.driver.find_element_by_name("username").send_keys("robert")
        time.sleep(1)
        self.driver.find_element_by_name("email").send_keys(
            "robert@isnotdead.com"
        )
        time.sleep(1)
        self.driver.find_element_by_name("password1").send_keys("Dickrivers76")
        time.sleep(1)
        self.driver.find_element_by_name("password2").send_keys("Dickrivers76")
        time.sleep(1)
        self.driver.find_element_by_id("btn-register").click()
        time.sleep(5)
        redirection_url = self.live_server_url + reverse("login")
        self.assertEqual(self.driver.current_url, redirection_url)
        self.driver.find_element_by_name("username").send_keys("robert")
        time.sleep(1)
        self.driver.find_element_by_name("password").send_keys("Dickrivers76")
        self.driver.find_element_by_id("btn-login").click()
        time.sleep(5)
        self.driver.find_element_by_id("profile-link").click()
        time.sleep(5)
        redirection_url = self.live_server_url + reverse("profile")
        self.assertEqual(self.driver.current_url, redirection_url)
        first_name = self.driver.find_element_by_name("first_name").get_attribute('value')
        self.assertEqual(first_name, "")
        last_name = self.driver.find_element_by_name("last_name").get_attribute('value')
        self.assertEqual(last_name, "")
        email = self.driver.find_element_by_name("email").get_attribute('value')
        self.assertEqual(email, "robert@isnotdead.com")
        mobile_phone = self.driver.find_element_by_name("mobile_phone").get_attribute('value')
        self.assertEqual(mobile_phone, "")


class TestUserInformationUpdatePage(StaticLiveServerTestCase):

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

    def test_valid_user_products(self):
        self.driver.get(self.live_server_url + reverse("register"))
        time.sleep(1)
        # Register a new user
        self.driver.find_element_by_name("username").send_keys("brenda")
        self.driver.find_element_by_name("email").send_keys(
            "brendat@isnotdead.com"
        )
        self.driver.find_element_by_name("password1").send_keys("Dickrivers76")
        self.driver.find_element_by_name("password2").send_keys("Dickrivers76")
        self.driver.find_element_by_id("btn-register").click()
        time.sleep(5)
        # New user login
        redirection_url = self.live_server_url + reverse("login")
        self.assertEqual(self.driver.current_url, redirection_url)
        self.driver.find_element_by_name("username").send_keys("brenda")
        self.driver.find_element_by_name("password").send_keys("Dickrivers76")
        self.driver.find_element_by_id("btn-login").click()
        time.sleep(5)
        # New user modifying profile page
        self.driver.find_element_by_id("profile-link").click()
        time.sleep(5)
        redirection_url = self.live_server_url + reverse("profile")
        self.assertEqual(self.driver.current_url, redirection_url)
        # Inserting new data and save
        time.sleep(1)
        self.driver.find_element_by_name("first_name").clear()
        self.driver.find_element_by_name("first_name").send_keys("Jennyfer")
        self.driver.find_element_by_name("last_name").clear()
        self.driver.find_element_by_name("last_name").send_keys("Heart")
        self.driver.find_element_by_name("email").clear()
        self.driver.find_element_by_name("email").send_keys(
            "Jennyfer@isnotdead.com"
        )
        self.driver.find_element_by_name("mobile_phone").clear()
        self.driver.find_element_by_name("mobile_phone").send_keys(
            "0672331433"
        )
        self.driver.find_element_by_id("btn-register").click()
        time.sleep(1)
        first_name = self.driver.find_element_by_name("first_name").get_attribute('value')
        self.assertEqual(first_name, "Jennyfer")
        last_name = self.driver.find_element_by_name("last_name").get_attribute('value')
        self.assertEqual(last_name, "Heart")
        email = self.driver.find_element_by_name("email").get_attribute('value')
        self.assertEqual(email, "Jennyfer@isnotdead.com")
        mobile_phone = self.driver.find_element_by_name("mobile_phone").get_attribute('value')
        self.assertEqual(mobile_phone, "0672331433")
