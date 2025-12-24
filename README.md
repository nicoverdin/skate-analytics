# Skate Analytics ⛸️📊

[![CI Status](https://github.com/nicoverdin/skate-analytics/actions/workflows/ci.yml/badge.svg)](https://github.com/nicoverdin/skate-analytics/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Django](https://img.shields.io/badge/Django-5.0-green)
![Vue](https://img.shields.io/badge/Vue.js-3.0-42b883)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ed)

**Skate Analytics** is a Full Stack application designed to track, analyze, and visualize figure skating performance metrics. It provides coaches and athletes with data-driven insights to improve technical elements and program scores.

---

## 🚀 Features (Phase 1: Backend & DevOps)

* **RESTful API:** Built with Django REST Framework.
* **Smart Scoring:** Automatic calculation of total scores based on base values, levels, and GOE.
* **Data Integrity:** Auto-generation of technical element codes (e.g., `Tr2%`) to prevent human error.
* **Dockerized Environment:** Full development setup using Docker & Docker Compose.
* **CI/CD Pipeline:** GitHub Actions workflow for automated testing (Unit/Integration) and linting.

## 🛠️ Tech Stack

* **Backend:** Python, Django REST Framework.
* **Database:** PostgreSQL.
* **Frontend:** Vue 3 + Vite (In progress).
* **DevOps:** Docker, GitHub Actions.

---

## 📦 How to Run

Prerequisites: **Docker** and **Docker Compose**.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/TU-USUARIO/skate-analytics.git](https://github.com/TU-USUARIO/skate-analytics.git)
    cd skate-analytics
    ```

2.  **Start the environment:**
    ```bash
    docker-compose up -d --build
    ```

3.  **Access the API:**
    * API Root: [http://localhost:8000/api/](http://localhost:8000/api/)
    * Admin Panel: [http://localhost:8000/admin/](http://localhost:8000/admin/)

4.  **Run Tests:**
    ```bash
    docker-compose exec backend python manage.py test
    ```

---

## 🔌 API Endpoints

| Resource | Endpoint | Description |
| :--- | :--- | :--- |
| **Skaters** | `/api/skaters/` | Manage athletes profiles and stats. |
| **Elements** | `/api/elements/` | Technical library (Jumps, Spins, Steps). |
| **Results** | `/api/results/` | Log performance outcomes. |

---

> **Note:** This project is currently under active development. Phase 2 (Frontend Visualization) is coming next.