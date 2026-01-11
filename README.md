## Late Show API
## Description

The Late Show API is a Flask REST API that manages episodes, guests, and their appearances on the Late Show.
It allows users to view episodes, guests, and create new guest appearances with ratings.

The API uses Flask, SQLAlchemy, and Flask-Migrate, and follows RESTful conventions.

## Technologies Used

Python

Flask

Flask SQLAlchemy

Flask Migrate

SQLite

Postman (for testing)

## Database Models
Episode

id (Integer, Primary Key)

date (String)

number (Integer)

Has many appearances

Guest

id (Integer, Primary Key)

name (String)

occupation (String)

Has many appearances

Appearance

id (Integer, Primary Key)

rating (Integer)

episode_id (Foreign Key)

guest_id (Foreign Key)

Belongs to an episode and a guest

## Validations

Appearance.rating must be between 1 and 5 (inclusive)

Relationships

An Episode has many Guests through Appearances

A Guest has many Episodes through Appearances

Deleting an episode or guest cascades and deletes related appearances

## Setup Instructions
1. Clone the Repository
git clone <your-private-repo-url>
cd lateshow-firstname-lastname

2. Install Dependencies
pipenv install
pipenv shell

3. Run Migrations
flask db upgrade

4. Seed the Database
python seed.py

5. Start the Server
flask run


Server runs at:

http://127.0.0.1:5000

API Endpoints
GET /episodes

Returns all episodes.

Response Example:

[
  {
    "id": 1,
    "date": "1/11/99",
    "number": 1
  }
]

## GET /episodes/:id

Returns a single episode with its appearances.

Success Response:

{
  "id": 1,
  "date": "1/11/99",
  "number": 1,
  "appearances": [
    {
      "id": 1,
      "rating": 4,
      "episode_id": 1,
      "guest_id": 1,
      "guest": {
        "id": 1,
        "name": "Michael J. Fox",
        "occupation": "actor"
      }
    }
  ]
}


Error Response:

{
  "error": "Episode not found"
}

## GET /guests

Returns all guests.

Response Example:

[
  {
    "id": 1,
    "name": "Michael J. Fox",
    "occupation": "actor"
  }
]

## POST /appearances

Creates a new appearance.

Request Body:

{
  "rating": 5,
  "episode_id": 2,
  "guest_id": 3
}


Success Response:

{
  "id": 10,
  "rating": 5,
  "guest_id": 3,
  "episode_id": 2,
  "episode": {
    "id": 2,
    "date": "1/12/99",
    "number": 2
  },
  "guest": {
    "id": 3,
    "name": "Tracey Ullman",
    "occupation": "television actress"
  }
}


Validation Error Response:

{
  "errors": ["Rating must be between 1 and 5"]
}

## Testing

A Postman collection is provided:

Import challenge-4-lateshow.postman_collection.json

Run all requests to verify functionality

## Author

Elvin Mwarangu

## License

This project is for educational purposes.