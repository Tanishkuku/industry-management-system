from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Transact
from app import db

transact_bp = Blueprint('transact', __name__, url_prefix='/transacts')

@transact_bp.route('/', methods=['GET', 'POST'])
def manage_transacts():
    if request.method == 'POST':
        description = request.form.get('description')
        amount_inr = request.form.get('amount_inr')
        new_transact = Transact(description=description, amount_inr=amount_inr)
        db.session.add(new_transact)
        db.session.commit()
        flash('Transaction recorded successfully!', 'success')
        return redirect(url_for('transact.manage_transacts'))
    transacts = Transact.query.all()
    return render_template('transacts.html', transacts=transacts)
