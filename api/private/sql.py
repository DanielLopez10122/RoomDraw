#!/usr/bin/python

import mysql.connector as mysql
import private.constants as constants

class SQL:
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
