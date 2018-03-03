from dbquery import doSql

class User(object):
  def __init__(self):
    self.userId = None
    self.userName = None
    self.userPass = None
    self.userType = None
    
  def getUser(self):
    return {\
    "id":self.userId,\
    "name":self.userName,\
    "type":userType}
    
  def setId(self,id):
    self.userId = id
    
  def setName(self,name):
    self.userName = name
    
  def setPass(self,password):
    self.userPass = password
    
  def setType(self,type):
    self.userType = type
    
  def commit(self):
    db = doSql()
    
    db.execqry("SELECT * FROM update_product("+\
    str(self.prodId)+",'"+\
    self.prodName+",'"+\
    self.prodDim+",'"+\
    self.prodPrice+",'"+\
    self.prodCapacity+",'"+\
    self.prodType+");", True)