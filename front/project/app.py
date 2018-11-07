from flask import Flask
from flask import request
from xgboot实现.test1 import  trainandTestNeedPrams
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/getXgbootData', methods=['get'])
def getXgbootData():
    grade1 = request.args.get('grade1')
    grade2 = request.args.get('grade2')
    grade3 = request.args.get('grade3')
    print (grade1,grade2,grade3)
     #trainandTestNeedPrams()
    '''
    将三个参数送入集合中。'''
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()