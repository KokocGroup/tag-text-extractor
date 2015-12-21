#! coding: utf-8
import unittest

from tag_text_extractor import extract_tag_texts, extract
from tag_text_extractor.tests import BaseTestCase


class ExtractorTestCase(BaseTestCase):
    def test_extract(self):
        html = self.get_data('example.html')
        data = extract_tag_texts(html)
        self.assertListEqual(data.keys(), ['a', 'body', 'title', 'text', 'h1', 'h2h6', 'beis', 'metadescription'])
        self.assertEquals(data['a']['word_count'], 179)
        self.assertEquals(data['h2h6']['word_count'], 6)
        self.assertEquals(data['text']['word_count'], 267)
        self.assertEquals(data['title']['word_count'], 8)
        self.assertEquals(data['metadescription']['word_count'], 0)
        self.assertEquals(data['beis']['word_count'], 85)
        self.assertEquals(data['h1']['word_count'], 0)
        self.assertEquals(data['body']['word_count'], 537)

    def test_small_example(self):
        html = "<html><head><meta content='...' /></head><body><p>Узнать о нашем магазине выможете из <a href='test'>нашей брошюры</a> а так же нашего сайта<p></body></html>"

        data = extract_tag_texts(html)
        self.assertEquals(data['a']['word_count'], 1)
        self.assertListEqual(data['a']['texts'], [u'нашей брошюры'])
        self.assertEquals(data['metadescription']['word_count'], 0)
        self.assertListEqual(data['metadescription']['texts'], [])
        self.assertEquals(data['body']['word_count'], 5)
        self.assertListEqual(data['body']['texts'],
                             [u'Узнать о нашем магазине выможете из',
                              u'нашей брошюры',
                              u'а так же нашего сайта'])

    def test_new_extractor(self):
        data = extract("<html><body><p>Узнать о нашем магазине вы можете из <a href='test'>нашей брошюры</a> а так же нашего сайта<p></body></html>")

        self.assertEquals(data['a']['word_count'], 2)
        self.assertListEqual(data['a']['texts'], [u'нашей брошюры'])
        self.assertEquals(data['text_fragment']['word_count'], 14)
        self.assertListEqual(data['text_fragment']['texts'],
                             [u'Узнать о нашем магазине вы можете из нашей брошюры а так же нашего сайта'])

        data = extract("<html><body><p>Узнать о нашем магазине вы можете из нашей брошюры а так же нашего сайта Узнать о нашем магазине вы можете из нашей брошюры а так же нашего сайта Узнать о нашем магазине вы можете из нашей брошюры а так же нашего сайта Узнать о нашем магазине вы можете из нашей брошюры а так же нашего сайта Узнать о нашем магазине вы можете из нашей брошюры а так же нашего сайта Узнать о нашем магазине вы можете из нашей брошюры а так же нашего сайта<p></body></html>")
        self.assertEqual(data['plain_text']['word_count'], 84)
        self.assertNotIn('text_fragment', data)

if __name__ == '__main__':
    unittest.main()
