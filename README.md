# CRM-in-django-python-with-mysql
This Django CRM project manages users, leads, and agents. Users have roles, leads are categorized, and agents are assigned to leads for efficient organization and tracking.



# To Compile this project 
$env:READ_DOT_ENV_FILE = "True"
python manage.py runserver


# Django CRM Project

This Django project is a simple CRM (Customer Relationship Management) system with basic user authentication and management functionalities. Below is a breakdown of its components:

## User Model (`User`):
- Inherits from Django's `AbstractUser`.
- Includes boolean fields `is_organisor` and `is_agent`.

## User Profile Model (`UserProfile`):
- One-to-one relationship with the `User` model.

## Lead Model (`Lead`):
- Represents potential customers or leads.
- Fields include `first_name`, `last_name`, `age`, `organisation`, `agent`, `category`, `description`, `date_added`, `phone_number`, and `email`.

## Agent Model (`Agent`):
- Represents agents handling leads.
- Contains fields `user` and `organisation`.

## Category Model (`Category`):
- Represents lead categories such as "New", "Contacted", "Converted", "UnConverted".

## Signals:
- Utilizes `post_save` signal to create `UserProfile` instances automatically.

This project facilitates managing users, leads, agents, and lead categories within an organization, allowing for efficient management and tracking of leads.
