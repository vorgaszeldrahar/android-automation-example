#
# Simple POC for automated testing of the Android Tasks POC App
#
# Author:    btweed
# Date:      8/10/2016
# Reference: https://github.com/appium/sample-code/blob/master/sample-code/examples/python/android_simple.py
#
import os
import unittest
import yaml

from appium import webdriver

from pages import LoginPage, MyTasksPage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class ConfigLoader(object):

    def __init__(self):
        file = open('config.yaml')
        yaml_dict = yaml.load(file)
        self.credentials = yaml_dict['valid_user_creds']
        self.app_path = yaml_dict['app_path']

    def get_credentials(self):
        return self.credentials

    def get_app_path(self):
        return self.app_path


class AndroidTasksTest(unittest.TestCase):
    """ This is the base class from which all other tests inherit """
    def setUp(self):
        super(AndroidTasksTest, self).setUp()
        config_loader = ConfigLoader()
        app_path = config_loader.get_app_path()

        desired_capabilities = {'platformName': 'Android', 'platformVersion': '6', 'deviceName': 'Android Emulator',
                                'app': PATH(app_path)}

        grid_url = 'http://localhost:4723/wd/hub'
        self.driver = webdriver.Remote(grid_url, desired_capabilities)
        self.credentials = config_loader.get_credentials()

    def tearDown(self):
        super(AndroidTasksTest, self).tearDown()
        self.driver.quit()


class LoginTest(AndroidTasksTest):

    def testLogin(self):
        """
        This test checks login and logout functionality.
        Steps:
        1. Login using a valid email/password combination
        2. Land on the 'My Tasks' page.
        3. Open the menu in the upper left-hand corner
        4. Tap the 'Sign out' link
        5. Land on the login page
        """
        login_page = LoginPage(self.driver)
        login_page.set_email(self.credentials['email'])
        login_page.set_password(self.credentials['password'])
        login_page.click_login_button()

        my_tasks_page = MyTasksPage(self.driver)

        # Wait to arrive on the 'My Tasks' page
        my_tasks_page.wait_for_it()

        # Confirm login was successful
        self.assertTrue('My Tasks' in self.driver.page_source)

        # Now sign out
        my_tasks_page.tap_menu_button()
        my_tasks_page.sign_out()

        # Confirm you are taken back to the login page
        login_page.wait_for_it()

    @unittest.skip('Need to figure out how to capture the error that pops up')
    def testFailedLogin(self):
        login_page = LoginPage(self.driver)
        login_page.set_email('frankherbert@arrakis.gov')
        login_page.set_password('password')
        login_page.click_login_button()

        # TODO: Confirm that a failed login attempt gives us some sort of useful message


class MyTasksTests(AndroidTasksTest):

    def log_me_in(self):
        """ Convenience method to make sure the user is logged in and on the My Tasks page """
        login_page = LoginPage(self.driver)
        login_page.set_email(self.credentials['email'])
        login_page.set_password(self.credentials['password'])
        login_page.click_login_button()

        my_tasks_page = MyTasksPage(self.driver)
        my_tasks_page.wait_for_it()

    def test_create_unlabeled_task(self):
        my_tasks_page = MyTasksPage(self.driver)
        my_tasks_page.create_task_for_label('Do a thing', None)
        pass

    def test_create_labeled_task(self):
        pass

    def test_create_label(self):
        pass

    def test_mark_task_completed(self):
        pass

    def test_delete_label(self):
        pass

    def test_click_on_task(self):
        pass

    def test_sort_by_due_date(self):
        pass

    def test_sort_by_label(self):
        pass

    def test_search_for_task(self):
        pass

    def test_view_completed(self):
        pass

    def test_view_delegated(self):
        pass

    def test_view_my_tasks(self):
        pass

    def test_sign_out(self):
        pass

if __name__ == '__main__':
    """ Just runs the one testcase (for now) """
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    unittest.TextTestRunner(verbosity=2).run(suite)





