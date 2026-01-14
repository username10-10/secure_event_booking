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
2. Create a virtual environment: python -m venv venv
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

### Admin Section

1. Create New Event interface on the Admin page
![WhatsApp Image 2026-01-03 at 1 30 17 AM](https://github.com/user-attachments/assets/87836928-9cc0-4c1a-b878-443a4e5a03a9)

2. List of events interface on the Admin page
![WhatsApp Image 2026-01-03 at 1 30 17 AM (1)](https://github.com/user-attachments/assets/6ee26bff-81b7-48af-846d-9597590bb7bd)

3. Booking interface on the Admin page
![WhatsApp Image 2026-01-03 at 1 30 18 AM](https://github.com/user-attachments/assets/010a9b9d-65c7-47ea-8e98-aa46d639245a)

4. Profile Admin interface
![WhatsApp Image 2026-01-03 at 1 30 18 AM (1)](https://github.com/user-attachments/assets/ce5aba6f-4c31-4b63-aa79-94a6b58b4631)

5. Click on admin it will send to django interface
![WhatsApp Image 2026-01-03 at 1 30 18 AM (2)](https://github.com/user-attachments/assets/ccd104b6-50d7-4cb7-b2ad-7d8951548478)

6. Admin Audit Logs
![WhatsApp Image 2026-01-03 at 1 30 18 AM (3)](https://github.com/user-attachments/assets/21b0f18c-75e7-4660-9b3b-af29a75ef494)

7. Admin Users
<img width="1600" height="550" alt="image" src="https://github.com/user-attachments/assets/8d06edbd-2678-4dc4-9cfc-02b418974242" />

8. Admin Bookings
<img width="1600" height="579" alt="image" src="https://github.com/user-attachments/assets/65667186-d5b1-48ca-8b47-5ab24fc408f9" />

9. Admin Events
<img width="1600" height="618" alt="image" src="https://github.com/user-attachments/assets/6d6930e0-c3fc-4fd5-9e37-e9f4c7743afb" />

10. All the booking only admin can review
<img width="1600" height="537" alt="image" src="https://github.com/user-attachments/assets/64568930-1022-4e6c-b997-71baf0a60e1f" />

11. Admin cancel booking for user iqbal (example)
<img width="1600" height="685" alt="image" src="https://github.com/user-attachments/assets/92327eec-e6d6-4e5f-8532-54f4f1d076f1" />

12. Audit log that only admin can access
<img width="1600" height="490" alt="image" src="https://github.com/user-attachments/assets/1416ea07-cda3-444a-9db8-51d04b2b7799" />

### User Section 

1. User registration

![WhatsApp Image 2026-01-03 at 1 30 45 AM (1)](https://github.com/user-attachments/assets/39340c22-9904-4add-a16a-a57fbdb21564)

2. Login page
<img width="1600" height="513" alt="image" src="https://github.com/user-attachments/assets/b3ba6d8a-cefd-4c37-9215-f426934dcffd" />

3. Two-factor authentication
![WhatsApp Image 2026-01-14 at 22 16 10](https://github.com/user-attachments/assets/39ccb86d-e280-4b45-977c-d3d3023d5e21)
![WhatsApp Image 2026-01-14 at 22 16 21](https://github.com/user-attachments/assets/28a65e00-bb98-4de2-8763-49a028bab076)
![WhatsApp Image 2026-01-14 at 22 18 54](https://github.com/user-attachments/assets/fbd45f87-ab71-49e9-919f-9a023feef0ff)
![WhatsApp Image 2026-01-14 at 22 19 06](https://github.com/user-attachments/assets/a758704b-4f0b-410c-9398-2a2dbd9edabc)
![WhatsApp Image 2026-01-14 at 22 19 23](https://github.com/user-attachments/assets/3778396d-b7b4-4a6a-8ad8-109a97a2452b)
If the user click to disable the two-factor authentication as above, then the interface will prompt back into the second picture which have
QR code.

![WhatsApp Image 2026-01-14 at 22 20 19](https://github.com/user-attachments/assets/4758c1fa-f4e9-47ee-8c75-118be8ae6cbf)
These are the backup tokens that can be used for emergency purposes. Each backup token can be used once. New tokens can be 
regenerated if all backup tokens have been used.

![WhatsApp Image 2026-01-14 at 22 21 15](https://github.com/user-attachments/assets/8e8bc6bc-f40d-45ca-af8d-4759ba001913)
Users can login as usual if the two-factor authentication is successfully set up.

![WhatsApp Image 2026-01-14 at 22 21 42](https://github.com/user-attachments/assets/b85727c9-be7e-4359-bf1c-de85a5a271bc)
User can choose either want to use token from token generator or backup tokens.

![WhatsApp Image 2026-01-14 at 22 22 12](https://github.com/user-attachments/assets/05595809-b7e0-4027-9aa4-3d4d76e7accb)
Above interface if user click on use backup tokens.

![WhatsApp Image 2026-01-14 at 22 24 10](https://github.com/user-attachments/assets/f1de21e9-8626-4b7d-94d4-ce01a28b4470)
User actually can use the authenticator app through phone instead of using backup tokens.

![WhatsApp Image 2026-01-14 at 22 26 28](https://github.com/user-attachments/assets/0c98dc16-a184-46ab-9d4c-aaa17c616b6b)
Above is the interface dashboard from admin-side.

5. Input credential user
<img width="1600" height="467" alt="image" src="https://github.com/user-attachments/assets/bee46a95-4cc4-4c8e-bc21-8661894bbb32" />

6. Upcoming events interface 
<img width="1600" height="732" alt="image" src="https://github.com/user-attachments/assets/74ca6571-4304-4854-b4a8-6fddf4120417" />

7. Booking for user
<img width="1600" height="492" alt="image" src="https://github.com/user-attachments/assets/c9846471-ebea-4ee2-ba6c-f251c6092f27" />

8. Seat will reduce when users book the event
![WhatsApp Image 2026-01-03 at 1 30 46 AM (1)](https://github.com/user-attachments/assets/0698e762-ee31-45da-8ec1-35f937591d3e)

9. List of booking that user made
<img width="1600" height="625" alt="image" src="https://github.com/user-attachments/assets/f9f50d4c-57ad-4e08-bd87-4c15097fdfb8" />

10. Profie user
<img width="1600" height="674" alt="image" src="https://github.com/user-attachments/assets/e29c7a2e-7dbb-46b6-b252-9bd16bd7cf9f" />

