from flask import flask

app = flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
    
@app.route('/login',methods = ['GET','POST'])
def login();
    error=None
    if request.method =='POST':
        Username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password'
            return 'login com sucesso'
        else:
            error = 'credenciais inválidas, tente novamente'
    return render_template('login,html', error=error)

if __name__ == '__main__' :
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
