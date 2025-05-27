# FastAPI API Project

This project is a FastAPI application that provides various endpoints related to regulations, rule evaluation, and compliance checking.

## Project Structure

```
fastapi-api
├── src
│   ├── main.py                # Entry point of the application
│   ├── api                    # Contains API route definitions
│   │   ├── __init__.py        # Initializes the API package
│   │   ├── regulations.py      # Endpoints for regulations
│   │   ├── rule_engine.py      # Endpoints for rule evaluation
│   │   └── compliance.py       # Endpoints for compliance checking
│   └── models                 # Contains data models or schemas
│       └── __init__.py        # Initializes the models package
├── requirements.txt           # Lists project dependencies
└── README.md                  # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fastapi-api
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   uvicorn src.main:app --reload
   ```

## Usage

- Access the API documentation at `http://127.0.0.1:8000/docs` after running the application.
- The following endpoints are available:
  - **Regulations**
    - `GET /regulations/{regulation_id}/sections/{section_id}`
    - `GET /regulations/search?query="CUI Basic"&classification_level="secret"`
  - **Rule Engine**
    - `POST /evaluate/classification`
    - `POST /evaluate/handling_requirements`
    - `POST /evaluate/marking_requirements`
  - **Compliance**
    - `POST /check/document_compliance`
    - `GET /requirements/by_classification/{level}`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.