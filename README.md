# Secure Event Booking Project

## Setup
1. Clone the repo
2. Create a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and set variables
5. Run migrations: `python manage.py migrate`
6. Run server: `python manage.py runserver`

## Features
- User registration & login
- Role-based access control
- Event booking system
- Admin audit log

## Security
- OWASP Top 10 controls
- Input validation, XSS/SQLi prevention
- Secure password storage (bcrypt)
- CSRF protection enabled
