#!/usr/bin/env python
#coding:utf8

from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class Role(db.Model):
    #相当于create table role(id int primary key autoincrease,
    # roles string(20) unique);
    __tablename__ = "role"

    #角色设定有三个一个管理员,一个注册用户,一个是匿名用户
    id = db.Column(db.Integer,primary_key=True)
    roles = db.Column(db.String(20),unique=True)

    #相关
    users =db.relationship("User",backref="role")

    def __unicode__(self):
        return self.roles

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=True)
    passwd  = db.Column(db.String(100))


    role_id = db.Column(db.Integer,db.ForeignKey("role.id"))
    article = db.relationship("Article",backref="user")



    def __unicode__(self):
        return self.username

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.passwd = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.passwd, password)




class Article(db.Model):
    #文章
    __tablename__ = "article"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.Text)
    datetm = db.Column(db.DateTime,default=datetime.utcnow())

    user_id = db.Column(db.Integer,db.ForeignKey("user.id"))
    comment = db.relationship("Comment",backref="article")

    def __init__(self,title,content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id


    def __unicode__(self):
        return  self.title



class Comment(db.Model):
    #评论
    __tablename__ = "comment"

    id = db.Column(db.Integer,primary_key=True)
    comments = db.Column(db.Text)
    datetm = db.Column(db.DateTime, default=datetime.utcnow())

    article_id = db.Column(db.Integer, db.ForeignKey("article.id"))

    def __init__(self,comments,article_id):
        self.comments = comments
        self.article_id = article_id
    def __unicode__(self):
        return self.comments

