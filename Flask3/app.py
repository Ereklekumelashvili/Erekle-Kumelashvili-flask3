from flask import Flask,render_template,request,redirect,url_for,session
from datetime import timedelta


app=Flask(__name__)
app.secret_key = 'Erekle'
app.permanent_session_lifetime = timedelta(minutes=5)




@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        name = request.form["text"]
        email = request.form['email']
        password = request.form['password']
        session['name'] = name
        session['email'] = email
        session['password'] = password
        return redirect(url_for('user'))
    else:
        if 'user' in session:
            return redirect(url_for('user',login='name' in session))
    return render_template('login.html')

@app.route('/user')
def user():
    if 'name' in session:
        name = session['name']
        return f'<h1>{name}</h1>'
    else:
        redirect(url_for('login'))

@app.route('/logout')
def logout():
        session.pop('name',None)
        session.pop('email',None)
        session.pop('password',None)
        return redirect(url_for('login'))


if __name__=='__main__':
    app.run(debug=True)