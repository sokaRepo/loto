#Loto Web App

###Dépendances

* Pip 

```bash
cd /tmp/
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
rm get-pip.py
```
* Flask python library

```bash
pip install flask # Framework application web en python
```

* Mysql
```
apt-get install mysql-server # serveur mysql à configurer
apt-get install python-dev libmysqlclient-dev # librairies requises pour la librairie MySQL-python
pip install MySQL-python # librairie MySQL pour python
```

* Requests
```
pip install requests # téléchargement de fichier
```

### Lancer l'application
```
export FLASK_APP=app.py
flask run
```
ou
```
python app.py
```

### Lancer l'application via Apache
Créer une nouvelle configuration dans /etc/apache2/sites-available/
```bash
vim /etc/apache2/sites-available/loto.conf
```
et changer la configuration comme suit:
```
<VirtualHost *:80>
    ServerName dashboard.toto.com
    ServerAdmin bob@toto.com
    WSGIScriptAlias / /var/www/toto.com/loto/loto.wsgi
    <Directory /var/www/toto.com/loto/>
            Order allow,deny
            Allow from all
    </Directory>
    Alias /static /var/www/toto.com/loto/static
    <Directory /var/www/toto.com/loto/static/>
            Order allow,deny
            Allow from all
    </Directory>
    ErrorLog ${APACHE_LOG_DIR}/error.log
    LogLevel warn
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

Dans le dossier de l'application loto créer un fichier loto.wsgi:
```python
import sys
sys.path.insert(0, '/var/www/toto.com/loto/')
from app import app as application
```

Dans le fichier utils.py changer la valeur de APP_PATH
```

### Caractéristiques
* Charger le dernier fichier ZIP loto sur https://www.fdj.fr/jeux/amigo/historiques
* Décompression du fichier ZIP afin d'avoir le fichier CSV
* Conversion du CSV en SQL
* Execution du fichier SQL
* Affichage des données de la base de données sous forme de tableau avec système de pagination
* Affichage des numéros qui sont le plus souvent tombés pour chaque tirage
* Site full Ajax pour un meilleur dynamisme
