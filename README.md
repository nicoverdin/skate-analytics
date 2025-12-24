# Skate Analytics 📊

[![CI Status](https://github.com/nicoverdin/skate-analytics/actions/workflows/ci.yml/badge.svg)](https://github.com/nicoverdin/skate-analytics/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Django](https://img.shields.io/badge/Django-5.0-green)
![JWT](https://img.shields.io/badge/Auth-JWT-orange)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ed)

**Skate Analytics** is a Full Stack application designed to track, analyze, and visualize figure skating performance metrics. It provides coaches and athletes with data-driven insights to improve technical elements and program scores.

---

## 🔐 Security & Auth (Phase 2 Complete)

The project now features a robust security layer to protect athlete data:
* **JWT Authentication:** Stateless security using `dj-rest-auth` and `SimpleJWT`.
* **RBAC (Role-Based Access Control):** * **Skaters:** Can only view and manage their own performance data.
    * **Admins:** Full access to manage technical elements and global statistics.
* **Data Privacy:** Every Skater profile is strictly linked to a Django User account.



## 🚀 Key Features

* **RESTful API:** Built with Django REST Framework.
* **Smart Scoring:** Automatic calculation of total scores based on base values, levels, and extra points.
* **Data Integrity:** Auto-generation of technical element codes (e.g., `Tr2%`) to prevent human error.
* **Dockerized Environment:** Full development setup using Docker & Docker Compose.
* **CI/CD Pipeline:** Automated testing (Unit/Integration) and linting via GitHub Actions.

## 🛠️ Tech Stack

* **Backend:** Python, Django REST Framework.
* **Security:** JWT, Django AllAuth.
* **Database:** PostgreSQL.
* **DevOps:** Docker, GitHub Actions.
* **Frontend:** Vue 3 + Vite (Phase 3 - Upcoming).

---

## 📦 How to Run

Prerequisites: **Docker** and **Docker Compose**.

1. **Clone and Enter:**
    ```bash
    git clone [https://github.com/nicoverdin/skate-analytics.git](https://github.com/nicoverdin/skate-analytics.git)
    cd skate-analytics
    ```

2. **Launch & Migrate:**
    ```bash
    docker-compose up -d --build
    docker-compose exec backend python manage.py migrate
    ```

3. **Create a User:**
    ```bash
    docker-compose exec backend python manage.py createsuperuser
    ```

4. **Run Tests:**
    ```bash
    docker-compose exec backend python manage.py test
    ```

---

## 🔌 API Endpoints (Protected)

| Resource | Endpoint | Auth Required | Description |
| :--- | :--- | :--- | :--- |
| **Auth** | `/api/auth/` | No | Login, logout, and token refresh. |
| **Skaters** | `/api/skaters/` | **Yes** | User-specific athlete profiles. |
| **Elements** | `/api/elements/` | **Yes** | Technical library (Jumps, Spins). |
| **Results** | `/api/results/` | **Yes** | Performance outcomes. |

---

## 🗺️ Roadmap

- [x] **Phase 1:** Backend Core & DevOps (Models, Serializers, CI/CD).
- [x] **Phase 2:** Authentication & Security (JWT, Permissions).
- [ ] **Phase 3:** Frontend Visualization (Vue 3, Dashboards, Charts).

---
> **Current Status:** Phase 2 is complete. Now working on Phase 3: bringing the data to life with a Vue 3 dashboard.