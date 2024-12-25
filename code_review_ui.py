import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

class CodeReviewApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Automated Code Review Assistant")
        self.root.geometry("500x400")

        # Label
        self.label = tk.Label(root, text="Choose Python Script for Review", font=("Helvetica", 14))
        self.label.pack(pady=20)

        # Browse Button
        self.browse_button = tk.Button(root, text="Browse Script", command=self.browse_file, font=("Helvetica", 12))
        self.browse_button.pack(pady=10)

        # Review Button
        self.review_button = tk.Button(root, text="Review Script", command=self.review_code, state="disabled", font=("Helvetica", 12))
        self.review_button.pack(pady=10)

        # Textbox for displaying the review results
        self.result_text = tk.Text(root, height=10, width=50, wrap="word", font=("Helvetica", 10))
        self.result_text.pack(pady=20)

        # File path variable
        self.file_path = ""

    def browse_file(self):
        # Open file dialog to choose the script file
        self.file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])

        if self.file_path:
            self.review_button.config(state="normal")  # Enable the review button if a file is selected

    def review_code(self):
        # Run the pylint command on the selected file
        if not self.file_path:
            messagebox.showerror("Error", "Please select a Python script to review!")
            return
        
        try:
            # Run pylint on the selected script file
            result = subprocess.run(['pylint', self.file_path], capture_output=True, text=True)
            self.display_review(result.stdout)
        except FileNotFoundError:
            messagebox.showerror("Error", "pylint is not installed. Please install it using `pip install pylint`.")

    def display_review(self, review_text):
        # Display the review results in the textbox
        self.result_text.delete(1.0, tk.END)  # Clear previous results
        self.result_text.insert(tk.END, review_text)  # Insert the new review text

# Create the main window
root = tk.Tk()
app = CodeReviewApp(root)

# Start the Tkinter event loop
root.mainloop()
