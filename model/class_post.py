from dbquery import doSql
from datetime import datetime as c_date

class Post(object):
  def __init__(self):
    self.id = ""
    self.reply = ""
    self.username = ""
    self.date = ""

  def getPost(self):
	return {\
	  "id":self.id,\
	  "reply":self.reply,\
	  "username":self.username,\
	  "timestamp":self.date}

  def setId(self,id):
    self.id = id

  def setReply(self,reply):
    self.reply = reply
    self.date = c_date.now()

  def setUsername(self,username):
    self.username = username

  def setDate(self,date):
    self.date = date

  def commit(self):
    db = doSql()

    db.execqry("SELECT * FROM update_post("+\
	str(self.id)+",'"+\
	self.reply+"','"+\
	self.date+"');", True)