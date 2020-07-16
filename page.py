from flask import Blueprint, render_template, abort

page_blueprint = Blueprint('page', __name__, template_folder='templates')

@page_blueprint.route('/page', methods=['GET'])
def page():
    return "page"
