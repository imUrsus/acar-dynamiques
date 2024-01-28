from flask import Flask, render_template, request, redirect, url_for, session,flash,jsonify, current_app
# on importe le contenu du dossier routes 
from .. import routes


@routes.route("/acar1_3")


def f_acar1_3():
    valeur_chrono_general = current_app.config['chrono_general'].donner_chrono()
    temps_restant_s_massage = current_app.config['s_massage'].donner_temps_restant()
    s_massageRunning = current_app.config['s_massageRunning']
    s_injectionRunning = current_app.config['s_injectionRunning']
    temps_restant_s_injection = current_app.config['s_injection'].donner_temps_restant()
    donnees = current_app.config['donnees']
    return render_template("acar1/page2.html",valeur_chrono_general=valeur_chrono_general,
                                            temps_restant_s_massage=temps_restant_s_massage,
                                            s_massageRunning = s_massageRunning,
                                            temps_restant_s_injection=temps_restant_s_injection,
                                            s_injectionRunning = s_injectionRunning,
                                            donnees = donnees)
