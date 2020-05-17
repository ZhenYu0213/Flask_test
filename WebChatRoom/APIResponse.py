import userSql
import RestfulAPI
from forms import RegistrationForm,LoginForm
from flask import Flask,jsonify,url_for,render_template,redirect,Response,request,url_for,flash

def login():
    userinfo = userSql.GetUserInfo()
    form = LoginForm()
    if form.validate_on_submit():
        flash('成功登入','success')
        return redirect(url_for('index'))
    else :
        flash('登入失敗','fail')
        return render_template('login.html',title='Login',form=form)