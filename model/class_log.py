#class_log.py
from dbquery import doSql
from datetime import datetime as c_date

class Log(object):
  def __init__(self):
    self.id = ""
    self.foo = ""
    self.val = ""
    self.date = ""
    self.ret = ""

  def getLog(self):
	return {\
	  "id":self.id,\
	  "function":self.foo,\
	  "value":self.val,\
	  "timestamp":self.date,\
      "return":self.ret}

  def setId(self,id):
    self.id = id

  def setFoo(self,foo):
    self.foo = foo
    self.date = c_date.now()
    
  def setRet(self,ret):
    self.ret = ret

  def setVal(self,val):
    m = str(val).split("'")
    s = ""
    for i in m:
      s = s + i
    self.val = s

  def setDate(self,date):
    self.date = date

  """
  def commit(self):
    db = doSql()

    db.execqry("SELECT * FROM update_log("+\
	str(self.id)+",'"+\
	self.reply+"','"+\
	self.date+"');",\
    True)
  """