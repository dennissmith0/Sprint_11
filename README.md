# Sprint 11 (BloomTech)
 
# Air Quality Dashboard

This Flask web application pulls data from the OpenAQ API, stores it in a SQLite database using Flask-SQLAlchemy, and displays potentially risky PM 2.5 values on a simple HTML page.

## Setup

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the required Python packages: `pip install -r requirements.txt`.
4. Set the environment variable for Flask: `export FLASK_APP=aq_dashboard.py`.
5. Run the Flask application: `FLASK_APP=aq_dashboard.py flask run`.
6. It's not required, but you can enable debug mode if you find that it's helpful to you: 'FLASK_ENV='development' FLASK_DEBUG=1'

## Usage

1. Navigate to the main page (`localhost:5000/` by default). This page will display a list of dates and times where the PM 2.5 value was 18 or above.
2. To pull fresh data from the OpenAQ API and update the database, navigate to the refresh route (`localhost:5000/refresh` by default).

## Project Structure

- `aq_dashboard.py`: This is the main file for the Flask application. It defines the routes and contains the main logic for interacting with the OpenAQ API and the SQLite database.
- (TODO) `templates/`: This directory contains the Jinja2 templates for the HTML pages.
- (TODO) `test_aq_dashboard.py`: This file contains tests for the functions in `aq_dashboard.py`.
- `README.md`: This file provides an overview of the project and instructions for setup and usage.

## Future Improvements (Stretch Goals)

- Add a form to the main page that allows users to specify which city they want to see data for.
- Store different types of requests in the database, and connect the entities appropriately with relations.
- Instead of dropping all data for every pull, only add new data and keep the rest.
- Perform some data analysis on the stored data (e.g., calculate averages, identify trends).
- Deploy the application on Heroku.
