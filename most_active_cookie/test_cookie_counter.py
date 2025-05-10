import unittest
from most_active_cookie.cookie_counter import get_most_active_cookies
import os

class TestCookieCounter(unittest.TestCase):

    def setUp(self):
        # creat CSV file (or ensure it's already there)
        self.test_file = "cookie_log.csv"
        
    def test_get_most_active_cookies_single(self):
        # one cookie is the most active
        file_path = self.test_file
        target_date = "2018-12-09"
        
        result = get_most_active_cookies(file_path, target_date)
        self.assertEqual(result, ['AtY0laUfhglK3lC7']) 

    def test_get_most_active_cookies_no_match(self):
        # test case where no cookies are found for our date
        file_path = self.test_file
        target_date = "2018-12-10"
        
        result = get_most_active_cookies(file_path, target_date)

        # empty result fo no cookies for this date 
        self.assertEqual(result, [])

    def test_get_most_active_cookies_invalid_timestamp(self):
        # test case for row with an invalid timestamp
        file_path = self.test_file
        target_date = "2018-12-09"
        
        result = get_most_active_cookies(file_path, target_date)
        self.assertEqual(result, ['AtY0laUfhglK3lC7'])

if __name__ == '__main__':
    unittest.main()
