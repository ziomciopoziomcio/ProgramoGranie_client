from flask import Flask

# Global variables
server_port = 5000
app = Flask(__name__)


# Routes
@app.route('/')
def home():  # Home route
    return 'Hello, World!'


# Main
if __name__ == '__main__':
    app.run(debug=True, host='', port=server_port)
