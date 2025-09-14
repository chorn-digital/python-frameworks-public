# Fast API Service

## Project structure

```
project-root/
│── flask_service/
│   ├── __init__.py
│   ├── app/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── extensions.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── post_model.py
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   └── post_schema.py
│   │   ├── repositories/
│   │   │   ├── __init__.py
│   │   │   └── post_repository.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   └── post_service.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   └── post_routes.py
│   │   └── factory.py  # create_app() here
│   ├── wsgi.py
│
│── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_v1_posts.py

```

## Using

```markdown
# Flask Project 🚀

**Flask REST API** project using:

- **Application Factory Pattern**
- **Blueprints** with versioning (`/api/v1` and `/api/v2`)
- **Flask-SQLAlchemy** + **Flask-Migrate** (DB migrations)
- **Pytest** with CI/CD (GitHub Actions)

---