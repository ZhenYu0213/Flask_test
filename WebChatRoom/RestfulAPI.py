import APIResponse
import userSql
from flask import Flask,jsonify,url_for,render_template,redirect,Response,request,url_for,flash,make_response
from forms import RegistrationForm,LoginForm

app = Flask(__name__,template_folder='templates')

app.config['SECRET_KEY'] = '5ace689c10ea1f012275875e99c1c9c2'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    userInfo = userSql.GetUserInfo()
    print(userInfo)
    for info in userInfo:
        if form.account.data == info['userAccount'] and form.password.data == info['userPassword']:
            return jsonify(errCode='1',errMsg='success')
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('sign.htm',form=form)


@app.route("/adminLogin", methods=['GET', 'POST'])
def AdminLogin():
    form = LoginForm()
    userInfo = userSql.GetUserInfo()
    print(userInfo)
    if form.validate_on_submit():
        for info in userInfo:
            if form.account.data == info['userAccount'] and form.password.data == info['userPassword']:
                flash('You have been logged in!', 'success')
                return redirect(url_for('home'))
            else:
                flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('adminLogin.html', title='Login', form=form)
app.run()


