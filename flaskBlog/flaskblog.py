from flask import Flask, render_template, url_for
import forms

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b8d2014c61758126a3f44d91c9962fe7'
posts = [
    {
        'author': 'corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2023'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2023'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = forms.RegistrationForm()
    return render_template('register.html', title='Register', form= form)

@app.route("/login")
def login():
    form = forms.LoginForm()
    return render_template('login.html', title='Login', form= form)


if __name__ == '__main__':
    app.run(debug=True)