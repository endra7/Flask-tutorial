from flask import Flask, redirect, url_for

app = Flask(__name__)

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

if __name__=='__main__':
    app.debug=True
    app.run()
    app.run(debug=True)