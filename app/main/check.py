#!/usr/bin/env python
#coding:utf8
from werkzeug.security import generate_password_hash, check_password_hash


class check_password(object):
    def set_password(self, password):
        passwd = generate_password_hash(password)
        return passwd

    def verify_password(self,check_passwd ,old_password):
        return check_password_hash(check_passwd, old_password)
