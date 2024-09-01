import tkinter as tk
from tkinter import messagebox
def register():
    Name = entry_name.get()
    Phone = entry_name.get()
    Gender = entry_name.get()
    Email = entry_name.get()
    Password = entry_name.get()

    if Name and Phone and Gender and Email and Password:
        messagebox.showinfo("Success", "Registration Successful!")
    else:
        messagebox.showerror("Error", "All fields are required!")

root = tk.Tk()
root.title("Registration Form")
root.geometry("300x270")
root.resizable(False,False)

tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Phone").grid(row=1, column=0, padx=10, pady=10)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Gender").grid(row=2, column=0, padx=10, pady=10)
entry_name = tk.Entry(root)
entry_name.grid(row=2, column=1, padx=10, pady=10)


tk.Label(root, text="Email").grid(row=3, column=0, padx=10, pady=10)
entry_email = tk.Entry(root)
entry_email.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="Password").grid(row=4, column=0, padx=10, pady=10)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=4, column=1, padx=10, pady=10)

Register_button = tk.Button(root, text="Register", command=register)
Register_button.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()