import datetime
from dataclasses import dataclass

@dataclass
class Publication:
  cve: str
  social_reason: str
  pdf_url: str
  publication_date: datetime.date
  principal_title: str
  section: str
  action_type: str
  document_text: str

if __name__ == "__main__":
  pass