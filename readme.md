# Secure File Sharing System – EZ-Lab Backend Assignment

- Name : Abhinav Rai
- Uni Roll : 2200290120003
- Superset ID : 6366471
- Email : abhinav.2226cs1165@kiet.edu

This project is a backend system for secure file sharing between Ops Users and Client Users.  
Built with **Django**, **Django REST Framework**, and **JWT authentication**.

---

## Features Implemented

- **Custom User Model** with two types:  
  - `ops` (can upload files)  
  - `client` (can register, verify email, login, download/list files)
- **Client User Signup:**  
  - `/api/client/signup/`  
  - Registers client user and returns an encrypted email verification URL.
- **Email Verification:**  
  - `/api/client/verify-email/?token=...`  
  - Activates client user account after clicking the link.
- **JWT Login for Client User:**  
  - `/api/client/login/`  
  - Returns JWT access and refresh tokens for verified users.
- **File Upload for Ops User:**  
  - `/api/ops/upload/`  
  - Only Ops Users can upload `.pptx`, `.docx`, `.xlsx` files (with file type validation).

---

## API Endpoints (So Far)

| Endpoint                       | Method | Description                                        | Auth Required |
|---------------------------------|--------|----------------------------------------------------|---------------|
| `/api/client/signup/`           | POST   | Client user signup (returns email verify link)      | No            |
| `/api/client/verify-email/`     | GET    | Verify email for client user (via encrypted link)   | No            |
| `/api/client/login/`            | POST   | JWT login for client users (returns tokens)         | No            |
| `/api/ops/upload/`              | POST   | Upload file (ops users only, validated types)       | Yes (ops)     |

---

## How to Run Locally

1. **Clone the repo and install dependencies:**
    ```bash
    git clone <repo-url>
    cd <project-folder>
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
2. **Apply migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
3. **Create a superuser (for admin):**
    ```bash
    python manage.py createsuperuser
    ```
4. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

---

## Testing Endpoints

- Use [Postman](https://www.postman.com/) to test all API endpoints.
- For JWT-protected endpoints, use the access token in the `Authorization: Bearer <token>` header.
- Email verification: Use the `verify_url` returned from signup and paste in your browser or GET request.

---

## What’s Next?

- Client user: list all files, download files via secure URL.
- Ops user: login endpoint.
- Encrypted download links and file access security.
- Test cases for endpoints.
- Deployment plan.

---

## Author

- Abhinav Rai
- abhinavrai966@gmail.com

---
## Thank You