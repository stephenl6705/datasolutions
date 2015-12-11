from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
#from unittest import skip

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(1)

    def tearDown(self):
        self.browser.quit()

    def test_can_go_to_home_page(self):
        # Nic has heard about a cool data solutions app. She goes
        # to check out its homepage
        self.browser.get('http://langestrst01.pythonanywhere.com/')

        # She notices the page title and the header mention Data-Solutions
        self.assertIn('Data-Solutions',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Data-Solutions',header_text)

        # She sees links to a list of topics including CCI Dashboard.
        topics = self.browser.find_element_by_id('topics')
        topic_list = topics.find_elements_by_tag_name('input')
        self.assertTrue(
            any(topic.get_attribute('value') == 'CCI Dashboard' for topic in topic_list),
            "CCI Dashboard did not appear in the list of topics")

        # She clicks on the CCI Dashboard and she finds it shows a new summary
        topic = topics.find_element_by_id("id_topic1")
        topic.click()
        summary = self.browser.find_element_by_id("id_summary")
        title = summary.find_element_by_tag_name("h2")
        self.assertEqual(
            title.text,"CCI Dashboard",
            "CCI Dashboard did not appear in the summary -- its text was:\n%s" % (title.text,)
        )

        # She clicks on the CCI Suite button and she finds it shows a new summary again
        topics = self.browser.find_element_by_id('topics')
        topic = topics.find_element_by_id("id_topic2")
        topic.click()
        summary = self.browser.find_element_by_id("id_summary")
        title = summary.find_element_by_tag_name("h2")
        self.assertEqual(
            title.text,"CCI C-Suite",
            "CCI C-Suite did not appear in the summary -- its text was:\n%s" % (title.text,)
        )

        # She selects the "CCI Dashboard topic" and finds a summary on the consumer confidence index
        topics = self.browser.find_element_by_id('topics')
        topic = topics.find_element_by_id("id_topic1")
        topic.click()
        text = self.browser.find_element_by_tag_name("p").text
        self.assertIn("CCI Dashboard",text,"CCI Dashboard has no summary")

        # and it opens up to the Nielsen Global Survey page
        # She notices the page title and the header mention Nielsen Global Survey
        # She sees a table with Nielsen Global Survey 2015 as a row
        # She is interested in the other links on the home page and clicks on the link to go back to home page
        #self.source_in_list_and_has_webpage('Nielsen Global Survey','id_sources_ngs')

        # She goes through the same process for "Trading Economics"
        #self.source_in_list_and_has_webpage('Trading Economics','id_sources_ti')

        # And through the same process for the Worldbank
        #self.source_in_list_and_has_webpage('World Bank','id_sources_wb')

        # She has a list of options such as to download the entire file,
        # but it also has a set of filter boxes if she doesn't want everything

        # First she clicks on the download button and a download box opens

        # She checks the right location is selected for the download
        # She then clicks ok and the file downloads to her chosen location

        # She then realizes the file is too big, she really wants to look at 2015 only
        # She then goes to the year filter box and selects 2015
        # She downloads again and the filtered file downloads to her chosen location


if __name__ == '__main__':
    unittest.main(warnings='ignore')
