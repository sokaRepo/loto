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