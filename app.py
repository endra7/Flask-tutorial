from flask import Flask

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

if __name__=='__main__':
    app.debug=True
    app.run()
    app.run(debug=True)