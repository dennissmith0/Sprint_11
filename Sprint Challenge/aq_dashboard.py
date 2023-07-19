"""OpenAQ Air Quality Dashboard with Flask."""
from flask import Flask
import openaq
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = openaq.OpenAQ()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(app)


class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(30), nullable=False)
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return '{}, {}'.format(self.datetime, self.value)


with app.app_context():
    DB.create_all()  # Add this line


@app.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    DB.drop_all()
    DB.create_all()

    # Get data from OpenAQ, make Record objects with it, and add to db
    data = get_results('Los Angeles', 'pm25')
    for utc_datetime, value in data:
        record = Record(datetime=utc_datetime, value=value)
        DB.session.add(record)
    DB.session.commit()
    return 'Data refreshed!'


def get_results(city='Los Angeles', parameter='pm25'):
    # Retrieve the data from the API
    status, body = api.measurements(city=city, parameter=parameter)

    # Create a list of (utc_datetime, value) tuples

    # return results
    if status == 200:
        results = [(item['date']['utc'], item['value'])
                   for item in body['results']]
        return results
    else:
        return []


@app.route('/')
def root():
    """Base view."""
    # Retrieve the list of tuples
    # results = get_results('Los Angeles', 'pm25')

    """Main route, display potentially risky PM 2.5 values."""
    # Query the database for records with value >= 18
    risky_records = Record.query.filter(Record.value >= 18).all()

    # Convert the records to (datetime, value) tuples
    # results = [(record.datetime, record.value) for record in risky_records]

    # Convert the list to a string and return it
    return str(risky_records)


if __name__ == '__main__':
    app.run()
