from class_user import User
from dbquery import doSql
from datetime import datetime as c_date

class UserFactory(object):
  @staticmethod
  def createUserFromId(p_userId):
    db = doSql()

    if not p_userId:
      return None

    query = "SELECT * FROM get_user("+str(p_userId)+");"
        
    ((
      id,
      username,
      uType
    ),) = db.execqry(query, False)

    user = User()
    user.setId(id)
    user.setName(username)
    user.setType(uType)

    return user
    
  @staticmethod
  def createUserName(p_userName):
    db = doSql()

    if not p_userName:
      return None

    query = "SELECT * FROM get_userName('"+str(p_userName)+"');"
    
    ((
      id,
      username,
      uType
    ),) = db.execqry(query, False)

    user = User()
    user.setId(id)
    user.setName(username)
    user.setType(uType)

    return user

  @staticmethod
  def createUser(p_username,p_password,p_email):
    db = doSql()

    query = "SELECT * FROM add_user('"+\
    p_username+"','"+\
    p_password+"','"+\
    p_email+"');"
        
    ((status_code,
      ),) = db.execqry(query, True)

    return status_code