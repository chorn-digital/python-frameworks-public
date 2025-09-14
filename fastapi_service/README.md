# Python FastApi Api Project

## Project structure

```
project-root/
│── requirements.txt
│── __init__.py
│── fastapi_service/
│   ├── __init__.py
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py          # FastAPI app entrypoint
│   │   ├── config/
│   │   │   ├── __init__.py
│   │   │   └── database.py  # DB setup
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── post_model.py  # SQLAlchemy models
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   └── post_schema.py # Pydantic schemas
│   │   ├── repositories/
│   │   │   ├── __init__.py
│   │   │   └── post_repository.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   └── post_service.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       └── post_routes.py

```

```