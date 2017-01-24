# -*- coding:utf-8 -*-

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class App(Base):
    __tablename__ = 'app'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    logo = Column(String)
    qrcode = Column(String)
    created_by = Column(Integer)
    created_at = Column(Integer)
    tags = Column(String)
    images = Column(String)


class Image(Base):
    __tablename__ = 'app_image'

    id = Column(Integer, primary_key=True)
    image = Column(String)


class Tag(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    name = Column(String)
