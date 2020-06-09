import json
import random
import datetime
from bson import json_util
from pymongo import MongoClient
from pprint import pprint

class InspectionRepository(object):
  def __init__(self):
    self.Connection = MongoClient('localhost', 27017)
    self.DataBase = self.Connection["city"]
    self.Inspections = self.DataBase["inspections"]
    
  def Add(self, inspection):
    try:
      result = self.Inspections.save(inspection);
      
    except Exception as error:
      raise error;
      
    return result;
  
  def Get(self, id):
    try:
      result = self.Inspections.find_one({"id" : id})
      
    except Exception as error:
      raise error
      
    return result
  
  def GetByBusinessName(self, businessName):
    try:
      result = self.Inspections.find_one({"business_name": businessName})
      
    except Exception as error:
      print("Error: {error}".format(error = error))
      raise error
      
    return result
  
  def UpdateBusinessName(self, id, businessName):
    try:
      business = self.Get(id)
      business["business_name"] = businessName
      result = self.Inspections.update({"id" : id}, business)
    
    except Exception as error:
      raise error
      
    return result
  
  def UpdateBusinessResult(self, id, result):
    try:
      business = self.Get(id)
      business["result"] = result
      result = self.Inspections.update({"id" : id}, business)
    
    except Exception as error:
      raise error
      
    return result
  
  def Delete(self, id):
    try:
      result = self.Inspections.delete_one({"id" : id})
      
    except Exception as error:
      raise error
      
    return result  
    
inspecRepo = InspectionRepository() 