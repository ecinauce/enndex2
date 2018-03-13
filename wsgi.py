import os
from flask import Flask, request, session, g, redirect, abort, flash, render_template, url_for, jsonify, json, escape
from werkzeug.security import generate_password_hash, check_password_hash

application = Flask(__name__)
# set the secret key.  keep this really secret:
application.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
#application.secret_key = os.urandom(24)

@application.route('/privacy/')
def privacy():
  return 'Facebook: I wanted to remove the login feature from the app, but unfortunately the users cant. A google search to stack overflow said so. But anyways, privacy policy, I will not store information, the main purpose for the Facebook app "Ennchan" is for self-education and exploration.'

@application.route('/ball/')
def ball():
  return render_template('ball.html')

@application.route('/')
def index():
  from pymongo import MongoClient
  import os
  
  wew = MongoClient('mongodb://userUIA:8YhwyYPaUmfH4Khx@mongodb:27017/ennchandb')
  
  wewDb = wew.ennchandb
  wewCol = wewDb.col
  wewCol.insert({"status":"OK"})
  out = wewCol.find_one()
  
  return render_template('slate.html')
  
@application.route('/testimonial')
def testimonial():
  from model.factory_post import PostFactory as pf
    
  postList = pf.createPostSection(1, 4)
  #raise Exception(postList[0])
  if 'username' in session:
    return render_template('dot.html', username=session['username'], posts=postList)
  return render_template('dot.html', posts=postList)
      
@application.route('/register/', methods=['POST'])
def register():
  if request.method == 'POST':
    from model.mFactory_user import MongoUserFactory as muf
    
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    
    return jsonify({'status':muf.createUser(username, password, email)})
    """
    from model.factory_user import UserFactory as uf
    
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    
    return jsonify({'status':uf.createUser(username, password, email)})"""
  return jsonify({'status':'BAD REQUEST'})


@application.route('/login/', methods=['POST'])
def login():
  from pymongo import MongoClient
  """
  from model.factory_user import UserFactory as uf
  from model.dbquery import doSql
  
  db = doSql()

  query = "select * from get_pass('"+str(request.form['username'])+"');"
  
  ((password,),) = db.execqry(query, True)
  """
  
  try:
    u = uf.createUserName(request.form['username'])
  except ValueError:
    return jsonify({'status':'WRONG CREDS'})
    
  if request.form['password'] == password:
    session['username'] = request.form['username']
  
    return jsonify({"username":session['username']})
  return jsonify({'status':'WRONG CREDS'})
   
@application.route('/logout/')
def logout():
  session.pop('username',None)
  return redirect(url_for('index'))
   
@application.route('/sendPost/', methods=['POST'])
def sendPost():
  from model.factory_post import PostFactory as pf
  
  return jsonify({'status':pf.createPost(session['username'], request.form['reply'])})

@application.route('/getPost/', methods=['GET','POST'])
def getPost():
  if request.method == 'POST':
    from model.factory_post import PostFactory as pf
    
    return jsonify(pf.createPostSection(request.form['index'], request.form['offset']))
  
if __name__ == "__main__":
  #Deployment script
  #application.run(host='0.0.0.0', port=8080)
  #Development script
  application.run(host='localhost', port=80, debug=True)