import tkinter as tk
from tkinter import messagebox
import model
import employeedao as empdao

class EmployeeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")

        # Create and configure frames
        self.insert_frame = tk.Frame(root)
        self.insert_frame.pack(pady=20)
        self.update_frame = tk.Frame(root)
        self.update_frame.pack(pady=20)
        self.delete_frame = tk.Frame(root)
        self.delete_frame.pack(pady=20)
        self.search_frame = tk.Frame(root)
        self.search_frame.pack()
        self.result_frame = tk.Frame(root)
        self.result_frame.pack()

        # Create and configure labels and entry widgets for insert
        self.insert_id_label = tk.Label(self.insert_frame, text="Employee ID:")
        self.insert_id_label.grid(row=0, column=0)
        self.insert_id_entry = tk.Entry(self.insert_frame)
        self.insert_id_entry.grid(row=0, column=1)
        self.insert_name_label = tk.Label(self.insert_frame, text="Employee Name:")
        self.insert_name_label.grid(row=1, column=0)
        self.insert_name_entry = tk.Entry(self.insert_frame)
        self.insert_name_entry.grid(row=1, column=1)
        self.insert_dept_label = tk.Label(self.insert_frame, text="Employee Dept:")
        self.insert_dept_label.grid(row=2, column=0)
        self.insert_dept_entry = tk.Entry(self.insert_frame)
        self.insert_dept_entry.grid(row=2, column=1)
        self.insert_salary_label = tk.Label(self.insert_frame, text="Employee Salary:")
        self.insert_salary_label.grid(row=3, column=0)
        self.insert_salary_entry = tk.Entry(self.insert_frame)
        self.insert_salary_entry.grid(row=3, column=1)
        self.insert_button = tk.Button(self.insert_frame, text="Insert", command=self.insert_employee)
        self.insert_button.grid(row=4, column=0, columnspan=2)

        # Create and configure labels and entry widgets for update
        self.update_id_label = tk.Label(self.update_frame, text="Employee ID:")
        self.update_id_label.grid(row=0, column=0)
        self.update_id_entry = tk.Entry(self.update_frame)
        self.update_id_entry.grid(row=0, column=1)
        self.update_search_button = tk.Button(self.update_frame, text="Search", command=self.search_employee_for_update)
        self.update_search_button.grid(row=0, column=2)
        self.update_name_label = tk.Label(self.update_frame, text="Employee Name:")
        self.update_name_label.grid(row=1, column=0)
        self.update_name_entry = tk.Entry(self.update_frame)
        self.update_name_entry.grid(row=1, column=1)
        self.update_dept_label = tk.Label(self.update_frame, text="Employee Dept:")
        self.update_dept_label.grid(row=2, column=0)
        self.update_dept_entry = tk.Entry(self.update_frame)
        self.update_dept_entry.grid(row=2, column=1)
        self.update_salary_label = tk.Label(self.update_frame, text="Employee Salary:")
        self.update_salary_label.grid(row=3, column=0)
        self.update_salary_entry = tk.Entry(self.update_frame)
        self.update_salary_entry.grid(row=3, column=1)
        self.update_button = tk.Button(self.update_frame, text="Update", command=self.update_employee)
        self.update_button.grid(row=4, column=0, columnspan=2)


        # Create and configure labels and entry widgets for delete
        self.delete_id_label = tk.Label(self.delete_frame, text="Employee ID:")
        self.delete_id_label.grid(row=0, column=0)
        self.delete_id_entry = tk.Entry(self.delete_frame)
        self.delete_id_entry.grid(row=0, column=1)
        self.delete_button = tk.Button(self.delete_frame, text="Delete", command=self.delete_employee)
        self.delete_button.grid(row=1, column=0, columnspan=2)

        # Create and configure labels and entry widgets for search
        self.search_id_label = tk.Label(self.search_frame, text="Enter Employee ID:")
        self.search_id_label.grid(row=0, column=0)
        self.search_id_entry = tk.Entry(self.search_frame)
        self.search_id_entry.grid(row=0, column=1)
        self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_employee)
        self.search_button.grid(row=0, column=2)
        self.search_all_button = tk.Button(self.search_frame, text="Search All", command=self.search_all_employees)
        self.search_all_button.grid(row=0, column=3)

        # Create and configure result text widget
        self.result_text = tk.Text(self.result_frame, height=10, width=40)
        self.result_text.pack()

    def insert_employee(self):
        try:
            emp_id = int(self.insert_id_entry.get())
            emp_name = self.insert_name_entry.get()
            emp_dept = self.insert_dept_entry.get()
            emp_salary = int(self.insert_salary_entry.get())

            E = model.Employee()
            E.setid(emp_id)
            E.setname(emp_name)
            E.setdept(emp_dept)
            E.setsalary(emp_salary)

            ed = empdao.EmployeeDao()
            ed.insertEmployee(E)

            messagebox.showinfo("Insert Successful", "Employee record inserted successfully.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid employee details.")

    def search_employee_for_update(self):
        try:
            emp_id = int(self.update_id_entry.get())
            ed = empdao.EmployeeDao()
            E = ed.searchEmployee(emp_id)

            if E is not None:
                self.update_name_entry.delete(0, tk.END)
                self.update_dept_entry.delete(0, tk.END)
                self.update_salary_entry.delete(0, tk.END)
                self.update_name_entry.insert(0, E.getname())
                self.update_dept_entry.insert(0, E.getdept())
                self.update_salary_entry.insert(0, E.getsalary())
                self.result_text.delete(1.0, tk.END)  # Clear previous results
            else:
                messagebox.showinfo("Employee Not Found", f"No employee found with ID {emp_id}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid employee ID.")

    def update_employee(self):
        try:
            emp_id = int(self.update_id_entry.get())
            emp_name = self.update_name_entry.get()
            emp_dept = self.update_dept_entry.get()
            emp_salary = int(self.update_salary_entry.get())

            E = model.Employee()
            E.setid(emp_id)
            E.setname(emp_name)
            E.setdept(emp_dept)
            E.setsalary(emp_salary)

            ed = empdao.EmployeeDao()
            ed.updateEmployee(E)

            messagebox.showinfo("Update Successful", "Employee record updated successfully.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid employee details.")

    def delete_employee(self):
        try:
            emp_id = int(self.delete_id_entry.get())

            ed = empdao.EmployeeDao()
            E = ed.searchEmployee(emp_id)

            if E is not None:
                choice = messagebox.askyesno("Confirm Deletion", f"Do you want to delete the employee with ID {emp_id}?")
                if choice:
                    ed.deleteEmployee(emp_id)
                    messagebox.showinfo("Delete Successful", f"Employee with ID {emp_id} deleted successfully.")
            else:
                messagebox.showinfo("Employee Not Found", f"No employee found with ID {emp_id}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid employee ID.")

    def search_employee(self):
        try:
            emp_id = int(self.search_id_entry.get())
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

    def search_all_employees(self):
        ed = empdao.EmployeeDao()
        employee_list = ed.searchAll()

        if employee_list:
            result_str = ""
            for emp in employee_list:
                result_str += f"Employee ID: {emp.getid()}\nEmployee Name: {emp.getname()}\nEmployee Dept: {emp.getdept()}\nEmployee Salary: {emp.getsalary()}\n\n"
            self.result_text.delete(1.0, tk.END)  # Clear previous results
            self.result_text.insert(tk.END, result_str)
        else:
            messagebox.showinfo("No Employees Found", "No employee records found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeGUI(root)
    root.mainloop()
