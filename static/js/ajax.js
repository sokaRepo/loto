function load_loto_csv() {
	var error = false;
	$(".lead").text('');
	$(".lead").append('Téléchargement de l\'archive loto.zip ... ');
	$.get("/ajax/save-csv", function(data) {
		data = jQuery.parseJSON(data);
		if (data.status == 'ok') {
			$(".lead").append('✔<br>');
		}
		else if(data.status == 'running') {
			error = true;
			$(".lead").append('L \'application est déjà en cours d\'utilisation, merci de réessayer dans quelques secondes<br>');	
		}
		else {
			error = true;
			$(".lead").append('<br>Erreur pendant le chargement :( <br>')
		}

		if (!error) {
			$(".lead").append('Décompression du fichier loto.zip ... ');
			unzip_csv();
			
		}

	});

}

function unzip_csv() {
	var error = false;
	$.get("/ajax/unzip-csv", function(data) {
		data = jQuery.parseJSON(data);
		if (data.status == 'ok') {
			$(".lead").append('✔<br>');
		}
		else {
			error = true;
			$(".lead").append('<br>Erreur pendant la décompression :(<br>');	
		}
		if (!error) {
			$(".lead").append('Conversion CSV vers SQL ... ');
			csv_to_sql();
		}
	});
}


function csv_to_sql() {
	$.get("/ajax/csv-sql", function(data) {
		data = jQuery.parseJSON(data);
		if (data.status == 'ok') {
			$(".lead").append(data.n + ' lignes ont été écrites dans db.sql ✔<br>');
			$(".lead").append('Exécution du fichier db.sql ...');
			exec_sql();
		}
		else {
			$(".lead").append('<br>Erreur pendant l\'écriture du fichier db.sql :(<br>');	
		}
	});		
}

function exec_sql() {
	$.get("/ajax/exec-sql", function(data) {
		data = jQuery.parseJSON(data);
		if (data.status == 'ok') {
			$(".lead").append('✔<br>');
		}
		else {
			$(".lead").append('<br>Erreur pendant l\'écriture du fichier db.sql :(<br>');	
		}
	});	
}


function get_db_table(page) {
	$.get("/ajax/dbtable/"+page, function(data) {	
		$("#dbTable").html(data);
	});		
}

function get_best_for_stat() {
	$.get("/ajax/stat/getbest"+page, function(data) {	
		$("#firstTable").html(data);
	});			
}