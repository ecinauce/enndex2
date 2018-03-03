#factory_log
from class_log import Log
from dbquery import doSql
from datetime import datetime as c_date

class LogFactory(object):
  @staticmethod
  def createLogFromId(p_logId):
    db = doSql()

    if not p_logId:
      return None

    query = "SELECT * FROM get_log("+str(p_logId)+");"
        
    ((
      id,
      foo,
      val,
      date,
      ret
    ),) = db.execqry(query, False)

    log = Log()
    log.setId(id)
    log.setFoo(foo)
    log.setVal(val)
    log.setDate(date)
    log.setRet(ret)

    return log

  @staticmethod
  def createLog(p_foo,p_val,p_ret):
    db = doSql()
    
    log = Log()
    log.setFoo(p_foo)
    log.setVal(p_val)
    log.setRet(p_ret)

    query = "SELECT * FROM add_log('"+\
    log.getLog()["function"]+"','"+\
    log.getLog()["value"]+"','"+\
    str(c_date.now())+"','"+\
    log.getLog()["return"]+"');"
        
    ((status_code,
      ),) = db.execqry(query, True)

    return status_code
    
  @staticmethod
  def createLogList():
    db = doSql()

    query = "SELECT * FROM get_all_logs();"
    rawLogList = db.execqry(query, False)
    #raise Exception(rawPostList)
    logList = []

    if len(rawLogList) > 0 and not rawLogList[0] == ['None']:
      for i in rawLogList:
        from factory_log import LogFactory
      
        logList += [LogFactory.createLogFromId(i[0]).getLog()]
    return logList