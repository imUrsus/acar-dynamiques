# le fichier __init__.py permet l'import des fichiers contenus dans le dossier routes.
# on y indique les emplacements des fichiers que contient le dossier routes


from flask import Blueprint
routes = Blueprint('routes', __name__)



from .index import *
from .acar1.acar1_1 import *
from .acar1.acar1_2 import *
from .acar1.acar1_3 import *
from .acar2.acar2 import *





