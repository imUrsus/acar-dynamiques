from flask import Flask, render_template, request, redirect, url_for, session,flash,jsonify, current_app
# on importe le contenu du dossier routes 
from .. import routes
#from ...fonctions.chrono import *
import sys
import os

# Récupérer le chemin du répertoire principal du projet
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_path)

from fonctions.chrono import *


@routes.route("/acar1_2")
def f_acar1_2():
    valeur_chrono_general = current_app.config['chrono_general'].donner_chrono()
    donnees = current_app.config['donnees']
    sabliers= [{'id': sablier['id'],'temps_restant':sablier['temps_restant'], 'isRunning' : sablier['isRunning']} for sablier in current_app.config['sabliers']]

    return render_template("acar1/acar1_2.html",valeur_chrono_general=valeur_chrono_general,
                                            donnees = donnees,
                                            sabliers = sabliers
                                            )
                                        
