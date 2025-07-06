# Secure File Sharing System – EZ Labs Backend Assignment

- **Name:** Abhinav Rai  
- **Uni Roll:** 2200290120003  
- **Superset ID:** 6366471  
- **Email:** abhinav.2226cs1165@kiet.edu  

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
- **JWT Login for Both Users:**  
  - `/api/client/login/`  
    - Returns JWT access and refresh tokens for verified users.
- **File Upload for Ops User:**  
  - `/api/ops/upload/`  
    - Only Ops Users can upload `.pptx`, `.docx`, `.xlsx` files (with file type validation).
- **List Uploaded Files (Client):**  
  - `/api/client/files/`  
    - Client user can list all uploaded files.
- **Generate Secure Download Link (Client):**  
  - `/api/client/download-link/<file_id>/`  
    - Returns an encrypted link to download the file.
- **Secure File Download (Client Only):**  
  - `/api/client/download-file/?token=...`  
    - Only the correct client user can access and download the file with this secure link.

---

## API Endpoints

| Endpoint                                 | Method | Description                                               | Auth Required    |
|-------------------------------------------|--------|-----------------------------------------------------------|------------------|
| `/api/client/signup/`                     | POST   | Client user signup (returns email verify link)            | No               |
| `/api/client/verify-email/`               | GET    | Verify email for client user (via encrypted link)         | No               |
| `/api/client/login/`                      | POST   | JWT login for users (returns tokens)                      | No               |
| `/api/ops/upload/`                        | POST   | Upload file (ops users only, validated types)             | Yes (ops)        |
| `/api/client/files/`                      | GET    | List all uploaded files (client only)                     | Yes (client)     |
| `/api/client/download-link/<file_id>/`    | GET    | Get secure download link for a file (client only)         | Yes (client)     |
| `/api/client/download-file/?token=...`    | GET    | Download file securely via encrypted link (client only)   | Yes (client)     |

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

## How to Test

- Use [Postman](https://www.postman.com/) to test all API endpoints (see included Postman collection).
- For JWT-protected endpoints, use the access token in the `Authorization: Bearer <token>` header.
- Email verification: Use the `verify_url` returned from signup and paste in your browser or send a GET request.
- To download a file, first generate a download link as a client, then open the link in Postman using the client user's token.

---

## Deployment Notes

- For production, use **Gunicorn**/**uWSGI** behind **Nginx** or **Apache**.
- Store files in a cloud storage (e.g., AWS S3) instead of local disk.
- Set `DEBUG=False` and configure allowed hosts and secrets via environment variables.
- Recommended DB: **PostgreSQL** or **MySQL** (can switch from SQLite in settings).
- Use a task queue (like **Celery + Redis**) for sending email (bonus/advanced).
- Deploy on AWS EC2, Heroku, or any VPS with Docker.

---

## Postman Collection

- All major request flows are included in the exported Postman collection (`EZ_Labs.postman_collection.json`).

---

## Author

- **Abhinav Rai**
- [abhinav.2226cs1165@kiet.edu](mailto:abhinav.2226cs1165@kiet.edu)

---

## Thank You!

---

*Feel free to add or tweak sections (requirements.txt, contact info, etc.) as needed!*

---
