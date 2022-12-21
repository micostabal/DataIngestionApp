
from elasticsearch import Elasticsearch, helpers
import requests
from requests.auth import HTTPBasicAuth
from dotenv import dotenv_values
import time
config = dotenv_values(".env")


INDEX_NAME = 'example_index'
ES_PORT = 9200
ES_USER = "elastic"
ES_PASS = config["es_password"]
ES_CERT_PATH = "http_ca.crt"
PUBLICATION_REQUEST_BODY = {
  "settings": {"number_of_shards": 1},
  "mappings": {
    "properties": {
      "cve": { "type": "keyword" },
      "social_reason": { "type": "keyword" },
      "pdf_url": { "type": "keyword" },
      "publication_date": { "type": "date" },
      "principal_title": { "type": "keyword" },
      "section": { "type": "keyword" },
      "action_type": { "type": "keyword" },
      "document_text": { "type": "text" },
    }
  }
}


class ElasticSearchClient:
  
  def __init__(self, resetIfExists=False):
    self.base_url = f"https://localhost:{ES_PORT}"
    self.client = Elasticsearch(
      self.base_url,
      ca_certs=ES_CERT_PATH,
      basic_auth=(ES_USER, ES_PASS)
    )
    self.index_name = INDEX_NAME
    if self.index_name in self.client.indices.get(index="*") and resetIfExists:
      self.client.indices.delete(index=self.index_name)
      time.sleep(1)
    
    self.client.indices.create(
      index=INDEX_NAME,
      body=PUBLICATION_REQUEST_BODY,
      ignore=400
    )

  def bulk_insert(self, documentGenerator):
    for ok, action in helpers.streaming_bulk(
      client=self.client,
      index=self.index_name,
      actions=documentGenerator
    ):
      pass
  
  def get_head(self):
    return ElasticSearchManager.es_api_call(
      f"{self.base_url}/{INDEX_NAME}/_search"
    )

  def get_count(self):
    return ElasticSearchManager.es_api_call(
      f"{self.base_url}/{INDEX_NAME}/_count"
    )
  
  @staticmethod
  def es_api_call(url):
    return requests.get(
      url,
      auth= HTTPBasicAuth(ES_USER, ES_PASS),
      verify=ES_CERT_PATH
    )


if __name__ == "__main__":

  def gendata():
    mywords = ['foo', 'bar', 'baz']
    for i, word in enumerate(mywords):
      yield {
        "_id": i+1,
        "cve": "newCve",
        "social_reason": word,
        "pdf_url": "newPdfUrl",
        "publication_date": "2022-08-04",
        "principal_title": "newPrincipalTitle",
        "section": "newSection",
        "action_type": "newAction",
        "document_text": "newDocText"
      }
  
  esm = ElasticSearchClient()
  
  esm.bulk_insert(gendata())
  
  time.sleep(2)
  
  response = esm.get_count()
  
  print(response.content)


