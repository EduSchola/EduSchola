# EduSchola

EduSchola is an education management system aimed at improving the efficiency and effectiveness of school administration. It provides a comprehensive platform for managing various aspects of a school, including student and staff management, course and curriculum management, financial management, and communication.

## Table of Contents
- Features
- Getting Started
- Installation
- Usage
- Contributing
- License

# Features

- Student and staff management: Easily manage student enrollment, attendance, and academic records. Keep track of staff details, roles, and responsibilities.

- Course and curriculum management: Create and manage courses, subjects, and curriculum content. Assign teachers and track student progress.

- Financial management: Track fee payments, generate invoices, and manage school finances.

- Communication: Facilitate communication between administrators, teachers, students, and parents through announcements, notifications, and messaging.

# Getting Started

These instructions will help you get a copy of the EduSchola project up and running on your local machine for development and testing purposes. For detailed instructions on contributing to the project, please refer to the CONTRIBUTING.md file.

### Prerequisites
- Python 3.x
- Django 3.x
- Reactjs (for frontend)

## Installation
Clone the repository:

git clone https://github.com/abrokinla/EduSchola.git

### Change to the project directory:

cd EduSchola
### Create and activate a virtual environment (optional but recommended):

python3 -m venv venv
source venv/bin/activate
### Install the project dependencies:

pip install -r requirements.txt

### Set up the database:

python manage.py migrate

### Usage
Start the Django development server:

python manage.py runserver
The server will start at http://localhost:8000/.

Open your web browser and visit http://localhost:8000/ to access the EduSchola application.

# Contributing
We welcome contributions from the community to help improve EduSchola. If you're interested in contributing, please follow the guidelines outlined in the CONTRIBUTING.md file.

# License
This project is licensed under the MIT License. See the LICENSE.md file for details.
