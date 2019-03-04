#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__= 'jiangyixin'
__time__ = 2019/3/4 21:33
"""
from application.app import db


def db_session_commit():
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise Exception(e)


class ModelMixin(object):

    def save(self):
        db.session.add(self)
        db_session_commit()
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        if commit:
            db_session_commit()

    def add(self):
        db.session.add(self)

    def update(self, **kwargs):
        required_commit = False
        for k, v in kwargs.items():
            if hasattr(self, k) and getattr(self, k) != v:
                required_commit = True
                setattr(self, k, v)
        if required_commit:
            db_session_commit()
        return required_commit

    @classmethod
    def add_or_save(cls, where: dict, **kwargs):
        record = cls.query.filter_by(**where).first()
        if record:
            record.update(**kwargs)
        else:
            record = cls(**kwargs).save()
        return record

    def to_json(self):
        if hasattr(self, '__table__'):
            return {i.name: getattr(self, i.name) for i in self.__table__.columns}
        raise AssertionError(f'<${self} does not hace attribute for __table__>')
