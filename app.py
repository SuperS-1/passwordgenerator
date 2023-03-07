import random

from flask import *
app = Flask(__name__)


@app.route('/l', methods=['POST'])
def gen():
    char = list('abcdefghijklmopqrstuvwxyz')
    if request.form.get('uppercase'):
        char.extend((list('ABCDEFGHILKLMNOPQRSTUVWXYZ')))
    if request.form.get('special'):
        char.extend((list('!@#$%^&*()~')))
    if request.form.get('numbers'):
        char.extend((list('1234567890')))
    l = int(request.form['length'])
    thepass = ""
    for i in range(l):
        thepass += random.choice(char)
    return render_template('password.html', da=thepass)


if __name__ == '__main__':
    app.run(debug=True)
