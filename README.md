# SecOps Task - CVE Management Flask Application

This project is a Flask-based web application for managing CVE (Common Vulnerabilities and Exposures) records. It allows users to add, retrieve, update, and delete CVE records through a RESTful API.

## Table of Contents

- [SecOps Task - CVE Management Flask Application](#secops-task---cve-management-flask-application)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
  - [API Endpoints](#api-endpoints)
  - [Error Handling](#error-handling)
  - [Additional Information](#additional-information)
  - [License](#license)
  - [Contact](#contact)

## Overview

This application provides an interface to manage CVE records stored in an SQLite database. The data is initially loaded from a CSV file.

## Prerequisites

- Python 3.x
- `pip` (Python package installer)

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/hilalibrahim/SecOps.git
    cd SecOps
    ```

2. **Install the required packages**:

    ```sh
    pip install Flask
    ```

3. **Import the data from the CSV file**:

    Ensure `CVE_DATABASE.csv` is in the same directory as `import_data.py`.

    ```sh
    python import_data.py
    ```

## Running the Application

1. Ensure `cve_database.db` is in the same directory as `app.py`.
2. Run the Flask application:

    ```sh
    python app.py
    ```

   The application will be available at `http://127.0.0.1:5000/`.

## API Endpoints

- **Retrieve a specific CVE by ID**:
  - **GET** `/cve/<cve_id>`
  - Example: `GET /cve/CVE-2021-1234`
  - Response: Details of the specified CVE or an error message if not found.

- **Retrieve all CVEs**:
  - **GET** `/cve/all`
  - Example: `GET /cve/all`
  - Response: A list of all CVEs.

- **Add a new CVE**:
  - **POST** `/cve/addCVE`
  - Request Body:
    ```json
    {
      "cve_id": "CVE-2021-1234",
      "description": "Description of the CVE",
      "severity": "High",
      "cvss": 7.5,
      "affected_packages": "package1, package2",
      "cwe_id": "CWE-79"
    }
    ```
  - Response: Confirmation message.

- **Delete a CVE by ID**:
  - **DELETE** `/cve/<cve_id>`
  - Example: `DELETE /cve/CVE-2021-1234`
  - Response: Confirmation message or an error message if not found.

- **Update a CVE by ID**:
  - **PUT** `/cve/<cve_id>`
  - Request Body:
    ```json
    {
      "description": "Updated description",
      "severity": "Medium",
      "cvss": 5.0,
      "affected_packages": "package1, package3",
      "cwe_id": "CWE-89"
    }
    ```
  - Example: `PUT /cve/CVE-2021-1234`
  - Response: Confirmation message or an error message if not found.

## Error Handling

- Appropriate error messages are returned if the specified CVE ID does not exist or if there are validation errors in the payload data.

## Additional Information

- The database is an SQLite database named `cve_database.db`.
- The CSV file used for initial data import is named `CVE_DATABASE.csv`.
- The Flask application code is in `app.py`.
- The data import script is in `import_data.py`.


## Contact

For any issues or inquiries, please contact [Hilal Ibrahim](https://github.com/hilalibrahim).
