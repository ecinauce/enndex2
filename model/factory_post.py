from class_post import Post
from dbquery import doSql
from datetime import datetime as c_date

class PostFactory(object):
  @staticmethod
  def createPostFromId(p_postId):
    db = doSql()

    if not p_postId:
      return None

    query = "SELECT * FROM get_post("+str(p_postId)+");"

    ((
      id,
      username,
      reply,
      date
    ),) = db.execqry(query, False)

    post = Post()
    post.setId(id)
    post.setUsername(username)
    post.setReply(reply)
    post.setDate(date)

    return post

  @staticmethod
  def createPost(p_username,p_reply):
    from factory_log import LogFactory
    db = doSql()

    query = "SELECT * FROM add_post('"+\
    p_username+"','"+\
    p_reply+"','"+\
    str(c_date.now())+"');"
        
    ((status_code,
      ),) = db.execqry(query, True)
    
    var = str((p_username, p_reply))
    sPosts = var.split("'")
    x = ""
    for i in sPosts:
      x = x + i
    LogFactory.createLog("createPost",x,"None")
    return status_code
    
  @staticmethod
  def createPostList():
    from factory_log import LogFactory
    db = doSql()

    query = "SELECT * FROM get_all_posts();"
    rawPostList = db.execqry(query, False)
    #raise Exception(rawPostList)
    postList = []

    if len(rawPostList) > 0 and not rawPostList[0] == ['None']:
      for i in rawPostList:
        from factory_post import PostFactory
      
        #raise Exception(type(i))
        postList += [PostFactory.createPostFromId(i[0]).getPost()]
        
    sPosts = str(postList).split("'")
    x = ""
    for i in sPosts:
      x = x + i
    LogFactory.createLog("createPostList","None",x)
    
    return postList
    
  @staticmethod  
  def createPostSection(index, offset):
    db = doSql()
    
    query = "SELECT * FROM get_post_section("+str(index)+","+str(offset)+");"
    rawPostList = db.execqry(query, False)
    
    postList = []

    if len(rawPostList) > 0 and not rawPostList[0] == ['None']:
      for i in rawPostList:  
        from factory_post import PostFactory
      
        try: 
          postList += [PostFactory.createPostFromId(i[0]).getPost()]
        except ValueError:
          pass

    #raise Exception(itemList)
    return postList
    