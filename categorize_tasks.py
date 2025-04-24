import csv
import requests
import json
import ast

# Your Gemini API key
GEMINI_API_KEY = 'YOUR-GEMINI-API'

# The API endpoint for Gemini
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=" + GEMINI_API_KEY

# Function to categorize multiple tasks using Gemini API
def categorize_tasks(tasks):
    # Create a single prompt with all uncategorized tasks
    tasks_prompt = "\n".join([f"Task: '{task}'" for task in tasks])

    # Prepare the request data (send all tasks as a single prompt)
    data = {
        "contents": [
            {
                "parts": [{"text": f"Identify at most 7 categories for the following tasks, and provide\
                         the tasks and categories in a hashmap, where the keys are the tasks, and the \
                         values are the categories (do not use special formatting).\
                          Avoid saying anything else:\n{tasks_prompt}"}]
            }
        ]
    }

    # Headers for the request
    headers = {
        'Content-Type': 'application/json'
    }

    # Send the POST request to the Gemini API
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        response_json = response.json()
        # Extract the generated content (assumed to be in 'text')
        generated_text = response_json["candidates"][0]["content"]["parts"][0]["text"]
        return generated_text
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

# Function to load uncategorized tasks from a CSV file
def load_tasks(csv_path):
    """Load tasks from the CSV and return a list of uncategorized tasks."""
    tasks = []
    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) != 3:  # Skip malformed rows
                continue
            _, task, elapsed = row
            tasks.append(task)
    return tasks

# Function to categorize all tasks from the CSV and log them
def categorize_all_tasks(csv_path):
    tasks = load_tasks(csv_path)

    # Send all uncategorized tasks for categorization
    print("\nSending all tasks for categorization...")
    categorized_content = categorize_tasks(tasks)

    if categorized_content:
        print("\nCategorized Tasks:\n")
        print(categorized_content)
        return ast.literal_eval(categorized_content)
    else:
        print("\nNo categorization response received.")

def save_tasks_with_categories(input_csv, output_csv, categorized_tasks):
    with open(input_csv, newline='') as infile, open(output_csv, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        
        # Write data with categories
        for row in reader:
            task = row[1]
            category = categorized_tasks.get(task, "Uncategorized")  # Default to "Uncategorized" if no match
            row.append(category)
            writer.writerow(row)

# Main execution
if __name__ == "__main__":
    input_path = "data.csv"  # Path to your original CSV file
    output_path = "categorized_data.csv"  # Path to save the new CSV with categories

    # Categorize tasks and get the results
    categorized_tasks = categorize_all_tasks(input_path)

    if categorized_tasks:
        # Save tasks with their respective categories into a new CSV
        save_tasks_with_categories(input_path, output_path, categorized_tasks)
        print(f"\nThe tasks with categories have been saved to '{output_path}'.")

