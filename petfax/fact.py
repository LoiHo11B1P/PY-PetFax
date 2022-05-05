from flask import ( Blueprint, render_template )

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/new')
def newFact():

    return render_template('factForm.html')