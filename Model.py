from flask_login import login_user,LoginManager,logout_user,login_required,UserMixin
from flask_sqlalchemy import SQLAlchemy
from Start import login_manger
from Start import db

# 定义模型
class Users(UserMixin, db.Model):
    __tablename__= 'login'
    user_id = db.Column(db.Integer, primary_key =True)
    user_name = db.Column(db.String(64), unique = True,index = True)
    user_password = db.Column(db.String(64), unique = True,index = True)

    def __init__(self, name, pwd):
        self.user_name = name
        self.user_password = pwd

    def get_id(self):
        return self.user_id

    def __repr__(self):
        return '<User %r>'% self.user_name

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False
