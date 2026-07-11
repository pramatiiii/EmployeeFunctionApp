import azure.functions as func
import pandas as pd
import json
import logging
import os

app = func.FunctionApp()

@app.route(route="GetEmployeesBySalary", auth_level=func.AuthLevel.ANONYMOUS)
def GetEmployeesBySalary(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing employee salary request")

    try:
        req_body = req.get_json()
        
        # FIXED: Corrected variable name to max_salary
        max_salary = req_body.get("max_salary")

        if max_salary is None:
            return func.HttpResponse(
                "Please provide max_salary in the request body.",
                status_code=400
            )

        # FIXED: Using a relative path to ensure it works across environments
        file_path = os.path.join(os.path.dirname(__file__), "employee_data.xlsx")
        logging.info(f"Accessing file at: {file_path}")

        if not os.path.exists(file_path):
             return func.HttpResponse(
                "Employee data file not found on the server.",
                status_code=500
            )

        df = pd.read_excel(file_path, engine="openpyxl")

        filtered_df = df[df["Salary"] > max_salary]

        employees = filtered_df.to_dict(orient="records")

        return func.HttpResponse(
            json.dumps(employees),
            mimetype="application/json",
            status_code=200
        )

    except ValueError:
        return func.HttpResponse(
            "Invalid JSON format or incorrect data types provided.",
            status_code=400
        )
    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")
        return func.HttpResponse(
            f"An internal error occurred: {str(e)}",
            status_code=500
        )
