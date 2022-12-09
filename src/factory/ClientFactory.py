

class ClientFactory:

  def createService(self, name: str):
    if (name=="local-storage"):
      return 1
    elif (name=="elastic-search"):
      return 2
    elif (name=="aws-s3"):
      return 3
    else:
      raise TypeError(f"There is no such client type: {name}")
    
