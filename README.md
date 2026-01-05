<div align="center">
  <img src="assets/banner.png" alt="RustChain Banner" width="100%">
  <br>
  <h1>Skate Analytics 📊</h1>
</div>

[![CI Status](https://github.com/nicoverdin/skate-analytics/actions/workflows/ci.yml/badge.svg)](https://github.com/nicoverdin/skate-analytics/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Vue](https://img.shields.io/badge/Vue.js-3.x-4fc08d)
![Django](https://img.shields.io/badge/Django-5.0-green)
![PWA](https://img.shields.io/badge/PWA-iOS%20Optimized-ff69b4)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ed)
![Cloud](https://img.shields.io/badge/Deployment-Coolify-6366f1)

**Skate Analytics** is a Full Stack application designed to track, analyze, and visualize figure skating performance metrics. It provides coaches and athletes with data-driven insights to improve technical elements and program scores through a high-performance web interface.

---

## 📱 Native PWA Experience (iOS & Mobile Optimized)

The application has been engineered to bridge the gap between web and native mobile apps, specifically targeting **Safari/iOS** limitations:
* **Immersive UI:** Full-screen experience using `viewport-fit=cover` and custom manifest configurations to eliminate browser navigation bars.
* **Scroll Jail & Elasticity Control:** Advanced CSS/JS architecture to block "rubber-banding" effects, providing a fixed-frame native feel.
* **Safe-Area Integration:** Dynamic layout adjustments to respect the **Notch** and **Dynamic Island** on modern iPhones.
* **Touch-First Design:** Optimized for rapid data entry during training sessions with zero-latency interactions.

---

## ☁️ Infrastructure & Cloud Deployment

Moving beyond `localhost`, the project is now live in a production environment:
* **Cloud Hosting:** Orchestrated on a **VPS** using **Coolify** for seamless CI/CD.
* **Containerization:** Fully dockerized stack (PostgreSQL, Django, Vue, Nginx).
* **Secure Access:** Automated SSL certification via Let's Encrypt and custom domain routing.
* **Automated Pipeline:** Integrated GitHub Actions for continuous testing and deployment.

---

## 🚀 Key Features

* **RESTful API:** Robust backend built with Django REST Framework.
* **Performance Analytics:** Visual breakdown of element consistency and scoring trends.
* **Interactive Dashboards:** Real-time visualization using **Chart.js**.
* **Smart Scoring:** Automatic calculation of Base Value (BV) and Quality of Execution (QOE).
* **RBAC (Role-Based Access Control):** * **Skaters:** Private progress tracking and performance history.
    * **Admins:** Management of technical element libraries (SOV) and global statistics.

---

## 🛠️ Tech Stack

* **Backend:** Python 3.10, Django REST Framework, PostgreSQL.
* **Frontend:** Vue 3 (Composition API), Vite, Axios, Tailwind CSS, Chart.js.
* **DevOps:** Docker & Docker Compose, Coolify, GitHub Actions.
* **Security:** JWT (SimpleJWT), Django AllAuth, HTTPS/SSL.

---

## 📦 Quick Start (Local Development)

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
| **Elements** | `/api/elements/` | **Yes** | Technical SOV library (Jumps, Spins). |
| **Results** | `/api/results/` | **Yes** | Performance outcomes and scoring data. |

---

## 🗺️ Roadmap

- [x] **Phase 1:** Backend Core & DevOps (Models, Serializers, CI/CD).
- [x] **Phase 2:** Authentication & Security (JWT, Permissions).
- [x] **Phase 3:** Frontend & Cloud (Vue 3, PWA Optimization, VPS Deployment).
- [ ] **Phase 4:** Competition Management & PDF Reporting.

---
> **Current Status:** Live in Production. The application is now fully accessible as a PWA with real-time data visualization.
