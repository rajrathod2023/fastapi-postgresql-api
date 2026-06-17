# FastAPI PostgreSQL CRUD API

## Overview

A REST API built using FastAPI, PostgreSQL, and SQLAlchemy for managing employee records.

## Features

* Create Employee
* Get Employees
* Update Employee
* Delete Employee
* Health Check Endpoint

## Technologies Used

* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic
* Uvicorn
* Git & GitHub

## Installation

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python -m uvicorn app.main:app --reload
```

### Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint        | Description     |
| ------ | --------------- | --------------- |
| GET    | /               | Health Check    |
| GET    | /employees      | Get Employees   |
| POST   | /employees      | Create Employee |
| PUT    | /employees/{id} | Update Employee |
| DELETE | /employees/{id} | Delete Employee |

## Database

PostgreSQL 17

Database Name:

employee_db

## Author

Raj Rathod
