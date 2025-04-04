#PROBLEM STATEMENT
#Python script for reading the simulation log files in a VLSI verification regression and capture the information in an Excel sheet  
#Like serial number 
#Test case name  
#status of testcase (whether pass/fail)
#if Fail , capture the UVM_ERROR /UVM_FATAL in Signature column 
#if Pass signature as NIL  
#At Last one column as comments 

#************ Motivation ************
#To achieve the task of reading simulation log files and capturing the information in an Excel sheet,we can use Python along with the pandas library for data manipulation and openpyxl or xlsxwriter for writing to Excel files. 
#Below is a Python script that demonstrates how to parse log files and write the required information to an Excel sheet.

#Before running the script, ensure you have the necessary Python packages installed as below : BASH
# pip install pandas openpyxl

#Sample Script as below

import pandas as pd

def parse_log_file(log_file):
    results = []
    with open(log_file, 'r') as file:
        test_case_name = None
        status = None
        signature = None
        comments = None
        serial_number = 1

        for line in file:
            if "Testcase:" in line:
                test_case_name = line.split("Testcase:")[1].strip()
                status = "Pass"  # Default status, will change if errors are found
                signature = "NIL"
                comments = ""

            if "UVM_ERROR" in line or "UVM_FATAL" in line:
                status = "Fail"
                signature = line.strip()

            if "End of Testcase" in line:
                results.append({
                    "Serial Number": serial_number,
                    "Test Case Name": test_case_name,
                    "Status": status,
                    "Signature": signature,
                    "Comments": comments
                })
                serial_number += 1

    return results

def write_to_excel(data, output_file):
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)

def main():
    log_file_path = "simulation.log"  # Path to your log file
    output_excel_path = "test_results.xlsx"  # Path to the output Excel file

    parsed_data = parse_log_file(log_file_path)
    write_to_excel(parsed_data, output_excel_path)
    print(f"Results written to {output_excel_path}")

if __name__ == "__main__":
    main()

#Explanation for above code
""" 
Log Parsing: The parse_log_file function reads the log file line by line. It looks for specific keywords to identify the test case name, status, and any errors. 
It assumes that each test case starts with a line containing "Testcase:" and ends with "End of Testcase".
Data Storage: The parsed information is stored in a list of dictionaries, where each dictionary represents a row in the Excel sheet.
Excel Writing: The write_to_excel function uses pandas to create a DataFrame from the list of dictionaries and writes it to an Excel file using to_excel.
Execution: The main function orchestrates the parsing and writing process, specifying the paths for the log file and the output Excel file.

##Customization
Log File Format: Adjust the parsing logic if your log file format differs. You may need to change the keywords or the way information is extracted.
Comments: You can add logic to populate the comments column based on specific conditions or additional information from the log file.
This script provides a basic framework for parsing log files and writing results to an Excel sheet, which you can expand and customize based on your specific requirements. 
"""
