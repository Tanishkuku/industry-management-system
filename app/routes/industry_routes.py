from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Industry
from app import db

industry_bp = Blueprint('industry', __name__, url_prefix='/industries')

@industry_bp.route('/', methods=['GET', 'POST'])
def manage_industries():
    if request.method == 'POST':
        name = request.form.get('name')
        folder = f"{name}_data"
        new_industry = Industry(name=name, folder=folder)
        db.session.add(new_industry)
        db.session.commit()
        flash('Industry created successfully!', 'success')
        return redirect(url_for('industry.manage_industries'))
    industries = Industry.query.all()
    return render_template('industries.html', industries=industries)
