
# 🚗 ParkZone Parking Management System

A full-stack web and mobile-friendly parking management system for customers and admins. Customers can view available parking slots, book reservations, and manage their profiles. Admins can manage slots, reservations, and generate reports.

---

## 🔧 Project Structure

```
parkzone-project/
│
├── backend/          # Django REST API backend
├── frontend/         # ReactJS frontend
└── README.md         # Project documentation (this file)
```

---

## 🖥️ FRONTEND (ReactJS)

### 📁 Location
```
/frontend
```

### 🚀 Setup Instructions
```bash
cd frontend
npm install
npm start
```

### 🧩 Features
- Customer login & signup
- View available parking slots
- Make reservations
- View profile & edit info
- View current bookings
- Booking history modal
- Protected routes based on login

### 🔐 Route Protection
Only logged-in customers (based on `localStorage`) can access customer pages like:
- `/customer-home`
- `/view-parking`
- `/my-account`
- `/profile`

### 🔌 API Integration
All requests are handled through `axiosInstance.js` pointing to the backend base URL.

---

## ⚙️ BACKEND (Django + Django REST Framework)



###  Setup Instructions
```bash
cd backend
python -m venv venv
source venv/bin/activate      # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### ⚙️ Dependencies
- Django
- djangorestframework
- Simple JWT (for token auth)

### 🔐 Authentication
- **Customer Login**: via `/api/customers/login/` using email and password  
- **Admin/User Login**: via `/api/token/` to get JWT access & refresh tokens

---

##  API ENDPOINTS

### 🔐 Auth
| Method | Endpoint                    | Description                          |
|--------|-----------------------------|--------------------------------------|
| POST   | `/api/customers/login/`     | Custom login using email/password    |
| POST   | `/api/token/`               | JWT token login for admin/staff      |

### 👤 Customer
| Method | Endpoint                     | Description                      |
|--------|------------------------------|----------------------------------|
| GET    | `/api/customers/<id>/`       | Get customer profile             |
| PUT    | `/api/customers/<id>/`       | Update customer info             |
| GET    | `/api/customers/`            | List all customers (admin)       |

### 🅿️ ParkingLots
| Method | Endpoint                      | Description                            |
|--------|-------------------------------|----------------------------------------|
| GET    | `/api/parkinglots/`           | List all parking slots                 |
| GET    | `/api/parkinglots/<id>/`      | View a parking slot                    |
| PUT    | `/api/parkinglots/<id>/`      | Update parking slot (e.g. availability)|
| POST   | `/api/parkinglots/`           | Add a new slot (admin)                 |
| DELETE | `/api/parkinglots/<id>/`      | Delete slot (admin)                    |

### 📅 Reservations
| Method | Endpoint                       | Description                     |
|--------|--------------------------------|---------------------------------|
| GET    | `/api/reservations/`           | List all reservations           |
| POST   | `/api/reservations/`           | Create a reservation            |
| GET    | `/api/reservations/<id>/`      | View reservation details        |
| PUT    | `/api/reservations/<id>/`      | Update reservation              |
| DELETE | `/api/reservations/<id>/`      | Cancel reservation              |

### 💳 Payments 
| Method | Endpoint                    | Description                    |
|--------|-----------------------------|--------------------------------|
| GET    | `/api/payments/`            | List all payments              |
| POST   | `/api/payments/`            | Add a new payment              |
| GET    | `/api/payments/<id>/`       | View payment                   |
| PUT    | `/api/payments/<id>/`       | Update payment info            |
| DELETE | `/api/payments/<id>/`       | Delete payment                 |

---

## 🔒 Security Notes
- Customer pages are restricted using localStorage token/ID
- Admin pages (Django Admin Panel) are protected with `is_staff` or `is_superuser`

---

##  Future Enhancements
- Password reset for customers
- Email notifications
- Payment integration (mobile money, PayPal)
- Admin dashboard UI
- PDF reports export

---

## 👨‍💻 Developed By
- Abdillah Ali Khamis & Fatma Suleiman  
