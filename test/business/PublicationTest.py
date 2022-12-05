from src.business.Publication import Publication
import unittest
import datetime
from unittest import TestCase


class PublicationTest(TestCase):
  
  def test_can_create_publication_properly(self):
    initParams = {
      'social_reason' : '1234',
      'pdf_url' : 'http://google.com',
      'cve' : '12345678',
      'publication_date' : datetime.date.today(),
      'principal_title' : "title 1",
      'section' : "section here",
      'action_type' : "merge",
      'document_text' : 'huge text here'
    }
    
    newPublication = Publication(**initParams)

    self.assertEqual(newPublication.social_reason, "1234")
    self.assertEqual(newPublication.pdf_url, 'http://google.com')
    self.assertEqual(newPublication.cve, '12345678')
    self.assertEqual(newPublication.publication_date, datetime.date.today())
    self.assertEqual(newPublication.principal_title, "title 1")
    self.assertEqual(newPublication.section, "section here")
    self.assertEqual(newPublication.action_type, "merge")
    self.assertEqual(newPublication.document_text, 'huge text here')


if __name__ == "__main__":
  unittest.main()