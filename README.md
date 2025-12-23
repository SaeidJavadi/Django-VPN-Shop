# VPN Shop - Sample Online Store

VPN Shop is a **sample online store** designed to sell VPN subscriptions.  
It is built with **Django 4.2** and includes modern features for both the **frontend** and **backend**, along with a **REST API** for programmatic access.

## Features

- **User Accounts**: Fully functional account system, including registration, login, password reset, and profile management.
- **Admin Dashboard**: Custom admin panel with enhanced user and content management capabilities.
- **Product Management**: Create, update, and delete VPN subscription products.
- **Media & Static Management**: Efficient handling of static files, images, and media uploads.
- **Payment Gateway Integration**: Sandbox integration for testing payments.
- **Multilingual Support**: English and Persian languages supported.
- **Custom Pages & Templates**: Full control over the look and structure of site pages.
- **Security Features**: Proper password validation and basic security measures implemented.

## Project Structure

```
backend/
├── accounts/       # User management and authentication
├── api/            # REST API endpoints
├── vpn/            # Main app (products, orders, pages)
├── payment/        # Payment gateway integration
├── templates/      # HTML templates
├── static/         # CSS, JS, images
├── media/          # Uploaded media
├── manage.py       # Django management script
└── vpnShop/        # Project configuration (settings, urls, wsgi)
docker/             # Docker development and production configurations
requirements.txt    # Python dependencies
```

## Getting Started (Without Docker)

If you want to run the project on your local machine **without Docker**, follow these simple steps:

### Prerequisites

- Python **3.12** installed
- pip (Python package manager)
- Virtual environment (recommended)
- SQLite3 (comes with Python, used by default in development)

### Setup Steps

#### 1. **Clone the project:**

```bash
git clone https://github.com/SaeidJavadi/Django-VPN-Shop.git
cd Django-VPN-Shop/backend
```

#### 2. **Create and activate a virtual environment:**

```bash
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
```

#### 3. **Install dependencies:**

```bash
pip install --upgrade pip
pip install -r ../requirements.txt
```

#### 4. **Set up environment variables:**

Rename the file `.env.example` to `.env` and set the following content with your own values:

```env
# Django settings
SECRET_KEY='your-secret-key'
DEBUG=True

# Email settings
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='your-email@example.com'
EMAIL_HOST_PASSWORD='your-email-password'

# PostgreSQL database settings
POSTGRES_DB='your_database_name'
POSTGRES_USER='your_database_user'
POSTGRES_PASSWORD='your_database_password'
POSTGRES_HOST='db'   # Name of the database service/container in docker-compose
POSTGRES_PORT=5432    # Database port inside the container
```

#### 5. **Run database migrations:**

```bash
python manage.py migrate
```

#### 6. **Create a superuser (for admin access):**

```bash
python manage.py createsuperuser
```

#### 7. **Run the development server:**

```bash
python manage.py runserver
```

#### 8. **Access the website:**

- Frontend: `http://127.0.0.1:8000/`
- Admin panel: `http://127.0.0.1:8000/admin/`

---

## Notes

- All static files are served automatically in **development mode**.
- The **REST API** is accessible under `/api/`.
- Media files are stored in the `media/` folder.

---

This setup allows anyone, even beginners, to run the VPN Shop locally for development or testing purposes **without Docker**.  
For production deployment, using Docker and a proper web server (like Nginx + Gunicorn) is recommended.

## Live Demo

🚀 Check out the live demo here:  
https://dvs.sjpy.ir
