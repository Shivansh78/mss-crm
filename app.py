from flask import Flask, render_template

app = Flask(__name__)

# Route to serve the HTML dashboard file
@app.route('/')
def index():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
