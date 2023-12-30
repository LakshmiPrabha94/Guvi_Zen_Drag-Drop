from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException

class Tester:
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    actions = ActionChains(driver)

    def __init__(self, url):       
        self.url = url

    def start(self):
        """Start the WebDriver, maximize the window, and navigate to the specified URL."""
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(30)

    def stop(self):
        """Quit the WebDriver."""
        self.driver.quit()

    def drag_drop(self):
        """Perform drag and drop operation on the specified elements."""
        try:
            # Switch to the frame containing the drag and drop elements
            self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, "demo-frame"))

            # Locate the draggable and droppable elements
            draggable_element = self.driver.find_element(By.ID, "draggable")
            droppable_element = self.driver.find_element(By.ID, "droppable")

            # Perform the drag and drop using ActionChains
            action_chains = ActionChains(self.driver)
            action_chains.drag_and_drop(draggable_element, droppable_element).perform()

            # Wait for a moment to see the result
            self.driver.implicitly_wait(1000)
            print("Drag andd drop action performed Successfully!!!")
            
        except NoSuchElementException as e:
            print("Error:", e)

        finally:
            self.stop()

if __name__ == '__main__':
    # Specify the URL
    test_url = "https://jqueryui.com/droppable/"

    # Create an instance of Tester
    tester_instance = Tester(test_url)

    # Start the test
    tester_instance.start()

    # Perform the drag and drop operation
    tester_instance.drag_drop()
