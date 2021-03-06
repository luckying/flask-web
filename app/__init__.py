#!/usr/bin/env python
#coding:utf8



from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config


db = SQLAlchemy()


def creat_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)


    from app.main import main as lantu
    app.register_blueprint(lantu)

    return  app




