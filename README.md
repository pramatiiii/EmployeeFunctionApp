# Employee Salary Filter API

A serverless backend application built with Python and Azure Functions. This API reads employee data from a local Excel spreadsheet and returns a filtered list of employees whose salaries exceed a specified threshold.

## Table of Contents
* Features
* Project Structure
* Local Development Setup
* API Documentation
* Important Bug Fixes Needed

---

## Features
* **Serverless Architecture:** Utilizes Azure Functions (v4 programming model) for easy scaling and deployment.
* **Data Processing:** Uses pandas and openpyxl to efficiently parse and filter .xlsx files.
* **RESTful Endpoint:** Provides a simple HTTP trigger to fetch filtered JSON data.

---

## Project Structure

* `function_app.py`: The core application logic and HTTP route definition.
* `local.settings.json`: Environment variables and local runtime configuration (ignored by version control).
* `requirements.txt`: Python dependencies required to run the app.
* `host.json`: Global configuration options for the Azure Functions host.
* `employee_data.xlsx`: The source data file containing employee records.

---

## Local Development Setup

Follow these steps to run the backend locally. 

**1. Install Prerequisites**
Ensure you have Python 3.8 or newer installed on your system. You will also need the Azure Functions Core Tools installed locally to run the `func` commands.

**2. Clone the Repository**
```bash
git clone <your-repository-url>
cd employee-salary-filter
