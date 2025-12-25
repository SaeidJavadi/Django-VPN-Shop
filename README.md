# 🛡️ VPN Shop - Sample Online Store

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-green?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-orange)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/SaeidJavadi/Django-VPN-Shop?style=social)](https://github.com/SaeidJavadi/Django-VPN-Shop/stargazers)

VPN Shop is a **sample online store** built to sell VPN subscriptions.  
It is powered by **Django 4.2** and features a modern **frontend**, robust **backend**, and a **REST API** for programmatic access.

🎥 **Demo Video**:

https://github.com/user-attachments/assets/67cade8b-29fc-474e-931b-371d08eb6f72

---

## 🌟 Features

- **User Accounts**: Registration, login, password reset, profile management.
- **Admin Dashboard**: Enhanced admin panel with user and content management.
- **Product Management**: CRUD operations for VPN subscription products.
- **Media & Static Management**: Efficient handling of static and media files.
- **Payment Gateway**: Sandbox integration for testing payments.
- **Multilingual Support**: English & Persian.
- **Custom Pages & Templates**: Full control over page layouts.
- **Security**: Password validation and basic security best practices.

---

## 🗂️ Project Structure

```
backend/
├── accounts/       # User authentication
├── api/            # REST API endpoints
├── vpn/            # Products, orders, pages
├── payment/        # Payment integration
├── templates/      # HTML templates
├── static/         # CSS, JS, images
├── media/          # Uploaded media
├── manage.py       # Django management
└── vpnShop/        # Project config (settings, urls, wsgi)
docker/             # Docker dev & production configs
requirements.txt    # Python dependencies
```

---

## ⚡ Getting Started (Without Docker)

Follow these steps to run the project locally:

### Prerequisites

- Python **3.12**
- pip (Python package manager)
- Virtual environment (recommended)
- SQLite3 (default for development)

### Setup

1️⃣ **Clone the repository**

```bash
git clone https://github.com/SaeidJavadi/Django-VPN-Shop.git
cd Django-VPN-Shop/backend
```

2️⃣ **Create and activate a virtual environment**

```bash
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
```

3️⃣ **Install dependencies**

```bash
pip install --upgrade pip
pip install -r ../requirements.txt
```

4️⃣ **Configure environment variables**

Rename `.env.example` → `.env` and update your credentials:

```env
SECRET_KEY='your-secret-key'
DEBUG=True
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='your-email@example.com'
EMAIL_HOST_PASSWORD='your-email-password'
POSTGRES_DB='your_database_name'
POSTGRES_USER='your_database_user'
POSTGRES_PASSWORD='your_database_password'
POSTGRES_HOST='db'
POSTGRES_PORT=5432
```

5️⃣ **Run migrations**

```bash
python manage.py migrate
```

6️⃣ **Create a superuser**

```bash
python manage.py createsuperuser
```

7️⃣ **Start the development server**

```bash
python manage.py runserver
```

8️⃣ **Access the application**

- Frontend: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`

---

## 🔧 Notes

- Static files served automatically in **development**.
- REST API available under `/api/`.
- Uploaded media stored in `media/`.

> ✅ This setup allows even beginners to run VPN Shop locally. For **production**, consider Docker + Nginx + Gunicorn.

---

## 🚀 Live Demo

[Check the live demo here](https://dvs.sjpy.ir)

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
