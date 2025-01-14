from flask import Flask

app = Flask(__name__)

# Additional route accepting a parameter
@app.route('/<name>')
def hello_name(name):
    return 'Hello %s!' % name

# Route for the root URL
@app.route('/')
def hello_world():
    return 'Hello World'

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host='0.0.0.0', port=5000, debug=True)
