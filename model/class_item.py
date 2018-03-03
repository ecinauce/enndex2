from dbquery import doSql

class Item(object):
  def __init__(self):
    self.itemId = None
    self.itemName = None
    self.itemType = None
    self.itemPrice = None
    self.itemImg = None
    
  def getItem(self):
    return {\
    "id":self.itemId,\
    "name":self.itemName,\
    "type":self.itemType,\
    "price":self.itemPrice,\
    "imgurl":self.itemImg}
    
  def setId(self,id):
    self.itemId = id
    
  def setName(self,name):
    self.itemName = name
    
  def setPrice(self,price):
    self.itemPrice = price
    
  def setImg(self,imgurl):
    self.itemImg = imgurl
    
  def setType(self,type):
    self.itemType = type
    
  def delete(self):
    db = doSql()
    
    db.execqry("SELECT * FROM delete_item("+\
    self.itemId+");", True)
    
  def commit(self):
    db = doSql()
    
    db.execqry("SELECT * FROM update_item("+\
    self.itemId+",'"+\
    self.itemName+"','"+\
    self.itemType+"',"+\
    self.itemPrice+",'"+\
    self.itemImg+"');", True)