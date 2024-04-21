import tkinter as tk
from tkinter import messagebox

# Callback function for the subject window form
def subject_form_callback(window):
    window.destroy()

# Function to process the form
def process_form(name, score, department):
    # Check the admission criteria
    if department.lower() == "computer science":
        open_cs_subject_window()
    elif department.lower() == "mass communication":
        open_mc_subject_window()
    else:
        messagebox.showerror("Invalid Department", "Please enter a valid department.")

# Function to process Computer Science admission
def process_computer_science(score):
    # Check if the score is sufficient and all subjects have been credited
    if int(score) >= 250 and english_credit.get() == "Yes" and maths_credit.get() == "Yes" and physics_credit.get() == "Yes" and chemistry_credit.get() == "Yes" and biology_credit.get() == "Yes":
        answer = "Accepted"
    else:
        answer = "Rejected"

    messagebox.showinfo("Answer", f"Your application has been {answer} ")

# Function to process Mass Communication admission
def process_mass_communication(score):
    # Check the admission criteria for Mass Communication
    if int(score) >= 230 and english_credit.get() == "Yes" and literature_credit.get() == "Yes" and government_credit.get() == "Yes" and history_credit.get() == "Yes":
        answer = "Accepted"
    else:
        answer = "Rejected"
    
    messagebox.showinfo("Answer", f"Your application has been {answer}")

# Function to open the subject credits window for Computer Science
def open_cs_subject_window():
    global english_credit, maths_credit, physics_credit, chemistry_credit, biology_credit
    cs_window = tk.Toplevel(root)
    cs_window.title("Computer Science Subject Credits")
    cs_window.geometry("600x400")

    english_label = tk.Label(cs_window, text="English Credit:")
    english_credit = tk.StringVar(value="No")
    english_radio_yes = tk.Radiobutton(cs_window, text="Yes", variable=english_credit, value="Yes")
    english_radio_no = tk.Radiobutton(cs_window, text="No", variable=english_credit, value="No")

    maths_label = tk.Label(cs_window, text="Maths Credit:")
    maths_credit = tk.StringVar(value="No")
    maths_radio_yes = tk.Radiobutton(cs_window, text="Yes", variable=maths_credit, value="Yes")
    maths_radio_no = tk.Radiobutton(cs_window, text="No", variable=maths_credit, value="No")

    physics_label = tk.Label(cs_window, text="Physics Credit:")
    physics_credit = tk.StringVar(value="No")
    physics_radio_yes = tk.Radiobutton(cs_window, text="Yes", variable=physics_credit, value="Yes")
    physics_radio_no = tk.Radiobutton(cs_window, text="No", variable=physics_credit, value="No")

    chemistry_label = tk.Label(cs_window, text="Chemistry Credit:")
    chemistry_credit = tk.StringVar(value="No")
    chemistry_radio_yes = tk.Radiobutton(cs_window, text="Yes", variable=chemistry_credit, value="Yes")
    chemistry_radio_no = tk.Radiobutton(cs_window, text="No", variable=chemistry_credit, value="No")

    biology_label = tk.Label(cs_window, text="Biology Credit:")
    biology_credit = tk.StringVar(value="No")
    biology_radio_yes = tk.Radiobutton(cs_window, text="Yes", variable=biology_credit, value="Yes")
    biology_radio_no = tk.Radiobutton(cs_window, text="No", variable=biology_credit, value="No")

    submit_button = tk.Button(cs_window, text="Submit", command=lambda: process_computer_science(score_entry.get()))

    english_label.pack()
    english_radio_yes.pack()
    english_radio_no.pack()
    maths_label.pack()
    maths_radio_yes.pack()
    maths_radio_no.pack()
    physics_label.pack()
    physics_radio_yes.pack()
    physics_radio_no.pack()
    chemistry_label.pack()
    chemistry_radio_yes.pack()
    chemistry_radio_no.pack()
    biology_label.pack()
    biology_radio_yes.pack()
    biology_radio_no.pack()
    submit_button.pack()

# Function to open the subject credits window for Mass Communication
def open_mc_subject_window():
    global english_credit, literature_credit, government_credit, history_credit
    mc_window = tk.Toplevel(root)
    mc_window.title("Mass Communication Subject Credits")
    mc_window.geometry("400x300")

    english_label = tk.Label(mc_window, text="English Credit:")
    english_credit = tk.StringVar(value="No")
    english_radio_yes = tk.Radiobutton(mc_window, text="Yes", variable=english_credit, value="Yes")
    english_radio_no = tk.Radiobutton(mc_window, text="No", variable=english_credit, value="No")

    literature_label = tk.Label(mc_window, text="Literature Credit:")
    literature_credit = tk.StringVar(value="No")
    literature_radio_yes = tk.Radiobutton(mc_window, text="Yes", variable=literature_credit, value="Yes")
    literature_radio_no = tk.Radiobutton(mc_window, text="No", variable=literature_credit, value="No")

    government_label = tk.Label(mc_window, text="Government Credit:")
    government_credit = tk.StringVar(value="No")
    government_radio_yes = tk.Radiobutton(mc_window, text="Yes", variable=government_credit, value="Yes")
    government_radio_no = tk.Radiobutton(mc_window, text="No", variable=government_credit, value="No")

    history_label = tk.Label(mc_window, text="History Credit:")
    history_credit = tk.StringVar(value="No")
    history_radio_yes = tk.Radiobutton(mc_window, text="Yes", variable=history_credit, value="Yes")
    history_radio_no = tk.Radiobutton(mc_window, text="No", variable=history_credit, value="No")

    submit_button = tk.Button(mc_window, text="Submit", command=lambda: process_mass_communication(score_entry.get()))

    english_label.pack()
    english_radio_yes.pack()
    english_radio_no.pack()
    literature_label.pack()
    literature_radio_yes.pack()
    literature_radio_no.pack()
    government_label.pack()
    government_radio_yes.pack()
    government_radio_no.pack()
    history_label.pack()
    history_radio_yes.pack()
    history_radio_no.pack()
    submit_button.pack()

# Main window
root = tk.Tk()
root.title("ADMISSION ELIGIBILITY CHECKER")
root.geometry("400x200")
root.configure(bg="#3E4149")

# Form fields
name_label = tk.Label(root, text="Name:", bg="#3E4149", fg="blue")
name_entry = tk.Entry(root)

score_label = tk.Label(root, text="Jamb-Score:", bg="#3E4149", fg="blue")
score_entry = tk.Entry(root)

department_label = tk.Label(root, text="Department:", bg="#3E4149", fg="blue")
department_entry = tk.Entry(root)


submit_button = tk.Button(root, text="Submit", command=lambda: process_form(name_entry.get(), score_entry.get(), department_entry.get()), bg="#4CAF50", fg="white")

#the widgets to the window
name_label.pack()
name_entry.pack()

score_label.pack()
score_entry.pack()

department_label.pack()
department_entry.pack()

submit_button.pack()


root.mainloop()

department_entry = tk.Entry(root)


submit_button = tk.Button(root, text="Submit", command=lambda: process_form(name_entry.get(), score_entry.get(), department_entry.get()), bg="#4CAF50", fg="white")

# Adding the widgets to the window
name_label.pack()
name_entry.pack()

score_label.pack()
score_entry.pack()

department_label.pack()
department_entry.pack()

submit_button.pack(pady=10)

# Start the main loop
root.mainloop()
