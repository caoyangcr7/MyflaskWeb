# 视图类，交互GUI
from flask import render_template,Blueprint,redirect,url_for,flash
from Start import db

from Start import login_manger
from Form import Login_Form,Register_Form
from Model import Users
from flask_login import LoginManager,login_user,UserMixin,logout_user,login_required

blog =Blueprint('blog', __name__)


@blog.route('/')
def index():
    form = Login_Form()
    return render_template('login.html', form=form)


@blog.route('/index')
def l_index():
    form =Login_Form()
    return render_template('login.html',form=form)


@blog.route('/login', methods = ['GET','POST'])
def login():
    form =Login_Form()
    if form.validate_on_submit():
        user =Users.query.filter_by(user_name = form.name.data).first()
        print(user.user_password)
        if user is not None and user.user_password == form.pwd.data:
            login_user(user)
            flash('登录成功！')
            return render_template('ok.html',user_name = form.name.data)
        else:
            flash('用户名或密码错误')
            return render_template('login.html',form = form)


@blog.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已经退出登录')
    return redirect(url_for('blog.index'))


@blog.route('/register',methods = ['GET','POST'])
def register():
    form = Register_Form()
    if form.validate_on_submit():
        user = Users(name = form.name.data,pwd = form.pwd.data)
        db.session.add(user)
        db.session.commit()
        flash('注册成功')
        return redirect(url_for('blog.index'))
    return render_template('register.html', form=form)
