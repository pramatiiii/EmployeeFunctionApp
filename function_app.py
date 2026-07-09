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

        man_salary = req_body.get("max_salary")

        if max_salary is None:
            return func.HttpResponse(
                "Please provide max_salary",
                status_code=400
            )

        file_path = r"C:\Users\pramathi.gupta\Desktop\EmployeeFunctionApp\employee_data.xlsx"
        print(file_path)

        df = pd.read_excel(file_path, engine="openpyxl")

        filtered_df = df[df["Salary"] > max_salary]

        employees = filtered_df.to_dict(orient="records")

        return func.HttpResponse(
            json.dumps(employees),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        return func.HttpResponse(
            str(e),
            status_code=500
        )