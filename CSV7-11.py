import csv
import re

def validate_email(email):
    # Regular expression for validating an Email
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

def display_csv_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            
            # Assuming the CSV structure is: Name,Email
            for row in reader:
                name = row[0]
                email = row[1]

                # Validate the email using the defined function
                if validate_email(email):
                    print(f"Name: {name}, Email: {email} (Valid)")
                else:
                    print(f"Name: {name}, Email: {email} (Invalid)")

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = 'friends.csv'  # Replace with the actual path to your CSV file
display_csv_contents(file_path)