# Python FastApi Api Project

The FastAPI API Project is a high-performance, asynchronous RESTful API application built using FastAPI, designed for
managing post data with complete CRUD functionality. It features a `Post` model for representing post data, with fields
for `userId`, `title`, and `body`, defined using SQLAlchemy. Pydantic schemas are used for data validation and
serialization, while CRUD operations are implemented through dedicated functions. The API endpoints, accessible
via `/posts/`, support creating, reading, updating, and deleting posts. Utilizing FastAPI's efficiency and asynchronous
capabilities, this project ensures a fast, scalable, and maintainable API, suitable for modern web applications.

## Setup Project

```
mkdir fastapi-api
cd fastapi-api
python -m venv venv
```

## Install FastAPI and Other Dependencies

```
pip install fastapi
pip install uvicorn
pip install sqlalchemy
pip install databases
pip install pydantic
```