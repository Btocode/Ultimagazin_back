# Ultimagazin_back

This is a Python-Django app that requires `pipenv` for managing dependencies. Please follow the instructions below to set up and run the app.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- `pipenv`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo-url.git


3. Navigate to the project folder:

3. Install the dependencies using pipenv:

4. Setup the environment variables:

5. Create a .env file in the project folder and configure the required environment variables

**Database Migration**
6. Run the following command to apply database migrations:
```shell
python3 manage.py makemigration
python3 manage.py migrate 
```
**Running the App**
7. Start the Django development server:
```shell
python3 manage.py runserver 
```
_License
This project is licensed under the MIT License._

```shell
Replace `your-repo-url`, `project-folder`, and update the necessary environment variables, secret key, and other configuration details based on your specific app requirements.

Remember to include a `LICENSE` file in your project directory if you haven't already and update the `License` section in the `readme.md` file accordingly.
```
