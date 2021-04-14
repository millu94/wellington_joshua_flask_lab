from flask import Flask

record_shop = Flask(__name__)

from controllers import controller

if __name__ == "__main__":
    record_shop.run(debug=True)