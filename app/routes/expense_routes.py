from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Expense
from app import db

expense_bp = Blueprint('expense', __name__, url_prefix='/expenses')

@expense_bp.route('/', methods=['GET', 'POST'])
def manage_expenses():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        amount_inr = request.form.get('amount_inr')
        new_expense = Expense(title=title, description=description, amount_inr=amount_inr)
        db.session.add(new_expense)
        db.session.commit()
        flash('Expense recorded successfully!', 'success')
        return redirect(url_for('expense.manage_expenses'))
    expenses = Expense.query.all()
    return render_template('expenses.html', expenses=expenses)
