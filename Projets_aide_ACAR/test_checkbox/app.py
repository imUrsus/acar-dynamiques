from flask import Flask, render_template, request

app = Flask(__name__)

# Dictionnaire pour stocker les états des questions

taches=[{'id': 1 , 'label':'lb1','libelle':'tache 1', 'dateheure':'', 'accomplie': False},
        {'id': 2 , 'label':'lb2','libelle':'tache 2', 'dateheure':'', 'accomplie': False},
        {'id': 3 , 'label':'lb3','libelle':'tache 3', 'dateheure':'', 'accomplie': False},
        {'id': 4 , 'label':'lb4','libelle':'tache 4', 'dateheure':'', 'accomplie': False},
        {'id': 5 , 'label':'lb5','libelle':'tache 5', 'dateheure':'', 'accomplie': False}
        ]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        # Met à jour l'état des questions en fonction des valeurs soumises
        for tache in taches:
            checkbox_value = request.form.get('name'+str(tache['id']))
            
            tache['accomplie'] = checkbox_value == 'on'
        print(taches)    

    # Rend le template avec les états actuels des questions
    return render_template('index.html', taches=taches)

# 
if __name__ == '__main__':
    app.run(debug=True)
