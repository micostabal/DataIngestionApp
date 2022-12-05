from bs4 import BeautifulSoup
from Utils import download_file, get_text_from_pdf, remove_file, preprocess_string
from business import Publication
from typing import Dict
import re


class DateParser:

    def get_doc(self, url, cve):
        try:
            pdf_filename = "tmp/{}.pdf".format(cve)
            download_file(
                url,
                pdf_filename
            )
            documento_raw = get_text_from_pdf(pdf_filename)
            remove_file(pdf_filename)
            return documento_raw
        except:
            return None
    
    def build_publication(
            self,
            cve: str,
            date: str,
            header: str,
            pdf_url: str,
            titles: Dict):
        init_params = {
            'social_reason' : preprocess_string(header),
            'pdf_url' : pdf_url,
            'cve' : cve,
            'publication_date' : date,
            'principal_title' : titles['title1'],
            'section' : titles['title2'],
            'action_type' : titles['title3'],
            'document_text' : preprocess_string(self.get_doc(pdf_url, cve))
        }

        return Publication(**init_params)

    def parse(self, date, raw_html: str):
        dom_tree = BeautifulSoup(raw_html, "html.parser")
        titles = { f'title{i}' : None for i in range(1, 5) }
        for tr in dom_tree.findAll('tr'):
            tds = tr.findAll('td')
            if 'class' in tds[0].attrs.keys():
                titles[
                    tds[0]['class'][0]
                ] = tds[0].text.strip(' ')
                continue
            header = tds[0]\
                .text\
                .replace('\n', '')\
                .strip(' ')
            pdf_url = tds[1].a['href']
            cve = re.match(r'.+\/(?P<cve>[0-9]+).pdf', pdf_url).group('cve')
            
            yield self.build_publication(
                cve, date, header, pdf_url, titles
            )

if __name__ == "__main__" : pass