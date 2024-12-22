from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Item, Industry
from app import db

item_bp = Blueprint('item', __name__, url_prefix='/items')

@item_bp.route('/', methods=['GET', 'POST'])
def manage_items():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        industry_id = request.form.get('industry_id')
        new_item = Item(name=name, description=description, price=price, industry_id=industry_id)
        db.session.add(new_item)
        db.session.commit()
        flash('Item created successfully!', 'success')
        return redirect(url_for('item.manage_items'))
    items = Item.query.all()
    industries = Industry.query.all()
    return render_template('items.html', items=items, industries=industries)
