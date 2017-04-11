#!/usr/bin/env python
#coding:utf8

from  flask import request,redirect,render_template,url_for,make_response,session,flash

from app.main import  main
from app.models import User,Role,Article,Comment

from app import db

@main.route("/",methods=["GET","POST"])
@main.route("/index")
def index():
    if request.method == "POST":
        username = request.form.get("username")
        passwd  = request.form.get("password")

        pass_url = User.query.filter_by(username=username).first()
        if pass_url == None :
            flash("NO USER")
            return render_template("registered.html")
        try:
            password = pass_url.verify_password(passwd)
            if  password is False:
                flash("PASSWORD IS WRONG")
                return redirect(url_for("main.index"))
            else:
                session["user"] = username
                # resp = make_response(render_template("main.html" ,user=username))
                # resp.set_cookie("userid",username)
                # return resp
                return redirect(url_for("main.blog"))

        except:
            erromassage = "You password is wrong"
            return render_template("erro.html")

    else:
        return render_template("index.html")


@main.route("/registered", methods=["POST","GET"])
def registe():
    if request.method == "POST":
        username = request.form.get("loginname")
        passwd = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        if user != None:
            flash( "THE USER HAS REGISTERED ")
        else:
            #这里后期写个函数,做格式校检

            new_user = User(username=username,password=passwd,role_id=2)

            db.session.add(new_user)
            db.session.commit()

            flash('You can now login.')
            return redirect(url_for('main.index'))
        return  render_template("index.html")
    else:
        return render_template("registered.html")


@main.route("/main",methods=["GET","POST"])
def blog():
    #展示内容不管是否登入都可以查看内容,如果登入可以自己修改自己内容(换个函数)
    #只是展示前10个页面,后面进行分页
    #进行搜索
    #print  session["user"]
    if request.method=="POST":
        title = request.form.get("search")
        all = Article.query.filter(Article.title.like(title)).all()
    else:
        all = Article.query.all()

    return render_template("main.html",title=all)


@main.route("/write",methods=["POST","GET"])
def write_aritle():
    user = session.get("user")
    userid = User.query.filter_by(username=user).first().id
    if request.method=="GET":
        if user != None and User.query.filter_by(username=user):
            print "this is write save session %s"%session.get("user")
            return render_template("write.html")
        else:
            return render_template("registered.html")
    #这里存入应该是带有html标签的内容以便存储信息
    if request.method =="POST":
        t = request.form.get("title")
        con = request.form.get("content")

        title = Article(title=t,content=con,user_id=userid)
        db.session.add(title)
        db.session.commit()
        return redirect(url_for("main.blog"))

@main.route("/<int:id>")
def look_aritle(id):

    aritle = Article.query.filter_by(id=id).first()
    title = aritle.title
    content = aritle.content

    p = Comment.query.get(id)
    if request.method =="POST":
        _commit = request.form.get("提交内容")
        commit_Comment = Comment(comments=_commit)
        db.session.add(commit_Comment)
        db.session.commit()
        redirect(url_for("main.look_aritle",name=id))

    return render_template("lookaritle.html",title=title,content=content,discuss=p)


@main.route('/logout')
def logout():
   # remove the username from the session if it is there

   session.pop('user', None)
   return redirect(url_for('main.index'))


