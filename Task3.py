import tkinter as tk
import string
import random

def generate_password():
    """Generates a random password based on the user-specified length."""
    try:
        # Get the desired password length from the input field
        password_length = int(length_entry.get())
        
        # Check if the length is a positive number
        if password_length <= 0:
            result_label.config(text="Please enter a positive length.", fg="red")
            return

        # Define the characters to be used for the password
        characters = string.ascii_letters + string.digits + string.punctuation

        # Generate the password by randomly selecting characters
        password = ''.join(random.choice(characters) for _ in range(password_length))

        # Display the generated password
        result_label.config(text=f"Generated Password: {password}", fg="black")

    except ValueError:
        # Handle the case where the input is not a valid number
        result_label.config(text="Invalid input. Please enter a number.", fg="red")

# Create the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.resizable(False, False)

# Create and place a heading label
heading_label = tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"))
heading_label.pack(pady=10)

# Create and place the label for password length input
length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack()

# Create and place the entry field for user input
length_entry = tk.Entry(root, width=30)
length_entry.pack(pady=5)

# Create and place the "Generate Password" button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Create and place the label to display the result
result_label = tk.Label(root, text="", font=("Courier", 12))
result_label.pack(pady=10)

# Start the main event loop
root.mainloop()
