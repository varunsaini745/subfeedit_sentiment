# FastAPI Project with Sentiment Analysis

This project is a FastAPI application that provides an endpoint for analyzing the sentiment of comments. The project includes unit tests for the API using `pytest` and `unittest.mock`.

## Table of Contents

- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)

## Installation

To set up the project, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/fastapi-sentiment-analysis.git
    cd fastapi-sentiment-analysis
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To run the FastAPI application, use the following command:

```bash
uvicorn main:app --reload
