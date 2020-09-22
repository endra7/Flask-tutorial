from flask import Flask, redirect,request, url_for, render_template

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
if __name__=='__main__':
    app.debug=True
    app.run()
    app.run(debug=True)