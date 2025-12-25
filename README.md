# Skate Analytics 📊

[![CI Status](https://github.com/nicoverdin/skate-analytics/actions/workflows/ci.yml/badge.svg)](https://github.com/nicoverdin/skate-analytics/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Vue](https://img.shields.io/badge/Vue.js-3.x-4fc08d)
![Django](https://img.shields.io/badge/Django-5.0-green)
![JWT](https://img.shields.io/badge/Auth-JWT-orange)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ed)

**Skate Analytics** is a Full Stack application designed to track, analyze, and visualize figure skating performance metrics. It provides coaches and athletes with data-driven insights to improve technical elements and program scores through an interactive web interface.

---

## 📈 Frontend & Visualization (Phase 3 Complete)

The interface is built with **Vue 3** and **Vite**, transforming raw API data into actionable insights:
* **Interactive Dashboards:** Real-time visualization of performance trends using **Chart.js**.
* **API Integration:** Seamless communication with the Django REST backend using **Axios**.
* **Responsive UI:** Built with **Tailwind CSS** to ensure coaches can track data from any device (mobile/tablet/desktop).
* **Dynamic Scoring:** Visual feedback on Base Value (BV) and Quality of Execution (QOE) for every logged element.



---

## 🚀 Key Features

* **RESTful API:** Robust backend built with Django REST Framework.
* **Performance Analytics:** Visual breakdown of elements consistency.
* **Smart Scoring:** Automatic calculation of total scores.
* **Security & RBAC:** * **Skaters:** Personal dashboard with private progress tracking.
    * **Admins:** Management of technical element libraries and global stats.
* **Dockerized Stack:** Orchestrated environment for both Backend (Django) and Frontend (Vue).

---

## 🛠️ Tech Stack

* **Backend:** Python 3.10, Django REST Framework, PostgreSQL.
* **Frontend:** Vue 3, Vite, Axios, Tailwind CSS, Chart.js.
* **Security:** JWT (SimpleJWT), Django AllAuth.
* **DevOps:** Docker & Docker Compose, GitHub Actions (CI/CD).

---

## 📦 Quick Start

Prerequisites: **Docker** and **Docker Compose**.

1. **Clone and Launch:**
    ```bash
    git clone [https://github.com/nicoverdin/skate-analytics.git](https://github.com/nicoverdin/skate-analytics.git)
    cd skate-analytics
    docker-compose up -d --build
    ```

2. **Initialize Database:**
    ```bash
    docker-compose exec backend python manage.py migrate
    docker-compose exec backend python manage.py createsuperuser
    ```

3. **Access the App:**
    * **Frontend:** `http://localhost:5173`
    * **API:** `http://localhost:8000/api/`

---

## 🔌 API Endpoints (Protected)

| Resource | Endpoint | Auth | Description |
| :--- | :--- | :--- | :--- |
| **Auth** | `/api/auth/` | No | Login, logout, and token refresh. |
| **Skaters** | `/api/skaters/` | **Yes** | User-specific athlete profiles. |
| **Elements** | `/api/elements/` | **Yes** | Technical library (Jumps, Spins). |
| **Results** | `/api/results/` | **Yes** | Performance outcomes and scores. |

---

## 🗺️ Roadmap

- [x] **Phase 1:** Backend Core & DevOps (Models, Serializers, CI/CD).
- [x] **Phase 2:** Authentication & Security (JWT, Permissions).
- [x] **Phase 3:** Frontend Visualization (Vue 3, Dashboards, Axios Integration).
- [ ] **Phase 4:** Competition Management & PDF Reporting.

---
> **Current Status:** Phase 3 is complete. The application now features a fully functional reactive dashboard.