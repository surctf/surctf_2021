# -*- coding: utf-8 -*-

import peewee as pw
from random import randint

db = pw.SqliteDatabase('konkursy.db')


class Konkurs(pw.Model):
    konkurs_id = pw.PrimaryKeyField()
    text = pw.CharField()
    hash = pw.CharField()

    class Meta:
        database = db


def create_tables():
    with db:
        db.create_tables([Konkurs])


def get_konkurs(hash):
    try:
        konkurs = Konkurs.get(Konkurs.hash == hash)
        return konkurs.text
    except pw.DoesNotExist:
        return "Конкурс не найден"


def rand_konkurs():
    konkurs = Konkurs.get(Konkurs.konkurs_id == randint(1, 10))
    return konkurs.hash
