# EduTrack (Initial Backend)

EduTrack is a modern, scalable **Student Data Management System** designed for both web and desktop applications. This repository contains the initial FastAPI backend skeleton powering EduTrack’s core features.

---

## 🚀 Features (Initial Version)

* FastAPI backend with RESTful API endpoints for:

  * User Authentication (Admin, Teacher, Student roles)
  * Student CRUD operations (Create, Read, Update, Delete)
* SQLAlchemy ORM models for database interactions (`User`, `Student`)
* Secure password hashing using **bcrypt** via Passlib
* SQLite database for easy local development (`data/edutrack.db`)
* Pydantic models for data validation
* Basic project structure enabling easy expansion (web frontend, desktop apps)

---

## 💻 Technology Stack

| Component         | Technology                 | Notes                                                |
| ----------------- | -------------------------- | ---------------------------------------------------- |
| Backend Framework | FastAPI                    | Modern, async, high-performance Python API framework |
| Database          | SQLite                     | Lightweight, file-based — easy for dev & testing     |
| ORM               | SQLAlchemy                 | Object-relational mapper for DB abstraction          |
| Password Hashing  | Passlib (bcrypt)           | Industry-standard for secure password hashing        |
| Data Validation   | Pydantic                   | Fast and easy data parsing & validation              |
| Frontend (future) | Bootstrap 5 / Tailwind CSS | Responsive UI frameworks for web frontend            |
| Desktop (future)  | PySide6 or CustomTkinter   | Desktop UI frameworks with Python support            |

---

## 📂 Project Structure

```
EduTrack/
│
├── backend/                   # Core backend API
│   ├── app.py                # FastAPI main app
│   ├── database.py           # Database connection setup
│   ├── models/               # SQLAlchemy models (User, Student, etc.)
│   ├── routes/               # API route handlers (auth, students, etc.)
│   ├── schemas/              # Pydantic data models
│   ├── utils/                # Utility modules (auth helpers, exports)
│   └── tests/                # Unit and integration tests
│
├── web/                      # Web frontend (optional)
│   ├── templates/            # Jinja2 HTML templates
│   ├── static/               # CSS, JS, images
│   └── views.py              # Web page routes
│
├── desktop/                  # Desktop app (optional)
│   ├── main.py               # Entry point for desktop app
│   ├── ui/                   # PySide6/Tkinter UI components
│   └── assets/               # Images, icons, resources
│
├── data/                     # SQLite database file & backups
│
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

---

## ⚡ Quick Start (Run Locally)

1. Create and activate a Python virtual environment (recommended Python 3.9+):

   ```bash
   python -m venv venv
   source venv/bin/activate     # Linux/macOS
   venv\Scripts\activate        # Windows
   ```

2. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the FastAPI backend with hot reload:

   ```bash
   uvicorn backend.app:app --reload --port 8000
   ```

4. Open your browser and visit:

   * API root: `http://127.0.0.1:8000`
   * Interactive API docs (Swagger UI): `http://127.0.0.1:8000/docs`

---

## 🔮 Planned Features / Next Steps

* **Role-based permissions** and **JWT Authentication** for secure access control
* Web frontend with server-rendered templates or SPA using React/Vue
* Desktop app with PySide6 or CustomTkinter, syncing with backend or standalone with local DB
* Export student data to Excel and PDF formats
* Email/SMS notifications for attendance and grades
* Dark & Light UI themes
* Offline mode support for desktop with data sync capabilities
* Unit tests, Continuous Integration (CI), and Docker containerization for deployment

---

## 💡 Naming & Vision

**EduTrack** — a short, modern, and clear name that reflects our mission to efficiently track and manage student data for schools and educational institutions.

If you have suggestions for a different name or branding, feel free to propose!

---

## 🤝 Contributing

Contributions and suggestions are welcome! Feel free to open issues or submit pull requests.

---

## 📄 License
MIT License

Copyright (c) 2025 Rayhan Dodi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
