# Industry Management Software

## Project Description
This project is an industry management system that allows various roles (Head, Sub-Head, Trading-Subjects, Inventory-Subjects, Expense-Accounts) to perform specific CRUD operations with role-based access.

### Features:
- User Authentication (Login, Registration, Password Management)
- Role-Based Access Control
- Industry, Storage, Items, Trades, Transactions, Expenses, and Inventory Management
- Data Dashboard for Analysis
- File Uploads for Receipts and Supporting Documents
- Secure Authentication using Flask-Login and bcrypt

---

## Folder Structure
industry_management_software/
├── .env
├── config.py
├── migrations/
├── README.md
├── requirements.txt
├── run.py
├── app/
    ├── __init__.py
    ├── models.py
    ├── routes/
    │   ├── __init__.py
    │   ├── auth_routes.py
    │   ├── industry_routes.py
    │   ├── storage_routes.py
    │   ├── item_routes.py
    │   ├── expense_routes.py
    │   ├── trade_routes.py
    │   ├── transact_routes.py
    │   ├── inventory_routes.py
    │   ├── dashboard_routes.py
    ├── templates/
    │   ├── base.html
    │   ├── dashboard.html
    │   ├── industries.html
    │   ├── storages.html
    │   ├── items.html
    │   ├── expenses.html
    │   ├── trades.html
    │   ├── transacts.html
    │   ├── inventory.html
    │   ├── login.html
    │   ├── register.html
    ├── static/
        ├── styles.css
