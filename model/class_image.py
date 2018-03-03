#from dbquery import doSql

class Image(object):
  def __init__(self):
    self.imgId = None
    self.imgUrl = None
    self.imgTitle = None
    self.imgCap = None
    
  def getImage(self):
    return {\
    "id":self.imgId,\
    "url":self.imgUrl,\
    "title":self.imgTitle,\
    "caption":self.imgCap}
    
  def setId(self,id):
    self.imgId = id
    
  def setUrl(self,url):
    self.imgUrl = url
    
  def setTitle(self,title):
    self.imgTitle = title
    
  def setCap(self,caption):
    self.imgCap = caption
    
  def commit(self):
    pass
    """
    db = doSql()
    
    db.execqry("SELECT * FROM update_image("+\
    str(self.imgId)+",'"+\
    self.imgUrl+",'"+\
    self.imgTitle+",'"+\
    self.imgCap+");", True)
    """