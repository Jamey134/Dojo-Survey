from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'TOPSECRET' 


@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/results')
def resultsPage():
    return render_template('results.html')


@app.route('/results/form', methods=['POST'])
def results():
    print("Got Post Info")
    # Here we add two properties (key_values) to session to store the name and emailß
    session['userName'] = request.form['name']
    session['userLocation'] = request.form['location']
    session['userLanguage'] = request.form['language']
    session['userComment'] = request.form['comment']
    return redirect('/results')





if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port = 5005)