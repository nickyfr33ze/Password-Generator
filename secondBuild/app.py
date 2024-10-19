from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length=16, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(length))

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ""
    if request.method == 'POST':
        password = generate_password()
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)