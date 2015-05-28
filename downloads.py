import sqlite3 as sql
from getpass import getuser

def get_downloads(db):
	cur = db.cursor()
	cur.execute("select LSQuarantineDataURLString from LSQuarantineEvent")

	downloads = []
	rows = cur.fetchall()

	for row in rows:
		if row[0] != None:
			downloads.append(row[0])

	return downloads

def main():

	dbf = "/Users/{0}/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV2".format(getuser())
	db = sql.connect(dbf)

	for d in get_downloads(db):
		parts = d.split('/')
		d = parts[len(parts) - 1]
		print(d)

if __name__ == '__main__':
	main()