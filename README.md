# 🌿Breathe ESG Dashboard — Enterprise ESG Review Platform

Breathe ESG Dashboard is a production-grade ESG data ingestion and governance platform designed to process, normalize, review, and monitor sustainability activities across enterprise data sources.

The platform enables organizations to upload operational ESG datasets, review activities, approve or lock records, monitor KPI metrics, and maintain audit-ready governance workflows through a modern enterprise dashboard.

---

## 🚀 Features

### ✅ ESG Data Ingestion Pipeline

Supports ingestion from multiple enterprise ESG sources:

* SAP Procurement Data
* Utility Electricity Consumption
* Corporate Travel Activities

Each dataset is normalized into a unified ESG activity model.

---

### ✅ ESG Review Dashboard

Enterprise dashboard with:

* Real-time ESG activity monitoring
* KPI analytics cards
* Approval workflows
* Lock workflows
* Status tracking
* Live activity updates
* Enterprise dark UI

---

### ✅ Activity Governance Workflow

Manage ESG activities through:

* Pending Review
* Approval Actions
* Record Locking
* Immutable Governance States
* Audit-Ready Processing

---

### ✅ Search & Filtering

Advanced dashboard filtering with:

* Activity search
* Source filtering
* Status filtering
* Scope-based filtering

---

### ✅ KPI Analytics

Real-time ESG metrics:

* Total Activities
* Approved Count
* Locked Count
* Pending Count

---

## 🧠 ESG Workflow States

| Status   | Description             |
| -------- | ----------------------- |
| PENDING  | Awaiting ESG review     |
| APPROVED | ESG activity approved   |
| LOCKED   | Finalized and immutable |

---

## ⚙️ Tech Stack

### Backend

* Django
* Django REST Framework
* Python
* SQLite

### Frontend

* React.js
* Vite
* Axios
* CSS3

---

## 🎨 UI Features

* Modern Enterprise Dashboard
* Dark Professional Theme
* KPI Analytics Cards
* Responsive Layout
* Hover Animations
* Live Status Indicators
* Interactive Table Actions

---

## 📁 Project Structure

```txt
breathe-esg-assignment/
│
├── backend/
│   ├── config/
│   ├── ingestion/
│   └── manage.py
│
├── frontend/
│   ├── src/
│   └── public/
│
├── sample_data/
│   ├── sap_fuel_procurement.csv
│   ├── utility_electricity.csv
│   └── travel_data.csv
│
└── README.md
```

---

## 🔐 ESG Governance Modules

| Module               | Purpose                    |
| -------------------- | -------------------------- |
| Data Ingestion       | Upload ESG datasets        |
| Normalization Engine | Standardize ESG records    |
| Review Workflow      | Approve activities         |
| Lock Workflow        | Finalize immutable records |
| KPI Analytics        | ESG dashboard metrics      |
| Audit Management     | Governance-ready tracking  |

---

## ⚡ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Ayushjssj/BREATHE-ESG-DASHBOARD.git
```

---

### 2️⃣ Navigate Into Project

```bash
cd breathe-esg-assignment
```

---

## ⚙️ Backend Setup

### Create Virtual Environment

```bash
cd backend
python -m venv venv
```

---

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

---

#### Install Dependencies

```bash
pip install django djangorestframework django-cors-headers pandas
```

---

#### Run Migrations

```bash
python manage.py migrate
```

---

#### Create Superuser

```bash
python manage.py createsuperuser
```

---

#### Start Backend Server

```bash
python manage.py runserver
```

Backend runs on:

```txt
http://127.0.0.1:8000
```

---

## ▶️ Frontend Setup

#### Install Frontend Dependencies

```bash
cd frontend
npm install
```

---

#### Install Axios

```bash
npm install axios
```

---

#### Start Frontend

```bash
npm run dev
```

Frontend runs on:

```txt
http://localhost:5173
```

---

## 📥 Sample CSV Upload

### SAP Procurement Upload

```bash
curl.exe -X POST "http://127.0.0.1:8000/api/upload/" ^
-F "tenant_id=1" ^
-F "source_id=1" ^
-F "file=@C:/path/sap_fuel_procurement.csv"
```

---

### Utility Upload

```bash
curl.exe -X POST "http://127.0.0.1:8000/api/upload/" ^
-F "tenant_id=1" ^
-F "source_id=2" ^
-F "file=@C:/path/utility_electricity.csv"
```

---

### Travel Upload

```bash
curl.exe -X POST "http://127.0.0.1:8000/api/upload/" ^
-F "tenant_id=1" ^
-F "source_id=3" ^
-F "file=@C:/path/travel_data.csv"
```

---

## 📡 API Endpoints

| Method | Endpoint                        | Description          |
| ------ | ------------------------------- | -------------------- |
| GET    | `/api/activities/`              | Fetch ESG activities |
| POST   | `/api/upload/`                  | Upload CSV data      |
| POST   | `/api/activities/<id>/approve/` | Approve activity     |
| POST   | `/api/activities/<id>/lock/`    | Lock activity        |

---

## 🌐 Main Dashboard Features

| Feature           | Description               |
| ----------------- | ------------------------- |
| KPI Cards         | ESG analytics overview    |
| Activity Table    | Real-time ESG monitoring  |
| Approval Workflow | ESG governance review     |
| Lock Workflow     | Immutable record handling |
| Search System     | Activity filtering        |
| Status Indicators | Governance tracking       |

---

## 🧠 Future Improvements

* Multi-Tenant ESG Support
* Authentication & RBAC
* PostgreSQL Integration
* ESG Report Export
* Real-Time Notifications
* AI-based ESG Insights
* Advanced ESG Analytics

---

## 👨‍💻 Built By

### Ayush Pandey

* Agentic AI Engineer
* AI & ESG Platform Developer
* Machine Learning Enthusiast

#### Connect With Me

* GitHub: https://github.com/Ayushjssj
* Email: [payush1502@gmail.com](mailto:payush1502@gmail.com)

---

## 📜 License

This project was developed as part of the **Breathe ESG Tech Intern Assignment**.

Unauthorized copying, redistribution, or commercial usage of this software without permission may constitute copyright infringement.

---

## ⭐ Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork the project
* 🌿 Build sustainable ESG systems

---

## 🚀 Breathe ESG Dashboard

#### Ingest • Normalize • Review • Govern • Monitor ESG Activities
