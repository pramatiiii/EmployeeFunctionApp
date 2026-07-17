# 💼 Employee Salary Filter API

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Azure Functions](https://img.shields.io/badge/Azure_Functions-v4-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![OpenPyXL](https://img.shields.io/badge/OpenPyXL-217346?style=for-the-badge)

A **serverless REST API** built with **Python**, **Azure Functions**, and **Pandas** that reads employee information from an Excel spreadsheet and returns employees whose salaries are greater than a specified threshold.

---

## 📑 Table of Contents

- Overview
- Features
- Tech Stack
- Project Structure
- Getting Started
- Running the Application
- API Documentation
- Example Request
- Example Response
- Future Improvements
- Author

---

# 📖 Overview

Employee Salary Filter API is a lightweight backend application developed using **Azure Functions**.

Instead of manually searching through Excel files, the API automatically filters employee records based on a salary threshold and returns the results in JSON format.

This project demonstrates:

- Azure Functions
- Serverless Backend Development
- REST API Development
- Excel Data Processing
- JSON Response Handling
- Python Data Analysis with Pandas

---

# ✨ Features

- 🚀 Serverless architecture using Azure Functions
- 📊 Reads employee data from an Excel (.xlsx) file
- 🔍 Filters employees based on salary
- 📄 Returns results in JSON format
- ⚡ Fast data processing with Pandas
- 💻 Easy to run locally
- ☁️ Ready for Azure deployment

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| Azure Functions | Serverless Computing |
| Pandas | Data Processing |
| OpenPyXL | Reading Excel Files |
| JSON | API Response Format |
| Azure Functions Core Tools | Local Development |

---

# 📂 Project Structure

```
employee-salary-filter/
│
├── function_app.py          # Azure Function logic
├── employee_data.xlsx       # Employee dataset
├── requirements.txt         # Python dependencies
├── host.json                # Azure Functions configuration
├── local.settings.json      # Local settings (not committed)
└── README.md
```

---

# 🚀 Getting Started

## Prerequisites

Install the following before running the project:

- Python 3.8+
- Git
- Azure Functions Core Tools
- Visual Studio Code (Recommended)

---

## Clone the Repository

```bash
git clone https://github.com/your-username/employee-salary-filter.git

cd employee-salary-filter
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Start the Azure Function locally:

```bash
func start
```

The API will run at:

```
http://localhost:7071
```

---

# 📡 API Documentation

## Endpoint

```
GET /api/filterEmployees
```

---

## Query Parameter

| Parameter | Type | Description |
|-----------|------|-------------|
| salary | Integer | Minimum salary threshold |

---

# 📥 Example Request

```
GET http://localhost:7071/api/filterEmployees?salary=60000
```

---

# 📤 Example Response

```json
[
  {
    "EmployeeID": 101,
    "Name": "Alice Johnson",
    "Department": "Engineering",
    "Salary": 75000
  },
  {
    "EmployeeID": 104,
    "Name": "John Smith",
    "Department": "Finance",
    "Salary": 82000
  }
]
```

---

# ⚙️ How It Works

```
Client Request
      │
      ▼
Azure Function HTTP Trigger
      │
      ▼
Read Excel File
      │
      ▼
Load Data Using Pandas
      │
      ▼
Filter Employees
      │
      ▼
Convert Results to JSON
      │
      ▼
Return Response
```

---

# 📦 Dependencies

- Azure Functions
- Pandas
- OpenPyXL

Install all packages using:

```bash
pip install -r requirements.txt
```

---

# 🔮 Future Improvements

- Azure SQL Database integration
- Department filtering
- Sorting support
- Pagination
- Authentication
- Swagger/OpenAPI documentation
- Unit testing
- Docker support
- CI/CD with GitHub Actions

---

# 👨‍💻 Author

**Pramati Gupta**

GitHub: https://github.com/pramatiiii

LinkedIn: https://www.linkedin.com/in/pramati-gupta-5b0b26321/

---

## ⭐ Support

If you found this project helpful, consider giving it a **⭐ Star** on GitHub.
