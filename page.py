from .app import app

@app.route('/page')
def page():
    return "page"
