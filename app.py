from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

def hash_sha1(data):
    return hashlib.sha1(data.encode()).hexdigest()

def hash_shake_128(data, length=32):
    shake = hashlib.shake_128(data.encode())
    return shake.hexdigest(length)

@app.route('/', methods=['GET', 'POST'])
def index():
    hashed_value = ""
    if request.method == 'POST':
        text = request.form['text']
        algorithm = request.form['algorithm']
        
        if algorithm == 'sha1':
            hashed_value = hash_sha1(text)
        elif algorithm == 'shake_128':
            length = int(request.form.get('length', 32))
            hashed_value = hash_shake_128(text, length)

    return render_template('index.html', hashed_value=hashed_value)

if __name__ == '__main__':
    app.run(debug=True)