# StreamFlix – AWS Three-Tier Web Application

StreamFlix is a simple Netflix-style movie web application developed using Python Flask and deployed on AWS using a three-tier architecture.

## Architecture

Browser
↓
Amazon EC2
↓
Flask + Gunicorn
↓
Amazon RDS MySQL

## Technologies Used

- Python
- Flask
- HTML
- CSS
- MySQL
- Amazon EC2
- Amazon RDS
- Gunicorn
- systemd
- Git/GitHub

## Features

- Movie listing
- Movie search
- Movie details
- MySQL database
- AWS EC2 deployment
- Amazon RDS database
- Gunicorn application server
- systemd service for automatic application startup

## AWS Configuration

### Application Tier
The Flask application is deployed on an Amazon EC2 instance.

### Database Tier
Amazon RDS MySQL is used to store movie information.

### Security
EC2 communicates with RDS through AWS Security Groups.

### Deployment
Gunicorn is used as the application server and systemd manages the StreamFlix service.

## Project Structure

streamflix/
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── movie.html
├── static/
│   └── style.css
└── .gitignore

## Note

Database credentials and other sensitive configuration values are stored in environment variables and are not included in this repository.
