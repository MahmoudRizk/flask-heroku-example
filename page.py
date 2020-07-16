from .app import app

@app.route('/page', methods=['GET'])
def page():
    return "page"
