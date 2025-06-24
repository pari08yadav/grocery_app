# 🛒 Grocery Store Management System

A web-based **Grocery App** built using **Python Django** and **HTML templates**. This project allows users to add grocery items to the inventory and buy items directly from the interface — simulating a basic grocery store workflow.

---

## 📌 Project Overview

This system enables users to:

- ➕ Add grocery items (name, quantity, price)
- 📋 View all available grocery items
- 🛍️ Buy items by selecting quantity
- 💸 Automatically calculate total cost
- 🔄 Update item stock after each purchase
- 🚫 Prevent purchase if stock is insufficient
- 🧾 Generate a simple order summary

---

## 🛠️ Tech Stack

- **Backend**: Python Django
- **Frontend**: Django templates (HTML, CSS, JS)
- **Database**: SQLite (default)

---

## ✅ Key Features

- Add items to the grocery inventory
- Display a dynamic table of all items with current stock and price
- Buy selected items with quantity input
- Auto-update stock after each successful purchase
- Prevent over-buying if stock is insufficient
- Simple checkout summary with total amount

---

## 🧪 Project Setup

### 📥 Clone the Repository


# (Optional) Create virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Run the development server
python manage.py runserver


```bash
git clone https://github.com/yourusername/grocery_app.git
cd grocery_app
