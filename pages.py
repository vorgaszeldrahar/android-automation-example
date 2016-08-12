from locators import LoginPageLocators, MyTasksPageLocators, MyTasksMenuLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Page(object):
    """ Parent class for all pages, holds the reference to webdriver instance """

    def __init__(self, webdriver_reference):
        self.driver = webdriver_reference


class LoginPage(Page):
    """ Represents the app's login page, used to manipulate login inputs """

    SHORT_WAIT = 3

    def is_login_page(self):
        """ Returns true if the app is currently showing the login page, false otherwise """
        # TODO
        pass

    def set_email(self, email_to_set):
        assert email_to_set is not None
        email_textbox = self.driver.find_element(*LoginPageLocators.EMAIL_TEXTBOX)
        email_textbox.send_keys(email_to_set)

    def set_password(self, password_to_set):
        assert password_to_set is not None
        password_textbox = self.driver.find_element(*LoginPageLocators.PASSWORD_TEXTBOX)
        password_textbox.send_keys(password_to_set)

    def click_login_button(self):
        login_button = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

    def wait_for_it(self):
        """ Waits for the app to be on the initial login page """
        WebDriverWait(self.driver, self.SHORT_WAIT).until(
            ec.presence_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )


class MyTasksPage(Page):
    # wait 3 seconds
    SHORT_WAIT = 5

    def wait_for_it(self):
        """ wait for the My Tasks page to load """
        WebDriverWait(self.driver, self.SHORT_WAIT).until(
            ec.presence_of_element_located(MyTasksPageLocators.MY_TASKS_TITLE))

    def tap_menu_button(self):
        menu_button = self.driver.find_element(*MyTasksPageLocators.MY_TASKS_MENU)
        menu_button.click()

    def create_task_for_label(self, task_text, label_name=None):
        """
        Creates a new task from the MyTasks page for the specified label. If no label is provided task will be
        unlabeled
        """
        pass

    def sign_out(self):
        """ Log the user out of the application """
        # TODO: Put this into its own page object?
        all_menu_items = self.driver.find_elements(*MyTasksMenuLocators.MENU_ITEM)
        all_menu_items[len(all_menu_items)-1].click()


