from src.scraper.DateParser import DateParser
from datetime import date
import unittest
from unittest import TestCase, mock

class DateParserTest(TestCase):

  dateParser=DateParser()
  
  def test_scraper_should_build_publication(self):
    
    
    with mock.patch.object(DateParser, 'get_doc', return_value="mock document text"):
      
      mock_cve="1954614"
      mock_header="mock_header"
      
      publication = DateParserTest.dateParser.build_publication(
        mock_cve,
        mock_header,
        "http://www.diariooficial.interior.gob.cl/publicaciones/2021/06/03/42969/05/1954614.pdf",
        "2021-06-03",
        {
          "title1": "Empresas y Cooperativas",
          "title2": "Sociedades Anónimas",
          "title3": "Administradora de Fondos de Inversión Nordsee Capital Management S.A.",
          "title4": "Title 4"
        }
      )
  
  def test_should_parse_signle_publication_text(self):
    mock_cve="1954614"
    mock_header="mock_header"
    
    with mock.patch.object(DateParser, 'get_doc', return_value="mock document text"):
      with open("./test/stubs/scraper/singlePublicationPageResponse.html", "r") as file:
        scraped_text = file.read()
        publications = list(DateParserTest.dateParser.parse(
          date(2021, 6, 3),
          scraped_text
        ))
        
        self.assertEqual(1, publications.__len__())
        first_publication = publications[0]
        
        self.assertEqual(first_publication.cve, mock_cve)
  




if __name__ == "__main__":
  unittest.main()