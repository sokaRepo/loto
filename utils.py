from requests import get, post
import os
import zipfile
import fileinput
from re import sub
import MySQLdb
from math import ceil

def con_mysql():
	db = MySQLdb.connect(host="localhost",    # your host, usually localhost
		                     user="root",         # your username
		                     passwd="root",  # your password
		                     db="loto")        # name of the data base
	cur = db.cursor()
	return cur, db

def is_load_running():
	cur, db = con_mysql()
	cur.execute('''SELECT value FROM settings WHERE name = 'load' ''')
	if cur.fetchall()[0][0] == 'stop':
		db.close()
		return False
	db.close()
	return True

def set_setting(name, value):
	cur, db = con_mysql()
	cur.execute('''UPDATE settings SET value = '{0}' WHERE name = '{1}' '''.format(value, name))
	db.commit()
	db.close()

def save_loto_csv():
	url = "https://media.fdj.fr/generated/game/amigo/amigo.zip"
	if os.path.isfile('csv/loto.zip'):
		os.remove('csv/loto.zip')
		#return True
	with open('csv/loto.zip', 'wb') as file:
		r = get(url, stream=True)
		if not r:
			return False
		for block in r.iter_content(1024):
			file.write(block)
	return True


def unzip_loto_csv():
	try:
		with zipfile.ZipFile('csv/loto.zip', 'r') as zip_r:
			zip_r.extract('amigo.csv', 'csv/')
		os.rename('csv/amigo.csv', 'csv/loto.csv')
		print "Uncompress OK"
		return True
	except Exception as e:
		print "ERROR (unzip_csv) : {}".format(e)
		return False


def parse(line):
	d = line.split(';')
	return d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8],d[9],d[10],d[11],d[12],d[13],d[14],d[15]

def csv_to_sql():
	i = 0
	with open('db.sql', 'w') as f_sql:
		for line in fileinput.input(['csv/loto.csv']):
			line = line.strip('\n')
			d = parse(line)
			d_w = "INSERT INTO data (id_tirage,date,heure,date_forclusion,n1,n2,n3,n4,n5,n6,n7,n_b_1,n_b_2,n_b_3,n_b_4,n_b_5) VALUES ({})".format(','.join(d))
			d_w = r = sub("([0-9]+.:[0-9]+)", r"'\1'", d_w)
			if not fileinput.isfirstline():
				f_sql.write(d_w+"\n")
				i += 1
			if i == 100000:
				break
	return i

def execute_sql():
	try:
		cur, db = con_mysql()
		cur.execute('DELETE FROM data')
		with open('db.sql', 'r') as f:
			for line in f:
				cur.execute(line)
		db.commit()		
		db.close()
		return True
	except Exception as e:
		print e
	return False

def load_data(n):
	row_per_page = 20
	cur, db = con_mysql()
	cur.execute('SELECT COUNT(*) FROM data')
	total = int(cur.fetchall()[0][0])
	nb_page = ceil(total/row_per_page)
	if n > nb_page:
		n = nb_page
	row = (n-1)*row_per_page
	cur.execute('''SELECT * FROM data LIMIT {},{} '''.format(row, row_per_page))
	return cur.fetchall()

def get_best_for_each_num():
	cur, db = con_mysql()
	all = {'n1':'', 'n2':'', 'n3':'', 'n4':'', 'n5':'', 'n6':'', 'n7':'', 'n_b_1':'', 'n_b_2':'', 'n_b_3':'', 'n_b_4':'', 'n_b_5':''}
	for n in all.iterkeys():
		cur.execute(''' SELECT  {}, count(*) AS count FROM data GROUP BY {} ORDER BY count DESC LIMIT 1'''.format(n, n))
		#print '{} => {}'.format(n, int(cur.fetchall()[0][0]) )
		all[n] = int(cur.fetchall()[0][0])
	db.close()
	return all

def get_worst_for_each_num():
	cur, db = con_mysql()
	all = {'n1':'', 'n2':'', 'n3':'', 'n4':'', 'n5':'', 'n6':'', 'n7':'', 'n_b_1':'', 'n_b_2':'', 'n_b_3':'', 'n_b_4':'', 'n_b_5':''}
	for n in all.iterkeys():
		cur.execute(''' SELECT  {}, count(*) AS count FROM data GROUP BY {} ORDER BY count ASC LIMIT 1'''.format(n, n))
		#print '{} => {}'.format(n, int(cur.fetchall()[0][0]) )
		all[n] = int(cur.fetchall()[0][0])
	db.close()
	return all