import tkinter as tk

# Sample employee data
employees = {
    "John Doe": "Logistics",
    "Jane Smith": "Operations",
    "Alice Johnson": "Customer Service"
}

def check_employee():
    name = name_entry.get().strip()
    department = department_entry.get().strip()

    if name in employees and employees[name] == department:
        department_members = [emp for emp, dept in employees.items() if dept == department]
        welcome_label.config(text=f"Welcome, {name}!\n\nOther members of {department} department:\n{', '.join(department_members)}")
    else:
        welcome_label.config(text="Employee does not exist or is not in the specified department.")

# GUI setup
root = tk.Tk()
root.title("Employee Verification")
root.geometry("400x300")

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

department_label = tk.Label(root, text="Department:")
department_label.pack()
department_entry = tk.Entry(root)
department_entry.pack()

check_button = tk.Button(root, text="Check", command=check_employee)
check_button.pack()

welcome_label = tk.Label(root, text="")
welcome_label.pack()

root.mainloop()