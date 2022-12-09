from business import Publication
from abc import ABC, abstractmethod


class DataClient(ABC):
  
  @abstractmethod
  def start(self) -> None: pass
  
  @abstractmethod
  def end(self) -> None: pass
  
  @abstractmethod
  def store_publication(self, publication: Publication) -> None: pass