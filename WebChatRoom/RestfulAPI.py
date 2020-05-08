import userSql
from flask import Flask,jsonify,request,Response,url_for,render_template,redirect

app = Flask(__name__,static_folder='templates/images',template_folder='templates')

@app.route('/')
def index():
    return render_template('test.html')



@app.route('/login',methods=['POST','GET'])
def LoginAPI():
    if request.method=='POST':
        userinfo = userSql.GetUserInfo()
        account=Flask.request_class.values('account')
        print(account)
        return render_template('index.html')

app.run()