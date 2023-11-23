from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = [
    {"username": "jani1002", "password": "password1"},
    {"username": "rohit123", "password": "password2"},
    {"username": "anil1342", "password": "password3"},
    {"username": "ravi1235", "password": "password4"},
]

    
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = next((u for u in users if u["username"] == username and u["password"] == password), None)
        if user:
            return redirect(url_for('login_page'))
        else:
            # You can handle invalid login here
            return "Invalid login credentials. Please try again."
    return redirect('home page.html')
    return render_template('home page.html')



@app.route('/loginpage')
def login_page():
    return redirect('home page')
    return render_template('loginpage.html')

@app.route('/home page')
def home_page():
    return redirect('stocks present')
    return render_template('home page.html')

@app.route('/stocks_present')
def stocks_present():
    return redirect('portfolio')
    return render_template('stocks present.html')

@app.route('/portfolio')
def portfolio():
    return redirect('news')
    return render_template('portfolio.html')

@app.route('/news')
def news():
    return redirect('contact')
    return render_template('news.html')

@app.route('/contact')
def contact():
    return redirect('home page')
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)