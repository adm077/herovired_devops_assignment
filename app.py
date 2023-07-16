from flask import Flask
app = Flask(__name__)

@app.route('/', method=['GET'])
def helloworld():
    return 'Hellow World'

if __name__ == "_main_":
    app.run(port=3000, debug=True)
    