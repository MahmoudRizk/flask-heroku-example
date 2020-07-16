"""Flask App Project."""

from flask import Flask, jsonify, redirect, url_for
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """Return homepage."""
    json_data = {'Hello': 'World!'}
    return jsonify(json_data)
    # return redirect('page')

if __name__ == '__main__':
    app.run()
