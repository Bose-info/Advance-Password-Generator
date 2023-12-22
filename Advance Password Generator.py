from tkinter import *
from random import randint, shuffle
import emoji
import pyperclip  # Import the pyperclip module for clipboard operations

def update_emoji_var():
    emoji_var.set(1 if emoji_checkbox_value.get() else 0)

def generate_password():
    num_chars = int(entry_chars.get())
    num_emojis = int(emoji_spinbox.get()) if emoji_var.get() == 1 else 0
    
    # Generate random ASCII characters for the specified number of characters
    password_list = [chr(randint(33, 126)) for _ in range(num_chars)]
    
    # Include emojis if the checkbox is selected
    if emoji_var.get() == 1 and num_emojis > 0:
        emoji_list = ["😀", "😎", "🔒", "💡", "🚀", "🌟", "💻", "🔑", "🎉", "🔐"]
        # Select emojis randomly from the list
        random_emojis = [emoji.emojize(choice) for choice in emoji_list]
        shuffle(random_emojis)
        password_list += random_emojis[:num_emojis]
    
    shuffle(password_list)
    
    # Convert the list of characters into a string
    password = ''.join(password_list)
    
    # Update the password entry with the generated password
    pw_entry.delete(0, END)
    pw_entry.insert(0, password)

def copy_to_clipboard():
    # Get the password from the entry widget
    password = pw_entry.get()
    
    # Copy the password to the clipboard
    pyperclip.copy(password)

root = Tk()
root.title("Advance Password Generator 🔒")
root.geometry("500x400")
root.resizable(False, False)
root.configure(bg='#3498db')

# Create a label frame to hold the widgets
lf = LabelFrame(root, text="Password Settings", font=("Arial", 16, "bold"), bg='#3498db', fg='white')
lf.pack(pady=20, padx=10)

# Entry for the number of characters
entry_chars_label = Label(lf, text="Number of Characters:", font=("Arial", 12), bg='#3498db', fg='white')
entry_chars_label.grid(row=0, column=0, padx=10, pady=5)

entry_chars = Entry(lf, font=("Arial", 12))
entry_chars.grid(row=0, column=1, padx=10, pady=5)

# Checkbox to include emojis
emoji_var = IntVar(value=0)
emoji_checkbox_value = BooleanVar()
emoji_checkbox = Checkbutton(lf, text="Include Emojis", variable=emoji_checkbox_value, onvalue=True, offvalue=False, command=update_emoji_var, font=("Arial", 12), bg='#3498db', fg='white', selectcolor='#3498db')
emoji_checkbox.grid(row=1, column=0, columnspan=2, pady=5)

# Spinbox for the number of emojis
emoji_spinbox_label = Label(lf, text="Number of Emojis:", font=("Arial", 12), bg='#3498db', fg='white')
emoji_spinbox_label.grid(row=2, column=0, padx=10, pady=5)

emoji_spinbox = Spinbox(lf, from_=0, to=10, font=("Arial", 12), width=5)
emoji_spinbox.grid(row=2, column=1, padx=10, pady=5)

# Password display entry
pw_entry = Entry(root, font=("Arial", 20), bd=0, justify='center')
pw_entry.pack(pady=20)

# Generate Password button
generate_button = Button(root, text="Generate Password", command=generate_password, font=("Arial", 14, "bold"), bg='#2ecc71', fg='white', padx=10, pady=5)
generate_button.pack()

# Add some padding between the buttons
padding_label = Label(root, text="", bg='#3498db')
padding_label.pack()

# Copy to Clipboard button
copy_button = Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 14, "bold"), bg='#3498db', fg='white', padx=10, pady=5)
copy_button.pack()

root.mainloop()
