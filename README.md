Network Monitoring Tool
A Django-based API for managing devices, metrics, alerts, and users.
Table of Contents
Features
Requirements
Installation
API Endpoints
Authentication
Usage
Features
CRUD operations for devices, metrics, alerts, and users
User authentication using Django REST framework's built-in authentication system
Token-based authentication for API requests
Requirements
Django 4.x
Django REST framework 3.x
PostgreSQL database
psycopg2-binary database adapter
Installation
Clone the repository: git clone https://github.com/your-username/network-monitor.git
Install required packages: pip install -r requirements.txt
Create a PostgreSQL database and update the DATABASES setting in settings.py
Run migrations: python manage.py migrate
Start the development server: python manage.py runserver
API Endpoints
Devices
GET /api/devices/: Fetch all devices
POST /api/devices/: Create a new device
GET /api/devices/<int:pk>/: Fetch a device by ID
PUT /api/devices/<int:pk>/: Update a device
DELETE /api/devices/<int:pk>/: Delete a device
Metrics
GET /api/metrics/: Fetch all metrics
GET /api/metrics/<int:pk>/: Fetch a metric by ID
Alerts
GET /api/alerts/: Fetch all alerts
GET /api/alerts/<int:pk>/: Fetch an alert by ID
Users
GET /api/users/<int:user_id>/devices/: Fetch all devices for a user
POST /api/users/<int:user_id>/devices/: Add a device to a user's list of monitored devices
Authentication
POST /api/login/: Authenticate a user and return a token
Authentication
This API uses Django REST framework's built-in authentication system. To authenticate, send a POST request to /api/login/ with the following data:
username: The username of the user
password: The password of the user
The response will include a token that can be used for subsequent API requests.

