from utils import con_mysql

def get_best_for_each_num():
	cur, db = con_mysql()
	all = {'n1':'', 'n2':'', 'n3':'', 'n4':'', 'n5':'', 'n6':'', 'n7':'', 'n_b_1':'', 'n_b_2':'', 'n_b_3':'', 'n_b_4':'', 'n_b_5':''}
	for n in all.iterkeys():
		cur.execute(''' SELECT  {}, count(*) AS count FROM data GROUP BY {} ORDER BY count DESC LIMIT 1'''.format(n, n))
		#print '{} => {}'.format(n, int(cur.fetchall()[0][0]) )
		all[n] = int(cur.fetchall()[0][0])
	db.close()
	return all


if __name__ == '__main__':
	best = get_best_for_each_num()
	print best