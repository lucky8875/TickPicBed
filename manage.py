#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__= 'jiangyixin'
__time__ = 2019/2/22 21:19
"""
import os
import click

from apps import create_app, db
from apps.models import User, Image

app = create_app(os.getenv('DEVELOPMENT', 'default'))


@click.group()
def cli():
    ...


@cli.command()
def startplugins(plugin_name):
    print(plugin_name)


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User, Image=Image)


if __name__ == '__main__':
    cli()
