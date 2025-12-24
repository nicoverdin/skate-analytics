# Skate Analytics 📊

Platform for tracking performance, levels, and progress in Figure Skating.
Designed for coaches and athletes to visualize improvement over time.

## 🚀 Tech Stack

* **Backend:** Python, Django, Django REST Framework.
* **Database:** PostgreSQL (via Docker).
* **Frontend:** Vue.js 3 + Vite (In Progress).
* **Infrastructure:** Docker Compose.

## 🛠️ Quick Start (Backend)

1.  **Clone the repo**
    ```bash
    git clone [https://github.com/tu-usuario/ice-metrics.git](https://github.com/tu-usuario/ice-metrics.git)
    cd ice-metrics
    ```

2.  **Start Database**
    ```bash
    docker-compose up -d
    ```

3.  **Setup Backend**
    ```bash
    cd backend
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    pip install -r requirements.txt
    ```

4.  **Run Migrations & Server**
    ```bash
    # Create a .env file based on .env.example first!
    python manage.py migrate
    python manage.py runserver
    ```