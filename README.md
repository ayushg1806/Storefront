# Django E-Commerce REST API | [Live App 🚀](https://storefront-8il5.onrender.com)

A production-style **e-commerce backend API** built with **Django** and **Django REST Framework**, designed to demonstrate how to build, test, optimize, and deploy a scalable RESTful backend.

This project focuses on **clean architecture**, **real-world API design**, **authentication**, **caching**, **testing**, and **deployment** using modern tools.

---

## Features

- RESTful API design (resource-oriented)
- Product & collection management
- Shopping cart functionality
- Order creation and management
- JWT authentication & authorization
- Role-based permissions (admin vs user)
- PostgreSQL (production) & MySQL (development)
- Redis caching
- Automated testing with Pytest
- Load testing with Locust
- Dockerized deployment
- Production-ready configuration

---

## Tech Stack

| Category | Technology |
|-------|-----------|
| Backend | Django, Django REST Framework |
| Authentication | JWT (Djoser + SimpleJWT) |
| Database (Dev) | MySQL |
| Database (Prod) | PostgreSQL (Supabase) |
| Caching | Redis |
| Testing | Pytest, pytest-django |
| Load Testing | Locust |
| Deployment | Docker, Render |
| Static Files | WhiteNoise |

---

## Project Structure
```text
storefront/
├── core/
├── likes/
├── locustfiles/
├── media/
├── playground/
├── static/
├── store/
├── storefront/
│   ├── settings/
│   │   ├── common.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── urls.py
│   └── wsgi.py
├── tags/
├── Dockerfile
├── manage.py
├── Pipfile
├── Pipfile.lock
├── pytest.ini
├── README.md
├── requirements.txt
└── requirements_dev.txt
```

## Authentication

### Register User
**POST** `/auth/users/`

```json
{
  "email": "user@example.com",
  "password": "StrongPassword123",
  "first_name": "John",
  "last_name": "Doe"
}
```

---

### Login (Get JWT Tokens)
**POST** `/auth/jwt/create/`

```json
{
  "email": "user@example.com",
  "password": "StrongPassword123"
}
```

---

### Refresh Token
**POST** `/auth/jwt/refresh/`

---

### Get Current User
**GET** `/auth/users/me/`

**Headers**
```
Authorization: Bearer <access_token>
```

---

## Store API

### Collections

| Method | Endpoint | Description |
|------|--------|------------|
| GET | `/store/collections/` | List collections |
| POST | `/store/collections/` | Create collection (admin only) |
| GET | `/store/collections/{id}/` | Retrieve collection |
| PUT | `/store/collections/{id}/` | Update collection (admin only) |
| DELETE | `/store/collections/{id}/` | Delete collection (admin only) |

---

### Products

| Method | Endpoint | Description |
|------|--------|------------|
| GET | `/store/products/` | List products |
| POST | `/store/products/` | Create product (admin only) |
| GET | `/store/products/{id}/` | Retrieve product |
| PUT | `/store/products/{id}/` | Update product (admin only) |
| DELETE | `/store/products/{id}/` | Delete product (admin only) |

---

### Filtering, Searching & Ordering

```
/store/products/?collection_id=1
/store/products/?search=laptop
/store/products/?ordering=price
```

---

### Product Images

| Method | Endpoint |
|------|--------|
| GET | `/store/products/{id}/images/` |
| POST | `/store/products/{id}/images/` |
| DELETE | `/store/products/{id}/images/{image_id}/` |

---

## Cart API

### Create Cart
**POST** `/store/carts/`

---

### Retrieve Cart
**GET** `/store/carts/{cart_id}/`

---

### Cart Items

| Method | Endpoint |
|------|--------|
| POST | `/store/carts/{cart_id}/items/` |
| GET | `/store/carts/{cart_id}/items/` |
| PATCH | `/store/carts/{cart_id}/items/{item_id}/` |
| DELETE | `/store/carts/{cart_id}/items/{item_id}/` |

---

## Orders

### Create Order
**POST** `/store/orders/`

**Headers**
```
Authorization: Bearer <access_token>
```

---

### List User Orders
**GET** `/store/orders/`

**Headers**
```
Authorization: Bearer <access_token>
```

---

### List All Orders (Admin)
**GET** `/store/orders/`

**Headers**
```
Authorization: Bearer <admin_token>
```

---

### Update Order Status (Admin)
**PATCH** `/store/orders/{id}/`

---

## Caching

Redis is used to cache:

- Product lists  
- Product details  

This improves performance and reduces database load.

---

## Testing

Run automated tests using Pytest:

```bash
pytest
```

---

## Load Testing

Simulate concurrent users with Locust:

```bash
locust
```

---

## Docker

### Build Image
```bash
docker build -t storefront .
```

### Run Container
```bash
docker run -p 8000:8000 storefront
```

---

## Deployment

- Dockerized backend  
- PostgreSQL hosted on Supabase  
- Deployed on Render  
- Database migrations run automatically at startup  
