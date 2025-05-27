from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ""
    if request.method == 'POST':
        length = int(request.form.get('length'))
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation
        all_chars = lower + upper + digits + symbols

        # Generate password
        password = ''.join(random.sample(all_chars, length))

    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
