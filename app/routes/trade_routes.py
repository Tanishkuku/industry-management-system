from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Trade
from app import db

trade_bp = Blueprint('trade', __name__, url_prefix='/trades')

@trade_bp.route('/', methods=['GET', 'POST'])
def manage_trades():
    if request.method == 'POST':
        description = request.form.get('description')
        amount_inr = request.form.get('amount_inr')
        new_trade = Trade(description=description, amount_inr=amount_inr)
        db.session.add(new_trade)
        db.session.commit()
        flash('Trade recorded successfully!', 'success')
        return redirect(url_for('trade.manage_trades'))
    trades = Trade.query.all()
    return render_template('trades.html', trades=trades)
