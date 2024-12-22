from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Storage, Industry
from app import db

storage_bp = Blueprint('storage', __name__, url_prefix='/storages')

@storage_bp.route('/', methods=['GET', 'POST'])
def manage_storages():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        address = request.form.get('address')
        industry_id = request.form.get('industry_id')
        new_storage = Storage(name=name, description=description, address=address, industry_id=industry_id)
        db.session.add(new_storage)
        db.session.commit()
        flash('Storage created successfully!', 'success')
        return redirect(url_for('storage.manage_storages'))
    storages = Storage.query.all()
    industries = Industry.query.all()
    return render_template('storages.html', storages=storages, industries=industries)
