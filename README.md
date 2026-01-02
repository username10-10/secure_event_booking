# Secure Event Booking System

## Project Description
The Secure Event Booking System was developed using the Django web application framework and is built on a microservices architecture. 
The core purpose of this web application is to provide a secure environment for people to create accounts, sign into the application, 
and manage their event reservations according to established OWASP Top Ten and ASVS Security Standards. With a primary focus on preventing 
vulnerable attacks such as SQL injection, cross-site scripting (XSS), and unapproved access, the Secure Event Booking System implements a 
strong security-first design.

## Security Features Summary
Injection Prevention: Utilizing a Django ORM to create SQL queries with parameters that cannot be modified or injected into.
Authetication and Identity: Providing Password Hashing and Secure Sessions using PBKDF2 as defined in the Django authentication package.
Access Control: Enforces Role-Based Access Control (RBAC) to restrict the Audit Log and administrative functions to authorized "Staff" users only.
Cross-Site Protection: Enforcing CSRF Tokens on every state change request and providing automated HTML escaping to mitigate XSS (Cross Site Scripting).
Logging and Audit: Utilizing a Custom Security Audit Module to keep track of all failed login attempts and system administrator security events.


## Installation Steps
1. Clone the repoitory: git clone https://github.com/username10-10/secure_event_booking
2. Create a virtual environment: python --m venv venv
3. Activate the environment:
   Windows: venv\Scripts\activate
   Mac/Linux: source venv/bin/activate
4. Install required packages: pip install -r requirements.txt

## How to Run the App
1. Configure environment: Create a .env file based on .env.example and next add
   your secret keys.
2. Apply Migrations: python manage.py migrate
3. Create Admin User: python manage.py createsuperuser
4. Launch Server: python manage.py runserver
5. Access the App: Open the browser and then navigate to http://127.0.0.1:8000

## Dependencies
Django 4.2+: Core web framework.
Python-dotenv: Secure environment variable management.
Pillow: Image processing for user profiles.
Bandit: Static Analysis Security Testing (SAST).

## Screenshots of System
