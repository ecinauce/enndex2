from class_item import Item
from dbquery import doSql
from datetime import datetime as c_date
from factory_log import LogFactory

class ItemFactory(object):
  @staticmethod
  def createItemFromId(p_itemId):
    db = doSql()

    if not p_itemId:
      return None

    query = "SELECT * FROM get_item("+str(p_itemId)+");"
    
    ((
      id,
      name,
      iType,
      price,
      imgurl
    ),) = db.execqry(query, False)

    item = Item()
    item.setId(id)
    item.setName(name)
    item.setType(iType)
    item.setPrice(price)
    item.setImg(imgurl)
    
    return item
  
  @staticmethod
  def createItem(p_itemName,p_itemType,p_itemPrice,p_itemImg):
    db = doSql()

    query = "SELECT * FROM add_item('"+\
    p_itemPrice+"','"+\
    p_itemName+"','"+\
    p_itemType+"','"+\
    p_itemImg+"');"
        
    item = Item()
    item.setId(0)
    item.setName(p_itemName)
    item.setType(p_itemType)
    item.setPrice(p_itemPrice)
    item.setImg(p_itemImg)
        
    ((status_code,
      ),) = db.execqry(query, True)

    return item
    
  @staticmethod
  def createItemList():
    db = doSql()

    query = "SELECT * FROM get_all_items();"
    rawItemList = db.execqry(query, False)
    itemList = []

    if len(rawItemList) > 0 and not rawItemList[0] == ['None']:
      for i in rawItemList:
        from factory_item import ItemFactory
      
        itemList += [ItemFactory.createItemFromId(i[0]).getItem()]

    return itemList
  
  @staticmethod  
  def createItemPage(index, offset):
    db = doSql()
    
    query = "SELECT * FROM get_item_section("+str(index)+","+str(offset)+");"
    rawItemList = db.execqry(query, False)
    
    itemList = []

    if len(rawItemList) > 0 and not rawItemList[0] == ['None']:
      for i in rawItemList:  
        from factory_item import ItemFactory
      
        try: 
          itemList += [ItemFactory.createItemFromId(i[0]).getItem()]
        except ValueError:
          pass

    #raise Exception(itemList)
    return itemList
    