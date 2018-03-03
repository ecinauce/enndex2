#from dbquery import doSql

class Partner(object):
  def __init__(self):
    self.partId = None
    self.partName = None
    self.partAddress = []
    self.partNumber = []
    self.partUrl = None
    
  def getPart(self):
    return {\
    "id":self.partId,\
    "name":self.partName,\
    "address":self.partAddress,\
    "number":self.partNumber,\
    "url":self.partUrl}
    
  def setId(self,id):
    self.partId = id
    
  def setName(self,name):
    self.partName = name
    
  def addAddress(self, newAdd):
    self.partAddress += [newAdd]
  
  def delAddress(self, address):
    temp = []
    for i in self.partAddress:
      if not i == address:
        temp += i
        
    self.partAddress = temp
   
  def addNumber(self, newNum):
    self.partNumber += [newNum]
  
  def delAddress(self, number):
    temp = []
    for i in self.partNumber:
      if not i == number:
        temp += i
        
    self.partNumber = temp
      
  def setUrl(self,url):
    self.partUrl = url
    
  def commit(self):
    pass
    """
    db = doSql()
    
    db.execqry("SELECT * FROM update_partner("+\
    str(self.partId)+",'"+\
    self.partName+",'"+\
    self.partAddress+",'"+\
    self.partNumber+",'"+\
    self.partUrl+");", True)
    """