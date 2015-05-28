import csv
from math import *

def iter_table(dydx, a, fa, steps, interval, csv_file):
	writer = csv.writer(csv_file)
	writer.writerow(['Steps','Xn-1','Yn-1','h','Xn',"Y'(Xn-1)",'Yn'])
	x = a
	rows = [[0,0,0,0,0,0,0] for i in range(0,steps)]
	rows[0] = [1,a,fa,interval,a+interval,eval(dydx),fa+0.1*eval(dydx)]
	writer.writerow(rows[0])
	for n in range(1, steps):
		rows[n][0] = n+1
		rows[n][1] = rows[n-1][4]
		rows[n][2] = rows[n-1][6]
		rows[n][3] = interval
		rows[n][4] = rows[n-1][4]+interval
		x = rows[n-1][4]
		rows[n][5] = eval(dydx)
		rows[n][6] = rows[n][2] + interval*rows[n][5]
		writer.writerow(rows[n])

def main():
	dydx = input('dydx = ')
	a = float(input('a = '))
	fa = float(input('f(a) = '))
	steps = int(input('steps = '))
	interval = float(input('interval = '))
	f = open('/Users/Jacob/Desktop/euler.csv', 'w')
	iter_table(dydx, a, fa, steps, interval, f)
	f.close()

	print('\nComplete!')

if __name__ == '__main__':
	main()