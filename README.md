Employee Salary Filter - Azure Function
This project contains an Azure Function App designed to filter employee records based on a specified salary threshold. The application is configured to run on the Python worker runtime.  
PY
+ 1

Prerequisites and Dependencies
Python environment set up for Azure Functions.  
JSON

azure-functions library for function app capabilities.  
TXT

pandas for data manipulation.  
TXT

openpyxl engine to read Excel data.  
TXT

An AzureWebJobsStorage configuration utilizing local development storage.  
JSON

File Structure and Configuration
function_app.py: Contains the main routing and logic for the HTTP trigger.  
PY

local.settings.json: Configures local development environment variables and runtime definitions.  
JSON

requirements.txt: Lists the required Python packages for deployment.  
TXT

host.json: Specifies configuration settings for the Azure Functions host, including Application Insights sampling and the Extension Bundle version.  
JSON

employee_data.xlsx: The function reads data directly from this Excel file using the openpyxl engine.  
PY

Note: The current code contains a hardcoded file path (C:\Users\pramathi.gupta\Desktop\EmployeeFunctionApp\employee_data.xlsx) that must be updated or mapped correctly on your local machine for the function to locate employee_data.xlsx.  
PY

API Endpoint: GetEmployeesBySalary
The application exposes a single HTTP endpoint configured with an anonymous authentication level.  
PY

Request
Route: GetEmployeesBySalary.  
PY

Content-Type: Expected to be JSON, as the function parses the request body using req.get_json().  
PY

Body: A JSON object containing a max_salary key.  
PY

Responses
Success (200 OK): Returns a JSON-formatted list of employee records (using the records orientation) where the salary is strictly greater than the provided max_salary.  
PY

Bad Request (400): Returned with the message "Please provide max_salary" if the parameter is missing.  
PY

Server Error (500): Returned with the error string if any exception occurs during processing.  
PY

Known Issues
Code Defect Warning: There is a typographical error in the function_app.py script where the extracted variable from the JSON body is named man_salary (man_salary = req_body.get("max_salary")). However, the subsequent validation and dataframe filtering logic check against an undefined max_salary variable. This must be corrected to max_salary = req_body.get("max_salary") for the function to execute successfully.  
PY
+ 1
