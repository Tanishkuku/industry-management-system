from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Inventory
from app import db

inventory_bp = Blueprint('inventory', __name__, url_prefix='/inventory')

@inventory_bp.route('/', methods=['GET', 'POST'])
def manage_inventory():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        new_inventory = Inventory(title=title, description=description)
        db.session.add(new_inventory)
        db.session.commit()
        flash('Inventory item added successfully!', 'success')
        return redirect(url_for('inventory.manage_inventory'))
    inventory = Inventory.query.all()
    return render_template('inventory.html', inventory=inventory)
