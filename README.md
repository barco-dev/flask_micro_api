# Flask Micro-API

This project is a minimal Flask REST API created for a backend and API design assignment.

## Features

- `GET /hello` returns a welcome message in JSON format.
- `GET /data` returns structured sample data.
- `POST /data` accepts a JSON object and adds it to the in-memory data list.
- Proper JSON responses and HTTP status codes are included.
- A Python `requests` test script demonstrates the API calls.

## Project Structure

```text
flask-micro-api/
├── app.py
├── test_api.py
├── requirements.txt
├── AGILE.md
└── README.md
```

## Installation

1. Clone or download the repository.
2. Open a terminal in the project folder.
3. Create a virtual environment if desired.
4. Install the dependencies:

```bash
python3 -m pip install -r requirements.txt
```

## Run the API

```bash
python3 app.py
```

The Flask server should start at:

```text
http://127.0.0.1:5000
```

## Endpoints

### GET /hello

Example response:

```json
{
  "message": "Hello! Welcome to Carlos's Flask Micro-API.",
  "status": "success"
}
```

### GET /data

Example response:

```json
{
  "count": 3,
  "data": [
    {
      "id": 1,
      "name": "Java",
      "category": "Programming Language"
    }
  ],
  "status": "success"
}
```

### POST /data

Send JSON such as:

```json
{
  "name": "Flask",
  "category": "Python Web Framework"
}
```

A successful request returns HTTP `201 Created`.

## Testing

Keep `app.py` running in one terminal. Open a second terminal and run:

```bash
python3 test_api.py
```

The script tests:

- `GET /hello`
- `GET /data`
- `POST /data`

Take a screenshot of the successful terminal output for the assignment evidence.

## Agile Process

See `AGILE.md` for the small sprint plan, user stories, backlog, and definition of done used for this project.
