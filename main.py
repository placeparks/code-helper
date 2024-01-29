from openai import OpenAI

client = OpenAI()

def analyze_code(js_code):
    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant, skilled in analyzing JavaScript code."},
                {"role": "user", "content": js_code}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"
    
def generate_code(task_description):
    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant capable of writing code for various tasks."},
                {"role": "user", "content": task_description}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

# Ask the user for their choice
choice = input("Enter '1' for code analysis or '2' for code generation: ")

if choice == '1':
    user_code = input("Please enter your JavaScript code for analysis: ")
    print("Analysis:\n", analyze_code(user_code))
elif choice == '2':
    task_description = input("Please describe the task you want to generate code for: ")
    print("Generated Code:\n", generate_code(task_description))
else:
    print("Invalid choice. Please enter '1' or '2'.")

