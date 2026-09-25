# StreamFlix – AWS Three-Tier Web Application

StreamFlix is a simple Netflix-style movie web application built using Python Flask and deployed on AWS using a three-tier architecture.

## Architecture

User Browser → Amazon EC2 → Flask + Gunicorn → Amazon RDS MySQL

The application follows a simple three-tier architecture:

- Presentation Layer – HTML and CSS frontend
- Application Layer – Python Flask application running on Amazon EC2
- Database Layer – MySQL database hosted on Amazon RDS

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
- Git
- GitHub

## Features

- Movie listing
- Movie search
- Movie details
- Movie ratings
- Movie genres
- Movie descriptions
- MySQL database integration
- AWS EC2 deployment
- Amazon RDS MySQL database
- Gunicorn application server
- systemd service for automatic application startup
- Environment variables for database credentials

## AWS Architecture

### Amazon EC2

The Flask application is deployed on an Amazon EC2 instance running Amazon Linux.

EC2 acts as the application server and handles requests from users.

### Amazon RDS

Amazon RDS MySQL is used as the database tier.

The application connects to the RDS MySQL database to store and retrieve movie information.

### Gunicorn

Gunicorn is used as the application server to run the Flask application on EC2.

### systemd

A systemd service is configured to manage the StreamFlix application.

It allows the application to:

- Start automatically
- Continue running after the SSH terminal is closed
- Restart automatically if the application stops unexpectedly

### Security Groups

AWS Security Groups are used to control network communication.

EC2 allows web application traffic through port 5000.

RDS allows MySQL traffic through port 3306 from the EC2 security group.

## Application Flow
```text
Browser
↓
Amazon EC2
↓
Gunicorn
↓
Flask Application
↓
Amazon RDS MySQL
```
## Project Structure
```text
streamflix/
├── app.py
├── requirements.txt
├── .gitignore
├── templates/
│   ├── index.html
│   └── movie.html
└── static/
    └── style.css
```
## Application Features

### Home Page

The home page displays the available movies with information such as:

- Movie title
- Genre
- Release year
- Rating
- Movie poster

### Search

Users can search for movies by title.

### Movie Details

Users can select a movie to view its detailed information.

## Database

The application uses MySQL hosted on Amazon RDS.

The database contains movie information including:

- Movie ID
- Title
- Genre
- Release year
- Rating
- Description
- Poster URL

## Security

Database credentials are stored using environment variables.

The `.env` file is not included in the GitHub repository.

The `.gitignore` file is configured to prevent sensitive and unnecessary files from being uploaded.

Sensitive information such as:

- Database passwords
- AWS credentials
- Private keys
- Environment files

is not included in the repository.

## Deployment

The application was developed locally using Python and Flask.

It was then deployed to Amazon EC2 and connected to an Amazon RDS MySQL database.

Gunicorn was configured as the application server, and systemd was used to manage the application service.

## Deployment Steps

1. Developed the Flask application locally.
2. Created the frontend using HTML and CSS.
3. Added MySQL database integration.
4. Created an Amazon RDS MySQL database.
5. Created an Amazon EC2 instance.
6. Configured EC2 Security Groups.
7. Configured RDS Security Groups.
8. Connected EC2 to RDS.
9. Uploaded the application source code to GitHub.
10. Cloned the GitHub repository on EC2.
11. Installed the required Python dependencies.
12. Configured environment variables.
13. Tested the Flask application.
14. Installed and configured Gunicorn.
15. Created a systemd service.
16. Enabled automatic application startup.
17. Tested the deployed application.

## Requirements

The main Python dependencies are listed in `requirements.txt`.

The project requires:

- Python
- Flask
- Flask-SQLAlchemy
- PyMySQL
- python-dotenv
- Gunicorn

## Learning Outcomes

Through this project, I gained practical experience with:

- Python Flask
- Web application development
- MySQL
- Amazon EC2
- Amazon RDS
- AWS Security Groups
- Linux commands
- Git and GitHub
- Gunicorn
- systemd
- Environment variables
- Basic cloud deployment
- Three-tier application architecture

## Future Improvements

Possible future improvements include:

- User authentication
- User registration
- Movie categories
- Watchlist functionality
- User ratings and reviews
- Online video streaming
- HTTPS
- Custom domain
- Load balancing
- CI/CD pipeline
- Docker containerization

