from flask import Flask, request
from flask_cors import CORS  # Import CORS
import os

app = Flask(__name__)

# Enable CORS for the entire app
CORS(app)

# Accessing the environment variable using os.environ
bignum = os.environ.get('BIG_NUMBER')  # Make sure BIG_NUMBER is set in your environment

@app.route('/sdfgiygwfidkjsidaifhsdfihwe7yfkahsdjfkhsdfweuihfhsjaflsjdkfiwejfiwejf8738479823746237426345752', methods=['POST'])
def rwg():
    return str(bignum)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
