# -*- coding: utf-8 -*-

import pymysql

mysqlDB = {
	"host":"",
	"port": 0,
	"user":"",	
	"password":"",
	"database":""
}

def selectFunction():
	SQLselect = """
		SELECT * FROM TABLE;
	"""
	try:
		conn = mysqlDB.connect(
				host = mysqlDB["host"],
				port = mysqlDB["port"],
				user = mysqlDB["user"],
				password = mysqlDB["password"],
				database = mysqlDB["database"]
			)
		cur = conn.cursor()
		cur.execute(SQLselect)
		result = cur.fetchall()
		cur.close()
		conn.close()
		return result
	except Exception as e:
		return -1

def insertFunction():
	SQLinsert = """
	"""
	try:
		conn = mysqlDB.connect(
			host = mysqlDB["host"],
			port = mysqlDB["port"],
			user = mysqlDB["user"],
			password = mysqlDB["password"],
			database = mysqlDB["database"]
		)
		cur = conn.cursor()
		cur.execute(SQLinsert)
		conn.commit()
		cur.close()
		conn.close()
	except Exception as e:
		return -1
