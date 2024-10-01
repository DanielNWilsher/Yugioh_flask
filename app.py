from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="Yu-Gi-Oh", message="Is King of Games")

if __name__ == '__main__':
    app.run(debug=True)
