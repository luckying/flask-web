#!/usr/bin/env python
#coding:utf8

import os
from app import creat_app,db
from app.models import Role,User,Article,Comment
from config import config
from flask_script import Shell,Manager

app = creat_app("production")
manager = Manager(app)

def test():
    return dict(app=app,db=db,Role=Role,User=User,Article=Article,Comment=Comment)

manager.add_command("shell",Shell(make_context=test))





if __name__ =="__main__":
    #app = creat_app(os.getenv('FLASK_CONFIG') or'production')
    #app.run(debug=True)
    manager.run()