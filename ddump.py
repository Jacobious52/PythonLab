import sqlite3 as sql
import csv
import sys
from getpass import getuser

def dump_downloads(db):
	cur = db.cursor()
	cur.execute("select LSQuarantineDataURLString from LSQuarantineEvent")

	f = open("downloads_dump.csv", "w")
	w = csv.writer(f)
	rows = cur.fetchall()

	for row in rows:
		if row[0] == None:
			continue
		w.writerow([row[0]])

	f.close()


def erase_downloads(db):
	cur = db.cursor()
	cur.execute("delete from LSQuarantineEvent")
	db.commit()

def main():
	arg = sys.argv[1]
	dbf = "/Users/{0}/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV2".format(getuser())
	if arg == "dump":
		print("dumping downloads to file...")
		db = sql.connect(dbf)
		dump_downloads(db)
		db.close()
		print("dump complete")
	elif arg == "del":
		print("erasing downloads...")
		db = sql.connect(dbf)
		erase_downloads(db)
		db.close()
		print("erase complete")
	else:
		print("usage: ddump <dump|del>")

if __name__ == '__main__':
	main()