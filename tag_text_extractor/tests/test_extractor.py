#! coding: utf-8
from tag_text_extractor import extract_tag_texts
from tag_text_extractor.tests import BaseTestCase
import unittest

class ExtractorTestCase(BaseTestCase):
    def test_extract(self):
        #TODO: добавить конкретных проверок
        html = self.get_data('example.html')
        data = extract_tag_texts(html)
        self.assertEquals(data.keys(), ['a', 'h2h6', 'text', 'title', 'metadescription', 'beis', 'h1', 'body'])

if __name__ == '__main__':
    unittest.main()
