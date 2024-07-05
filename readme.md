# Basic Flask App with CRUD Operations

This repository contains a basic Flask web application demonstrating CRUD (Create, Read, Update, Delete) operations using an SQLite database.

## Features

- Create, Read, Update, and Delete records
- Simple and clean web interface using HTML templates
- SQLite database for data storage

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Ritik-1101/Basic-Flask-App-CRUD.git
    cd Basic-Flask-App-CRUD
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```sh
    python run.py
    ```

2. Open your browser and navigate to `http://127.0.0.1:5000` to access the application.

## Project Structure

- `app/` - Contains the main application files.
- `templates/` - HTML templates for the web interface.
- `static/` - Static files (CSS, JS, images).
- `db.sqlite` - SQLite database file.
- `run.py` - Main script to start the Flask application.
- `requirements.txt` - List of dependencies.
