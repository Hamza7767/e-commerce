# ShopEasy - Simple E-commerce Website

A full-featured e-commerce web application built with **Python**, **Flask**, and **Bootstrap 5**.

## Features

### Customer Features
- **Home page** with featured products and category browsing
- **Product catalog** with search, category filter, and sorting
- **Product detail** pages with add-to-cart
- **User registration & login**
- **Shopping cart** (add, update quantity, remove items)
- **Checkout** with shipping information
- **Order history** and order detail pages
- **User profile** page

### Admin Features
- **Dashboard** with stats (products, orders, pending orders)
- **Product management** (add, edit, delete products)
- **Category management** (add, delete categories)
- **Order management** (view orders, update status)

## Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Seed the database

```bash
python seed.py
```

This creates sample products, categories, and demo accounts:

| Role  | Username | Password  |
|-------|----------|-----------|
| Admin | admin    | admin123  |
| User  | demo     | demo123   |

### 3. Run the application

```bash
python app.py
```

Open **http://localhost:5000** in your browser.

## Project Structure

```
e-commerce/
├── app.py              # Application entry point
├── config.py           # Configuration settings
├── models.py           # Database models
├── extensions.py       # Flask extensions
├── seed.py             # Database seed script
├── requirements.txt    # Python dependencies
├── routes/
│   ├── auth.py         # Login, register, profile
│   ├── shop.py         # Home, products, product detail
│   ├── cart.py         # Shopping cart
│   ├── orders.py       # Checkout and orders
│   └── admin.py        # Admin panel
├── templates/          # HTML templates
└── static/css/         # Custom styles
```

## Tech Stack

- **Backend:** Python 3, Flask, Flask-SQLAlchemy, Flask-Login
- **Database:** SQLite
- **Frontend:** Bootstrap 5, Bootstrap Icons

## Order Status Flow

`pending` → `processing` → `shipped` → `delivered`

Orders can also be set to `cancelled` by an admin.
