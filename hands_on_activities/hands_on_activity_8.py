import tkinter as tk
from tkinter import ttk, messagebox
from sqlite3 import *


class EmployeeManagementSystem:
    def __init__(self, root):
        self.conn = connect("TEST.db")
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        # Dictionary to store departments and their sections
        self.dept_sections = {
            "Accounting": ["Payroll", "Fund Management"],
            "MIS": ["Computer Operation", "DB Management", "Network"],
            "Production": ["Operation", "Manufacturing"],
            "Sales": ["Marketing", "Advertisement"]
        }

        # Storage for employee data
        self.employees = []

        # Create main frames
        self.create_frames()

        # Create form elements
        self.create_form()

        # Create button panel
        self.create_buttons()

        # Create text area for displaying information
        self.create_text_area()

        self.create_database()

    def create_database(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                          (emp_id INT PRIMARY KEY,
                            name TEXT,
                            department TEXT,
                            section TEXT
                          )''')

        self.conn.commit()
        self.conn.close()

    def create_frames(self):
        # Top frame for search
        self.search_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.search_frame.pack(fill=tk.X, padx=20, pady=10)

        # Main frame for form
        self.main_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.main_frame.pack(fill=tk.BOTH, padx=20, pady=10)

        # Button frame
        self.button_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.button_frame.pack(fill=tk.X, padx=20, pady=10)

        # Text area frame
        self.text_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.text_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def create_form(self):
        # Employee Number with Search button
        tk.Label(self.main_frame, text="Employee Number:", bg="#f0f0f0", font=("Arial", 10)).grid(row=0, column=0,
                                                                                                  sticky="w", pady=5)
        self.emp_number = tk.Entry(self.main_frame, width=30)
        self.emp_number.grid(row=0, column=1, sticky="w", pady=5)

        self.search_btn = tk.Button(self.main_frame, text="SEARCH", command=self.search_employee)
        self.search_btn.grid(row=0, column=2, padx=5, pady=5)

        # Employee Name
        tk.Label(self.main_frame, text="Employee Name:", bg="#f0f0f0", font=("Arial", 10)).grid(row=1, column=0,
                                                                                                sticky="w", pady=5)
        self.emp_name = tk.Entry(self.main_frame, width=30)
        self.emp_name.grid(row=1, column=1, sticky="w", pady=5)

        # Department (Dropdown)
        tk.Label(self.main_frame, text="Department:", bg="#f0f0f0", font=("Arial", 10)).grid(row=2, column=0,
                                                                                             sticky="w", pady=5)
        self.department = ttk.Combobox(self.main_frame, width=27, state="readonly")
        self.department["values"] = list(self.dept_sections.keys())
        self.department.grid(row=2, column=1, sticky="w", pady=5)
        self.department.bind("<<ComboboxSelected>>", self.update_sections)

        # Section (Listbox)
        tk.Label(self.main_frame, text="Section:", bg="#f0f0f0", font=("Arial", 10)).grid(row=3, column=0, sticky="w",
                                                                                          pady=5)

        # Frame for listbox and scrollbar
        list_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        list_frame.grid(row=3, column=1, sticky="w", pady=5)

        # Create scrollbar
        scrollbar = tk.Scrollbar(list_frame, orient="vertical")

        # Create listbox
        self.section_listbox = tk.Listbox(list_frame, width=30, height=5, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.section_listbox.yview)

        # Pack listbox and scrollbar
        self.section_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def create_buttons(self):
        # Add Button
        self.add_btn = tk.Button(self.button_frame, text="ADD", width=10, command=self.add_employee)
        self.add_btn.pack(side=tk.LEFT, padx=5)

        # Edit Button
        self.edit_btn = tk.Button(self.button_frame, text="EDIT", width=10, command=self.edit_employee)
        self.edit_btn.pack(side=tk.LEFT, padx=5)

        # Delete Button
        self.delete_btn = tk.Button(self.button_frame, text="DELETE", width=10, command=self.delete_employee)
        self.delete_btn.pack(side=tk.LEFT, padx=5)

        # View Button
        self.view_btn = tk.Button(self.button_frame, text="VIEW", width=10, command=self.view_employees)
        self.view_btn.pack(side=tk.LEFT, padx=5)

        # Exit Button
        self.exit_btn = tk.Button(self.button_frame, text="EXIT", width=10, command=self.root.destroy)
        self.exit_btn.pack(side=tk.LEFT, padx=5)

    def create_text_area(self):
        self.text_area = tk.Text(self.text_frame, width=80, height=15)
        self.text_area.pack(fill=tk.BOTH, expand=True)
        self.text_area.config(state=tk.DISABLED)

    def update_sections(self, event=None):
        # Clear the listbox
        self.section_listbox.delete(0, tk.END)

        selected_dept = self.department.get()
        if selected_dept in self.dept_sections:
            # Populate listbox with sections for the selected department
            for section in self.dept_sections[selected_dept]:
                self.section_listbox.insert(tk.END, section)

    def add_employee(self):
        emp_num = self.emp_number.get().strip()
        emp_name = self.emp_name.get().strip()
        dept = self.department.get()

        # Check if a section is selected
        if self.section_listbox.curselection():
            section_idx = self.section_listbox.curselection()[0]
            section = self.section_listbox.get(section_idx)
        else:
            section = ""

        # Basic validation
        if not emp_num or not emp_name or not dept or not section:
            messagebox.showerror("Error", "All fields are required!")
            return

        # Check if employee number already exists
        for emp in self.employees:
            if emp["number"] == emp_num:
                messagebox.showerror("Error", "Employee number already exists!")
                return

        # Add employee to the list
        employee = {
            "number": emp_num,
            "name": emp_name,
            "department": dept,
            "section": section
        }

        self.employees.append(employee)
        messagebox.showinfo("Success", "Employee added successfully!")
        self.clear_form()
        self.view_employees()

    def search_employee(self):
        emp_num = self.emp_number.get().strip()

        if not emp_num:
            messagebox.showerror("Error", "Please enter an employee number to search!")
            return

        found = False
        for emp in self.employees:
            if emp["number"] == emp_num:
                self.emp_name.delete(0, tk.END)
                self.emp_name.insert(0, emp["name"])

                self.department.set(emp["department"])
                self.update_sections()

                # Select the matching section in the listbox
                for i in range(self.section_listbox.size()):
                    if self.section_listbox.get(i) == emp["section"]:
                        self.section_listbox.selection_set(i)
                        break

                found = True
                break

        if not found:
            messagebox.showinfo("Not Found", "No employee found with the given number!")

    def edit_employee(self):
        emp_num = self.emp_number.get().strip()

        if not emp_num:
            messagebox.showerror("Error", "Please enter an employee number to edit!")
            return

        emp_name = self.emp_name.get().strip()
        dept = self.department.get()

        # Check if a section is selected
        if self.section_listbox.curselection():
            section_idx = self.section_listbox.curselection()[0]
            section = self.section_listbox.get(section_idx)
        else:
            section = ""

        # Basic validation
        if not emp_name or not dept or not section:
            messagebox.showerror("Error", "All fields are required!")
            return

        found = False
        for i, emp in enumerate(self.employees):
            if emp["number"] == emp_num:
                self.employees[i] = {
                    "number": emp_num,
                    "name": emp_name,
                    "department": dept,
                    "section": section
                }
                found = True
                messagebox.showinfo("Success", "Employee updated successfully!")
                self.clear_form()
                self.view_employees()
                break

        if not found:
            messagebox.showinfo("Not Found", "No employee found with the given number!")

    def delete_employee(self):
        emp_num = self.emp_number.get().strip()

        if not emp_num:
            messagebox.showerror("Error", "Please enter an employee number to delete!")
            return

        found = False
        for i, emp in enumerate(self.employees):
            if emp["number"] == emp_num:
                confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete employee {emp_num}?")
                if confirm:
                    del self.employees[i]
                    messagebox.showinfo("Success", "Employee deleted successfully!")
                    self.clear_form()
                    self.view_employees()
                found = True
                break

        if not found:
            messagebox.showinfo("Not Found", "No employee found with the given number!")

    def view_employees(self):
        self.text_area.config(state=tk.NORMAL)
        self.text_area.delete(1.0, tk.END)

        if not self.employees:
            self.text_area.insert(tk.END, "No employees found.")
        else:
            header = f"{'Number':<15}{'Name':<30}{'Department':<15}{'Section':<30}\n"
            self.text_area.insert(tk.END, header)
            self.text_area.insert(tk.END, "-" * 90 + "\n")

            for emp in self.employees:
                line = f"{emp['number']:<15}{emp['name']:<30}{emp['department']:<15}{emp['section']:<30}\n"
                self.text_area.insert(tk.END, line)

        self.text_area.config(state=tk.DISABLED)

    def clear_form(self):
        self.emp_number.delete(0, tk.END)
        self.emp_name.delete(0, tk.END)
        self.department.set("")
        self.section_listbox.delete(0, tk.END)


# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagementSystem(root)
    root.mainloop()