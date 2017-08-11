from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

# 创建登录和注册的模板，包含账号，密码和一个提交按钮
class Login_Form(FlaskForm):
    name = StringField('user_name', validators=[DataRequired()])
    pwd = PasswordField('user_password', validators=[DataRequired()])
    submit = SubmitField('Login in')


class Register_Form(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    pwd =PasswordField('pwd', validators=[DataRequired()])
    submit = SubmitField('Register')


