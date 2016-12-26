from flask import Blueprint, render_template, request, session, redirect
from utils import *
from json import dumps as jsonify

ajax = Blueprint('ajax', __name__)

@ajax.route('/ajax/save-csv')
def load_csv():
	if is_load_running():
		return render_template('ajax.html', info=jsonify({'status':'running'}))
	set_setting('load', 'running')
	if save_loto_csv():
		return render_template('ajax.html', info=jsonify({'status':'ok'}))
	set_setting('load', 'stop')
	return render_template('ajax.html', info=jsonify({'status':'error'}))

@ajax.route('/ajax/unzip-csv')
def unzip_csv():
	if unzip_loto_csv():
		return render_template('ajax.html', info=jsonify({'status':'ok'}))
	set_setting('load', 'stop')
	return render_template('ajax.html', info=jsonify({'status':'error'}))

@ajax.route('/ajax/csv-sql')
def csv_sql():
	n = csv_to_sql()
	if n > 0:
		return render_template('ajax.html', info=jsonify({'status':'ok', 'n':n}))
	set_setting('load', 'stop')
	return render_template('ajax.html', info=jsonify({'status':'error'}))

@ajax.route('/ajax/exec-sql')
def exec_sql():
	set_setting('load', 'stop')
	if execute_sql():
		return render_template('ajax.html', info=jsonify({'status':'ok'}))
	return render_template('ajax.html', info=jsonify({'status':'error'}))

@ajax.route('/ajax/dbtable/<int:page>')
def get_db_table(page):
	return render_template('table.html', data=load_data(int(page)), page=int(page) )

@ajax.route('/ajax/stat/getbest')
def get_best():
	stat = get_best_for_each_num()
	return render_template('stat_table1.html', stat=stat)