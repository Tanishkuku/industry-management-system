from flask import Blueprint, render_template
from app.models import Industry, Storage, Item, Expense, Trade, Transact, Inventory

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard_bp.route('/')
def overview():
    industries = Industry.query.all()
    storages = Storage.query.all()
    items = Item.query.all()
    expenses = Expense.query.all()
    trades = Trade.query.all()
    transacts = Transact.query.all()
    inventory = Inventory.query.all()
    return render_template(
        'dashboard.html',
        industries=industries,
        storages=storages,
        items=items,
        expenses=expenses,
        trades=trades,
        transacts=transacts,
        inventory=inventory
    )
