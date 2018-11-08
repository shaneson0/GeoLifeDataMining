from flask import Flask
from flask import request

app = Flask(__name__)
import service


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

@app.route('/getJSONData', methods=['get','post'])
def getXgbootData():
    id= request.args.get('user_id')
    date= request.args.get('user_date')
    print (id,date)
    #从文件中获取数据。
    result = service.getJsonDataBy_File(int(id),str(date))
    if  result=="":
        return "successCallback" + "(" + 'no' + ")"
    else:
        return "successCallback" + "(" + result + ")"  # 将结果以json形式返回，通过jsonp与前台交互





if __name__ == '__main__':
    app.run()