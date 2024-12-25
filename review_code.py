import subprocess
import sys

def review_code(file_path):
    try:
        # Run pylint on the provided file and capture the output
        result = subprocess.run(['pylint', file_path], capture_output=True, text=True)
        print(result.stdout)  # Output the review results
    except FileNotFoundError:
        print("pylint is not installed. Please install it using `pip install pylint`.")

if __name__ == "__main__":
    # Set a default script to review (you can change this to any script you want)
    default_script = "my_script.py"

    # Check if the file exists
    try:
        with open(default_script, "r"):
            pass
    except FileNotFoundError:
        print(f"The script '{default_script}' was not found. Please ensure the file exists.")
    else:
        review_code(default_script)
