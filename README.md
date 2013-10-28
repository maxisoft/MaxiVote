MaxiVote
========
![MaxiVote Logo](https://lh5.googleusercontent.com/-UCsFbB2UaFA/UcmeY77sbkI/AAAAAAAAAIo/h7nw8W8ZHWQ/s144/Vote.png)

Base d'un bot de vote écrit en [python](http://www.python.org/).

Fonctionne a l'aide de plugins, dont la liste est disponible [ici](https://bitbucket.org/maxivote-plugin).

## Voici les sites supportés : ##
	Ad Vitam Aeternam
	Earthquake
	Millenium
	Molten
	Nostalgeek
	Gameminer (a venir)
    

## Installation Windows: ##

  + [Télécharger](https://bitbucket.org/maxisoft/maxivote/downloads/V2.zip)
  + Extraire dans un dossier où installer (typiquement Mes documents)
  + Lancer `MaxiVote.exe`

## Installation Unix: ##

  + Avoir les dépendances suivantes :
    * git 
    * python-dev 
    * python-pip

  + Lancer la commande suivante :
  <br/>
    `pip install cherrypy storm mercurial pycrypto`

  + Se placer dans le dossier où installer (typiquement ~)
  + Lancer :
    * `git clone https://github.com/maxisoft/MaxiVote.git`
    * `cd MaxiVote`
    * `chmod 755 linux_clean.sh`
    * `./linux_clean.sh`
  + Et enfin lancer le bot :
  <br/>
    `python -O3 main.py`


## Configuration ##

une fois installé , ce Bot se configure simplement a l'aide d'un navigateur a l'adresse locale suivante: [127.0.0.1:9645/](http://127.0.0.1:9645/)
