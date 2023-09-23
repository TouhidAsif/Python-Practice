import tkinter as tk
from tkinter import messagebox
import model
import employeedao as empdao

class EmployeeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")

        # Create and configure frames
        self.search_frame = tk.Frame(root)
        self.search_frame.pack(pady=20)
        self.result_frame = tk.Frame(root)
        self.result_frame.pack()

        # Create and configure labels and entry widgets
        self.emp_id_label = tk.Label(self.search_frame, text="Enter Employee ID:")
        self.emp_id_label.grid(row=0, column=0)
        self.emp_id_entry = tk.Entry(self.search_frame)
        self.emp_id_entry.grid(row=0, column=1)

        # Create buttons
        self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_employee)
        self.search_button.grid(row=0, column=2)
        self.exit_button = tk.Button(self.search_frame, text="Exit", command=root.quit)
        self.exit_button.grid(row=0, column=3)

        # Create and configure result text widget
        self.result_text = tk.Text(self.result_frame, height=5, width=40)
        self.result_text.pack()

    def search_employee(self):
        try:
            emp_id = int(self.emp_id_entry.get())
            ed = empdao.EmployeeDao()
            E = ed.searchEmployee(emp_id)

            if E is not None:
                result_str = f"Employee ID: {E.getid()}\nEmployee Name: {E.getname()}\nEmployee Dept: {E.getdept()}\nEmployee Salary: {E.getsalary()}"
                self.result_text.delete(1.0, tk.END)  # Clear previous results
                self.result_text.insert(tk.END, result_str)
            else:
                messagebox.showinfo("Employee Not Found", f"No employee found with ID {emp_id}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid employee ID.")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeGUI(root)
    root.mainloop()