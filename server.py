from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'TOPSECRET' 


@app.route('/')
def homePage():
    return render_template('index.html')


@app.route('/results', methods=['POST'])
def results():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')





if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port = 5005)