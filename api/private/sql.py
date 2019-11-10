#!/usr/bin/python

import sqlalchemy
import sqlalchemy.orm
import private.constants

def get_dialect():
	return private.constants.sql_dialect
def get_driver():
	return private.constants.sql_driver
def get_host():
	return private.constants.sql_host
def get_port():
	return private.constants.sql_port
def get_user():
	return private.constants.sql_user
def get_password():
	return private.constants.sql_password
def get_db():
	return private.constants.sql_db

def sql_create_session():
	url = sqlalchemy.engine.url.URL(get_driver(), get_user(),
			get_password(), get_host(), get_port(), get_db())
	engine = sqlalchemy.create_engine(url)
	Session = sqlalchemy.orm.sessionmaker(bind=engine)
	return Session()
