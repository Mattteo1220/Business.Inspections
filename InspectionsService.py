#!/usr/bin/python
import json
import datetime
from bson import json_util
import bottle
from bottle import Bottle, template, route, run, request, abort, get, post, put, delete
from InspectionRepository import InspectionRepository
from Inspection import Inspection

class InspectionsService:
  def __init__(self):
    self._host = "localhost"
    self._port = 8080
    self._app = Bottle()
    self.InspectionRepository = InspectionRepository()
    
  def Initialize(self):
    if __name__ == '__main__':
      #app.run(debug=True)
      print("Host={host}".format(host=self._host))
      run(host=self._host, port=self._port)
      
  def __getitem__(inspection):
    return 
      
  @get('/IsAlive')
  def IsAlive():
    IsAlive = True
    string = "IsAlive: {IsAlive}\n".format(IsAlive = IsAlive)
    
    return json.loads(json.dumps(string, indent=4, default=json_util.default))
    
  @get('/read')
  def GetBusiness():
    businessName = request.query.businessName
    inspectionRepo = InspectionRepository()
    inspection = inspectionRepo.GetByBusinessName(businessName)
    
    string = "Inspection: {inspection}\n".format(inspection = inspection)
    
    if not businessName:
      abort(404, "Not Found")
    
    return json.loads(json.dumps(string, indent=4, default=json_util.default))
    
  @get('/getNewInspection')
  def GetNewBusiness():
    inspection = Inspection()
    newInspection = inspection.Generate()
    
    if newInspection is None:
      abort(404, "Failed to create an inspection")
    
    string = "businessName: {business_name}\n".format(business_name = newInspection["business_name"])
    
    return json.loads(json.dumps(string, indent=4, default=json_util.default))
  
  @post('/create')
  def CreateBusiness():
    inspectionRepo = InspectionRepository()
    inspection = Inspection()
    
    if  (request.forms.get("id") is None
      or request.forms.get("certificate_number") is None
      or request.forms.get("business_name") is None
      or request.forms.get("date") is None
      or request.forms.get("result") is None
      or request.forms.get("sector") is None
      ):
      abort(404, "Not Found")
    
    businessInspection = {
      "id": request.forms.get("id"),
      "certificate_number" : request.forms.get("certificate_number"),
      "business_name" : request.forms.get("business_name"),
      "date" : request.forms.get("date"),
      "result" : request.forms.get("result"),
      "sector" : request.forms.get("sector"),
      "address" : inspection.GenerateAddress()
    }
    
    if businessInspection is None:
      string = "Failed to create inspection"
    else:
      result = inspectionRepo.Add(businessInspection)
      string = ("Add Succeeded: {result}\n".format(result = True if result is not None else False))
    
    return json.loads(json.dumps(string, indent=4, default=json_util.default))
  
  @put('/update')
  def UpdateBusinessResult():
    inspectionRepo = InspectionRepository()
    businessId = None
    result = None
    
    if(request.forms.get("id") is None):
      abort(404, "Not Found")
    else:
      businessId = request.forms.get("id")
      
    if(request.forms.get("result") is None):
      abort(404, "Not Found")
    else:
      result = request.forms.get("result")
      
    #string = "id: {id}, result: {result}\n".format(id = businessId, result = result)
      
    inspection = inspectionRepo.Get(businessId)
    
    if(inspection is None):
      raise error("Failed to find Business")
    
    #update inspection
    inspection["result"] = result
    updateResult = inspectionRepo.UpdateBusinessResult(businessId, inspection)
    
    if(updateResult is None):
      abort(404, "Not Found")
    
    if(updateResult is not None):
      string = "Update Successful\n"
    else:
      string = "Update Failed\n"

    return json.loads(json.dumps(string, indent=4, default=json_util.default))
  
  @delete('/remove')
  def RemoveBusiness():
    inspectionRepo = InspectionRepository()
    businessId = None
    
    if(request.forms.get("id") is None):
      abort(404, "Not Found")
    else:
      businessId = request.forms.get("id")
      
    result = inspectionRepo.Delete(businessId)
    
    if(result is not None):
      string = "Remove successful\n"
    else:
      string = "Remove Unsuccessful\n"
      
    return json.loads(json.dumps(string, indent=4, default=json_util.default))
    
inspectionService = InspectionsService()
inspectionService.Initialize()

    
