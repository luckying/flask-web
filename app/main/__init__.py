#!/usr/bin/env python
#coding:utf8



from flask import Blueprint

main = Blueprint('main',__name__)

from app.main import errors,views
