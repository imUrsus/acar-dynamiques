from flask import Flask, render_template, request, redirect, url_for, session,flash, current_app,jsonify
# on importe le contenu du dossier routes 
from .. import routes

# Récupérer le chemin du répertoire principal du projet
import os,sys,time,time
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_path)

from fonctions.chrono import *

def init_donnees():
    if 'donnees' not in current_app.config:
        current_app.config['donnees'] = [
         {'id': 1 , 'label':'Absence de pouls','slide':1,'dateheure':'', 'accomplie': 0},
        {'id': 2 , 'label':'Effondrement de la capnie','slide':1 ,'dateheure':'', 'accomplie': 0},
        {'id': 3 , 'label':'Commencer massage cardiaque','slide':2 ,  'dateheure':'', 'accomplie': 0},
        {'id': 4 , 'label':'IOT ou masque laryngé','slide':3 , 'dateheure':'', 'accomplie': 0},
        {'id': 5 , 'label':'Mettre Fi O2 100 %','slide':3 , 'dateheure':'', 'accomplie': 0},
        {'id': 6 , 'label':'Couper gaz anesthésie','slide':3 , 'dateheure':'', 'accomplie': 0},
        {'id': 7 , 'label':' KTIO si pas de VVP','slide':3 , 'dateheure':'', 'accomplie': 0},
        {'id': 8 , 'label':' Faire venir DSA','slide':4 , 'dateheure':'', 'accomplie': 0},
        {'id': 9 , 'label':' Sortir l’ Adrénaline','slide':4 , 'dateheure':'', 'accomplie': 0},
        {'id': 10 , 'label':' Faire venir l’amiodarone ( 3 ampoules)','slide':4 , 'dateheure':'', 'accomplie': 0},
        {'id': 11 , 'label':' Mettre en place DSA / DAE','slide':4 , 'dateheure':'', 'accomplie': 0}
        
        ]
    if 'sabliers' not in current_app.config:
        current_app.config['sabliers'] = [
            {'id' : 3 , 'sablier':sablier(60),'temps_restant':'','isRunning':'false' },
        ]
        
    if 'chrono_general' not in current_app.config:
        current_app.config['chrono_general'] = chrono()
        current_app.config['chrono_general'].demarrer()



        


# Vérifiez si c'est la première demande avant chaque demande
@routes.before_request
def before_request():
    init_donnees()
    


@routes.route("/acar1_1")
def f_acar1_1():
    valeur_chrono_general = current_app.config['chrono_general'].donner_chrono()
    donnees = current_app.config['donnees']
    sabliers= [{'id': sablier['id'],'temps_restant':sablier['temps_restant'], 'isRunning' : sablier['isRunning']} for sablier in current_app.config['sabliers']]

    return render_template("acar1/acar1_1.html",valeur_chrono_general=valeur_chrono_general,
                                            donnees = donnees,
                                            sabliers = sabliers
                                            )
                                        


@routes.route('/modifier/<int:tache_id>', methods=['POST'])
def modifier(tache_id):
    L_taches = [d for d in current_app.config['donnees'] if d['id'] == tache_id]
    tache_en_cours = L_taches[0] if L_taches else None

    if tache_en_cours:
        tache_en_cours['accomplie'] = 1 - tache_en_cours['accomplie']
    
    for sablier in  current_app.config['sabliers']:
        
        if sablier['id']==tache_id :
            sablier['sablier'].demarrer()
            sablier['isRunning']='true'
            sablier['temps_restant']=sablier['sablier'].donner_temps_restant()
    sabliers= [{'id': sablier['id'],'temps_restant':sablier['temps_restant'], 'isRunning' : sablier['isRunning']} for sablier in current_app.config['sabliers']]

    return jsonify({'donnees': current_app.config['donnees'],'sabliers':sabliers})


@routes.route('/maj')
def maj():

    for sablier in  current_app.config['sabliers']:
        if sablier['isRunning']=='true':
            sablier['temps_restant']=sablier['sablier'].donner_temps_restant()
    sabliers= [{'id': sablier['id'],'temps_restant':sablier['temps_restant'], 'isRunning' : sablier['isRunning']} for sablier in current_app.config['sabliers']]
    print(current_app.config['donnees'])
    return jsonify({'donnees': current_app.config['donnees'],'sabliers':sabliers})


@routes.route("/maj_chrono_general")
def maj_chrono_general():
    valeur_chrono_general = current_app.config['chrono_general'].donner_chrono()
    return jsonify({'valeur_chrono_general':valeur_chrono_general})

