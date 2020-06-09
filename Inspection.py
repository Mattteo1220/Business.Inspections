import random
import datetime

class Inspection(object):
  def __init__(self):
    self.inspection = {
      "id" : None,
      "certificate_number" : None,
      "business_name" : None,
      "date" : None,
      "result" : None,
      "sector": None,
      "address" : None
    }
  
  def Generate(self):
    self.inspection["certificate_number"] = random.randint(1111111,9999999);
    self.inspection["date"] = datetime.datetime.now();
    self.inspection["id"] = ("{first}-{second}-ENFO".format(first = random.randint(11111,99999), second = random.randint(1111,9999)));
    inspection = { 
               "id": self.inspection["id"], 
               "certificate_number" : self.inspection["certificate_number"],
               "business_name" : "Worlds Tomorrow-{tagNum}".format(tagNum = random.randint(111,999)),
               "date" : self.inspection["date"],
               "result" : "No Violation Issued",
               "sector" : ("Retail Dealer - {buildingNumber}".format(buildingNumber = random.randint(1111,9999))),
               "address" : self.GenerateAddress()
             }
    return inspection;
  
  def GenerateAddress(self):
    self.inspection["certificate_number"] = random.randint(1111111,9999999);
    self.inspection["date"] = datetime.datetime.now();
    postalCode = random.randint(11111,99999);
    number = random.randint(1111,9999);
    self.id = ("{first}-{second}-ENFO".format(first = random.randint(11111,99999), second = random.randint(1111,9999)));
    address = {
      "city" : "SaratogaSprings",
      "zip" : postalCode,
      "street" : "world Street",
      "number" : number
    }
    
    return address