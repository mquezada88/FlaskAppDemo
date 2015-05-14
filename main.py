from flask import Flask
from coreapp import appapp.
app = Flask(__name__)

debug = True
if __name__ == '__main__':
    app.run()
