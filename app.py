from flask import Flask, redirect,request, url_for, render_template, make_response,session,escape
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.secret_key='x4s5er4AD445'
@app.route('/')
def hello():
    return ('Hello')

#Variable rule : binding URL to variable

#binding string variable
@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s' %name

#binding int and float variable
@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog No %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' % revNo

#URL building
# Greet admin as is. Greet others as guest
@app.route('/admin')
def admin():
    return 'Hello admin'
@app.route('/guest/<guest>')
def guest(guest):
    return 'Hello %s as Guest' % guest
@app.route('/user/<name>')
def user(name):
    if name=='admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest',guest=name))

#3-------------Side ways to get value from form and display-----
@app.route('/form')
def register():
    return render_template('register.html')

@app.route('/verify', methods=['POST','GET'])
def verify():
    if request.method=='POST':
        name=request.form['name']
        return redirect(url_for('guest',guest=name))
#4--------------------Trying out jinja2 template engine - basic----
@app.route('/welcome/<user>')
def welcome(user):
    return render_template('welcome.html', name=user,marks=60)
#5----------using for loop, dict and table ---- with jinja2 and  flask--
@app.route('/result')
def result():
    scores = {'phy':60,'chem':60,'maths':70}
    return render_template('result.html', result=scores)

#6-----Working with static files ---Not working..at greet.html js static script path
@app.route('/greet')
def greet():
    return render_template('greet.html')

#7---Sending form data to template
#a form is rendered through /student.html and is posted to /display URLwhich tirggers the display function
@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/display',methods=['POST','GET'])
def display():
    if request.method=='POST':
        result = request.form
        return render_template("display.html",result=result)

#8 setting and getting cookies
#Get potential cookie data from any form. Getting data from welcome.html and set form action to /setcookie over there
@app.route('/setcookie',methods=['POST','GET'])
def set_cookie():
    if request.method=='POST':
        user=request.form['user']
        password=request.form['password']

        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('user',user)
        resp.set_cookie('pass',password)
        return resp
#hmm... can't redirect before returning response can I? 

@app.route('/readcookie')
def read_cookie():
    return render_template('readcookie.html')

@app.route('/getCookie')
def getCookie():
    name=request.cookies.get('user')
    password = request.cookies.get('pass')
    return (render_template('getCookie.html',name=name,password=password))

#--Working with sessions Ensure app.secret_key is set and session is imported from flask
@app.route('/mysession')
def mysession():
    if 'username' in session:
        username = session['username']
        return 'Logged in as '+username+'<br> <a href="/logout">Click here to log out</a>'
    else:
        return 'You are not logged in <br> <a href="/login"> Click here to log in </a>'
@app.route('/login', methods=['POST','GET'])
def login():
    if request.method=="POST":
        session['username'] = request.form['username']
        return redirect(url_for('mysession'))
    return '''
    <form action="" method="POST">
    <input type ="text" name="username"/>
    <input type="submit" value="login"/>
    </form>
    '''
@app.route('/logout')
def logout():
    #remove username from session
    session.pop('username', None)
    return redirect(url_for('mysession'))
#--file uploading-----------
@app.route('/upload')
def file_upload():
    return render_template('upload.html')
@app.route('/uploader', methods=['POST','GET'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return "File uploaded successfully"


if __name__=='__main__':
    app.debug=True
    app.run()
    app.run(debug=True)