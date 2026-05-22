# QuickTasker

A minimal task manager API built with **FastAPI**. The project showcases:

- In‑memory CRUD for tasks
- OpenAPI docs at `/docs`
- Dockerfile ready for container builds
- GitHub Actions CI/CD pipeline with linting, testing, and security scanning

## Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Run the API (development mode)
uvicorn main:app --reload
```

The API will be reachable at `http://127.0.0.1:8000`. Browse the interactive docs at `http://127.0.0.1:8000/docs`.

## Running Tests

```bash
pip install pytest httpx
pytest
```

## CI/CD

The repository includes a GitHub Actions workflow (`.github/workflows/ci.yml`) that runs on every push and pull request. It performs:

- Dependency installation
- Linting with **ruff**
- Unit tests with **pytest**
- Static analysis with **CodeQL**

## License

MIT License – see the `LICENSE` file.
