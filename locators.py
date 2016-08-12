# A locator is used to identify/address an element in the UI. This class is the place to reference all locators
# within the application.
# Locators in this source are grouped according to the page of the application, but we are not prohibited from embracing
# other organizational schemes if they fit our purposes.

from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    EMAIL_TEXTBOX = (By.ID, 'com.podio.tasks:id/emailText')
    PASSWORD_TEXTBOX = (By.ID, 'com.podio.tasks:id/passwordText')
    LOGIN_BUTTON = (By.ID, 'com.podio.tasks:id/loginButton')


class MyTasksPageLocators(object):
    # Title bar doesn't have a resource ID so I have to find it via XPATH
    MY_TASKS_TITLE = (By.XPATH,
                      '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.TextView[1]')
    # Menu button in the upper left corner
    MY_TASKS_MENU = (By.XPATH,
                     '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.ImageButton[1]')


class MyTasksMenuLocators(object):
    """ Locators for finding items in the MyTasks Pop-Up menu """
    # Each item in the menu has a resource-id of drawerRow
    # TODO: Kindly ask devs to provide unique resource-id for specific menu items like Sign Out
    MENU_ITEM = (By.ID, 'com.podio.tasks:id/drawerRow')
