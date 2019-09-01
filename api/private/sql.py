#!/usr/bin/python

import mysql.connector as mysql
from . import constants

class _SQL():
	def __init__(self, host=constants.sql_host, user=constants.sql_user, password=constants.sql_password, db=constants.sql_db):
		self._connection = mysql.connect(host=host, user=user, password=password, database=db)
		self._cursor = self._connection.cursor()
	def __del__(self):
		self._connection.disconnect()

	# return multiple rows
	def run_stored_proc_for_multiple_items(self, stored_proc, *args):
		self._cursor.callproc(stored_proc, args)
		for result in self._cursor.stored_results():
			return result.fetchall()

	# return a single row
	def run_stored_proc_for_single_item(self, stored_proc, *args):
		try:
			return self.run_stored_proc_for_multiple_items(stored_proc, *args)[0]
		except IndexError:
			return None

	# just do something
	def run_stored_proc(self, stored_proc, *args):
		self._cursor.callproc(stored_proc, args)

		# flush the results
		for result in self._cursor.stored_results():
			result.fetchall()

	# commit the results to the database
	def commit(self):
		self._connection.commit()

def _sql_init(host=constants.sql_host, user=constants.sql_user,
		password=constants.sql_password, db=constants.sql_db):
	return _SQL(host, user, password, db)
def sql_run_stored_proc(stored_proc, *args):
	s = _sql_init()
	s.run_stored_proc(stored_proc, *args)
	s.commit()
def sql_run_stored_proc_for_single_item(stored_proc, *args):
	return _sql_init().run_stored_proc_for_single_item(stored_proc, *args)
def sql_run_stored_proc_for_single_item(stored_proc, *args):
	return _sql_init().run_stored_proc_for_multiple_items(stored_proc, *args)
