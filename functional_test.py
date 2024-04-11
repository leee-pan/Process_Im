from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.common.by import By

class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME,'h1').text
        self.assertIn('To-Do',header_text)

        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
        )

        inputbox.send_keys('Buy flowers')
        inputbox.send_keys(Keys.Enter)
        time.sleep(1)

        table = self.browser.find_element(By.ID,'id_list_table')
        self.assertIn('1:Buy flowerse', [row.text for row in rows])

        self.fail('Finish the test!')

if __name__== '__main__':
    unittest.main()