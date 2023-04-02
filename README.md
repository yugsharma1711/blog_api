// README.md
# Project Support
### Introduction
This is a versatile API designed to serve as a backend for various types of blog websites. It utilizes Azure SQL Database for efficient management of the database, while images are stored on the local machine. Detailed documentation is available on the home page of the blog API, providing all the necessary information for easy implementation and customization.
### Project Support Features
* Users can signup and login to their accounts
* Public (non-authenticated) users can access blogs on the platform
* Authenticated users can access all causes as well as create a new blog, edit their created blog and also delete what they've created.
### Installation Guide
* Clone this repository [here](https://github.com/blackdevelopa/ProjectSupport.git).
* The main branch is the most stable branch at any given time, ensure you're working from it.
* Run python manage.py runserver to start the server.
* You can't work with the azure database and your IP wont be allowed, So use your locally installed DB. Do configure to your choice in the application entry file.
### Usage
* Run python manage.py runserver to start the application.
* Connect to the API using Postman on port 7066.
### API Endpoints
| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| POST | /api/token |Takes a set of user credentials and returns an access and refresh JSON web token pair to prove the authentication of those credentials.|
| POST | POST /api/token/refresh/ |Takes a refresh type JSON web token and returns an access type JSON web token if the refresh token is valid.|
| POST | /api/user/register/ | To create a new user |
| POST | /api/createblog/ | To create the blog |
| DELETE | /api/deleteblog/{id} | To delete  a blog |
| GET | /api/getallblog/| To get all the blogs |
| GET | /api/getblog/{id}/ | To retrieve a single blog |
### Technologies Used
* [Django](https://www.djangoproject.com/) Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.
* [Azure](https://azure.microsoft.com/en-us/ )Microsoft Azure, often referred to as Azure, is a cloud computing platform operated by Microsoft that provides access, management, and development of applications and services via globally-distributed data centers.
