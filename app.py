from flask import Flask, render_template
from forms import RegisterForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY']='011d552f9bf6c46ba8b7379603e3c0b3'

@app.route("/")
@app.route("/home")
def hello_world():
    return render_template('home.html')
    

@app.route("/register")
def register():
    #creating an instance of our form
    form= RegisterForm()
    return render_template('register.html', title='Register', form=form) #to have access to the instance of the form

@app.route("/login")
def login():
    #creating an instance of our form
    form= LoginForm()
    return render_template('login.html', title='Register', form=form) #to have access to the instance of the form


@app.route("/upload")
def upload():
    return  render_template('upload.html')



if __name__=='__main__':
	app.run(debug=True)