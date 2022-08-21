from flask import Blueprint, render_template
from app.models import Recent

bp = Blueprint('product', __name__, url_prefix='/product')

@bp.route('/list/')
def _list():
    weight_list = Recent.query.order_by(Recent.create_time.desc())
    return render_template('weight/weight_list.html', weight_list=weight_list)


@bp.route('/detail/<int:product_id>/')
def detail(product_id):
    weight = Recent.query.get_or_404(product_id)
    return render_template('weight/weight_detail.html', weight=weight)