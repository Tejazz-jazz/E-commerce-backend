# 🛍️ E-commerce Backend (Django REST API)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-5.0-green)
![DRF](https://img.shields.io/badge/DRF-REST--Framework-red)

This is a simple **E-commerce backend** built using Django REST Framework.  
It includes user authentication, product management, cart management, and order placement features.

---

## ⚙️ Features

- 👤 User Registration & Login (JWT Authentication)
- 🛒 Add / Remove Products from Cart
- 📦 Place and View Orders
- 🧾 Product CRUD (Create, Read, Update, Delete)
- 🔐 Secure Authentication System
- ⚙️ Admin Panel to Manage Everything

---

## 🧠 Tech Stack

- **Python 3**
- **Django 5**
- **Django REST Framework (DRF)**
- **SQLite** (default database)
- **Postman** for API testing

---

## 💻 How to Run Locally

```bash
git clone https://github.com/Tejazz-jazz/E-commerce-backend.git
cd E-commerce-backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
