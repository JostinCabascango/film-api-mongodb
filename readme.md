# Film API

Esta es una API sencilla que te permite gestionar películas. Puedes realizar operaciones CRUD en películas, así como
filtrarlas, ordenarlas y limitarlas. La API utiliza MongoDB como base de datos.

## Getting Started

Sigue estas instrucciones para obtener una copia del proyecto y ejecutarlo en tu máquina local.

### Prerequisites

- Python 3.8 o superior
- MongoDB

### Installing

1. Clona el repositorio:
   ```
   git clone https://github.com/JostinCabascango/film-api-mongodb.git
   ```
2. Navega al directorio del proyecto:
    ```
    cd film-api-mongodb
    ```
3. Instala los paquetes requeridos:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

Para ejecutar la aplicación, usa el siguiente comando en el directorio del proyecto:

```
uvicorn main:app --reload
```

La aplicación estará disponible en `http://localhost:8000`.

## Testing the API

Puedes probar la API utilizando el archivo `tests/test_main.http` proporcionado en una herramienta
como [Postman](https://www.postman.com/).
La API tiene los siguientes endpoints:

- `GET /api/films/`: Get all films.
- `GET /api/films/{film_id}`: Get a single film by its ID.
- `POST /api/films/`: Create a new film.
- `PUT /api/films/{film_id}`: Update a film by its ID.
- `DELETE /api/films/{film_id}`: Delete a film by its ID.
- `GET /api/films/filter/`: Get films by genre.
- `GET /api/films/sort/`: Get sorted films.
- `GET /api/films/limit/`: Get limited films.

## Demo

Puedes ver una demostración del proyecto en el siguiente
enlace: [Google Drive Video](https://drive.google.com/file/d/1BlJlZuSUJLp11pGkLgfy9za6hQAtJOvv/view?usp=sharing)
