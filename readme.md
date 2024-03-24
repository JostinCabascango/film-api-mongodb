# Film API

This is a simple API that allows you to manage films. You can perform CRUD operations on films and also filter, sort and
limit the films. The API uses MongoDB as its database.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing
purposes.

### Prerequisites

- Python 3.8 or higher
- MongoDB

### Installing

1. Clone the repository:
    ```
    git clone https://github.com/JostinCabascango/film-api-mongodb.git
    ```
2. Navigate to the project directory:
    ```
    cd film-api-mongodb
    ```
3. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

## Running the Application

To run the application, use the following command in the project directory:

```
uvicorn main:app --reload
```

The application will be available at `http://localhost:8000`.

## Testing the API

You can test the API using the provided `tests/test_main.http` file in a tool
like [REST Client for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)
or [Postman](https://www.postman.com/).

The API has the following endpoints:

- `GET /api/films/`: Get all films.
- `GET /api/films/{film_id}`: Get a single film by its ID.
- `POST /api/films/`: Create a new film.
- `PUT /api/films/{film_id}`: Update a film by its ID.
- `DELETE /api/films/{film_id}`: Delete a film by its ID.
- `GET /api/films/filter/`: Get films by genre.
- `GET /api/films/sort/`: Get sorted films.
- `GET /api/films/limit/`: Get limited films.

