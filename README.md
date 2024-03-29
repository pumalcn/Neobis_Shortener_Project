# URL shortener
A URL shortener is a service that transforms long and complex URLs into short, easily memorable ones. 

## Table of Contents
- [Tech Stack](#tech_stack)
- [Installation](#installation)
- [Features](#features)
- [Contributing](#contributing)

# 💻 Tech Stack:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-%23336791.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)


## Installation

### Cloning from GitHub Repository

To get started with the URL shortener, you can clone the repository from GitHub using the following steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/pumalcn/Neobis_Shortener_Project.git
 
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   py -m venv myworld
   myworld\Scripts\activate.bat
3. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   
4. Run database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   
5. Create a superuser account (for admin access)
   ```bash
   python manage.py createsuperuser
   
6. Start the development server:
   ```bash
   python manage.py runserver
   
7. Open your web browser and go to http://localhost:8000 to access the Todo_List Django Web App.

8. For Set Up the Postgres Database use tutorial https://www.koyeb.com/tutorials/use-django-rest-framework-and-managed-postgres-to-build-an-api
## Contributing

We welcome contributions to improve the Django To Do List Web App. If you'd like to contribute, please follow these guidelines:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Make your changes and test them thoroughly.

4. Submit a pull request with a clear description of your changes.

5. Ensure your code follows best practices and includes necessary tests if applicable.
