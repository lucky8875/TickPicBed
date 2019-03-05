#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__= 'jiangyixin'
__time__ = 2019/2/22 21:19
"""
import os

from application.app import create_app, db
from application.models import User, Image
from flask_migrate import Migrate

app = create_app(os.getenv('DEVELOPMENT', 'default'))
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User, Image=Image)

