# juvoxa
Simulation of a platform to be used by hospitals for managing doctors and patients

## Requirements

The project requires [Python 3.7](https://www.python.org/downloads/release/python-370/) or higher and
the [PIP](https://pip.pypa.io/en/stable/) package manager.

## Useful Python commands

### Installation

Install the project dependencies

```console
$ pip install -r requirements.txt
```

### Run the application

Run the application which will be listening on port `5000`.

```console
$ python3 app/app.py
```

### Note: The app will serve a html page, but the frontend is not implemented completely yet

### Please navigation to Swagger OpenAPI Documentatio instead.
```
http://192.168.64.243:5000/api/ui
```


## API

Below is a list of API endpoints with their respective input and output. Please note that the application needs to be
running for the following endpoints to work. For more information about how to run the application, please refer
to [run the application](#run-the-application) section above.

### Hospital List

Endpoint

```text
GET /api/hospitals
```

Example of response body

```json
[
  {
    "hospitalCity": "string",
    "hospitalId": 0,
    "hospitalName": "string",
    "hospitalType": "string"
  }
]
```
