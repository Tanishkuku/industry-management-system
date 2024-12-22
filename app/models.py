from app import db, bcrypt
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # head, sub-head, etc.
    industry_id = db.Column(db.Integer, db.ForeignKey('industries.id'))
    last_active = db.Column(db.DateTime)
    user_folder = db.Column(db.String(255), nullable=True)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)


class Industry(db.Model):
    __tablename__ = "industries"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    folder = db.Column(db.String(255), nullable=False)


class Storage(db.Model):
    __tablename__ = "storages"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    address = db.Column(db.String(255), nullable=False)
    industry_id = db.Column(db.Integer, db.ForeignKey('industries.id'))


class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    industry_id = db.Column(db.Integer, db.ForeignKey('industries.id'))


class Expense(db.Model):
    __tablename__ = "expenses"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    amount_inr = db.Column(db.Float, nullable=False)
    uploaded_receipt = db.Column(db.String(255), nullable=True)


class Trade(db.Model):
    __tablename__ = "trades"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=True)
    amount_inr = db.Column(db.Float, nullable=False)
    uploaded_receipt = db.Column(db.String(255), nullable=True)


class Transact(db.Model):
    __tablename__ = "transacts"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=True)
    amount_inr = db.Column(db.Float, nullable=False)
    uploaded_receipt = db.Column(db.String(255), nullable=True)


class Inventory(db.Model):
    __tablename__ = "inventory"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    uploaded_receipt = db.Column(db.String(255), nullable=True)
