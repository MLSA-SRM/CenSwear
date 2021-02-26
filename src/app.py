from flask import Flask , render_template , request , redirect


app = Flask(__name__)

# app.config[''] = ''
# app.config[''] = ''

@app.route('/')
def index():
    return render_template('landingPage.html')

if __name__ == "__main__":
    app.run(debug=True)