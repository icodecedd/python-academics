from sqlite3 import *
from tkinter import *
from tkinter import messagebox

# Initialize database
def init_db():
    conn = connect('employee.db')
    cursor = conn.cursor()
    # cursor.execute('drop table employees')
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                     (emp_id INT PRIMARY KEY, 
                      name TEXT, 
                      status TEXT, 
                      position TEXT, 
                      salary REAL)''')

    conn.commit()
    conn.close()

# Salary mapping
salary_mapping = {
    "Clerk": 20000,
    "Accountant": 25000,
    "Sales Manager": 45000,
    "Production Staff": 22000,
    "Project Manager": 50000
}

def update_salary(*args):
    position = position_var.get()
    salary = salary_mapping.get(position, 0)
    salary_text.config(state=NORMAL)
    salary_text.delete(1.0, END)
    salary_text.insert(END, f"{salary:,.2f}")
    salary_text.config(state=DISABLED)

def clear_fields():

    emp_number_entry.delete(0, END)
    emp_name_entry.delete(0, END)
    status_var.set("Permanent")
    position_var.set("")  # This will trigger salary update automatically

# Main application
if __name__ == "__main__":
    # Initialize database
    init_db()

    root = Tk()

    # Employee Information Section
    Label(root, text="Employee Number:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    emp_number_entry = Entry(root)
    emp_number_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    def search_employee():
        emp_id = emp_number_entry.get()
        if not emp_id:
            messagebox.showwarning("Warning", "Please enter employee number")
            return

        conn = connect('employee.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE emp_id=?", (emp_id,))
        employee = cursor.fetchone()
        conn.close()

        if employee:
            emp_name_entry.delete(0, END)
            emp_name_entry.insert(0, employee[1])
            status_var.set(employee[2])
            position_var.set(employee[3])
            # Salary will update automatically via position_var trace
            results_text.config(state=NORMAL)
            results_text.delete(1.0, END)
            results_text.insert(END, f"ID: {employee[0]}\nName: {employee[1]}\nStatus: {employee[2]}\nPosition: {employee[3]}\nSalary: {employee[4]:,.2f}\n\n")
            results_text.config(state=DISABLED)
        else:
            messagebox.showinfo("Not Found", "Employee not found")

    Button(root, text="Search", width=10, command=search_employee)\
        .grid(row=0, column=2, padx=5, pady=5, sticky="ew")

    Label(root, text="Employee Name:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    emp_name_entry = Entry(root)
    emp_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    # Employee Status Radio Buttons

    status_var = StringVar(value="Permanent")
    Label(root, text="Employee Status:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    Radiobutton(root, text="Permanent", variable=status_var, value="Permanent")\
        .grid(row=2, column=1, padx=5, pady=2, sticky="w")
    Radiobutton(root, text="Probationary", variable=status_var, value="Probationary")\
        .grid(row=3, column=1, padx=5, pady=2, sticky="w")
    Radiobutton(root, text="Casual", variable=status_var, value="Casual")\
        .grid(row=4, column=1, padx=5, pady=2, sticky="w")
    Radiobutton(root, text="Contractual", variable=status_var, value="Contractual")\
        .grid(row=5, column=1, padx=5, pady=2, sticky="w")

    # Position Dropdown
    position_var = StringVar(value="")
    position_var.trace("w", update_salary)  # Call update_salary when position changes
    Label(root, text="Position:").grid(row=6, column=0, padx=5, pady=5, sticky="w")
    OptionMenu(root, position_var, "Clerk", "Accountant", "Sales Manager", "Production Staff", "Project Manager")\
        .grid(row=6, column=1, padx=5, pady=5, sticky="ew")

    # Salary Display
    Label(root, text="Salary:").grid(row=7, column=0, padx=5, pady=5, sticky="w")
    salary_text = Text(root, height=1, width=9, state=DISABLED)
    salary_text.grid(row=7, column=1, columnspan=2, padx=5, pady=5, sticky="w")
    update_salary()  # Initialize salary display

    # Action Buttons
    def add_employee():
        try:
            emp_id = int(emp_number_entry.get())
            if emp_id <0:
                messagebox.showwarning("Warning", "Employee number must be a positive integer")
                return 
        except ValueError:
            messagebox.showwarning("Warning", "Employee number must be an integer")
            return
        name = emp_name_entry.get()
        status = status_var.get()
        position = position_var.get()

        if not all([emp_id, name, status, position]):
            messagebox.showwarning("Warning", "All fields are required")
            return

        try:
            conn = connect('employee.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO employees VALUES (?, ?, ?, ?, ?)",
                         (emp_id, name, status, position, salary_mapping[position]))
            conn.commit()
            messagebox.showinfo("Success", "Employee added successfully")
            clear_fields()
        except Error as e:
            messagebox.showerror("Error", f"Failed to add employee: {e}")
        finally:
            conn.close()

    def update_employee():
        emp_id = emp_number_entry.get()
        name = emp_name_entry.get()
        status = status_var.get()
        position = position_var.get()

        if not all([emp_id, name, status, position]):
            messagebox.showwarning("Warning", "All fields are required")
            return

        try:
            conn = connect('employee.db')
            cursor = conn.cursor()

            # First check if employee exists
            cursor.execute("SELECT emp_id FROM employees WHERE emp_id=?", (emp_id,))
            if not cursor.fetchone():
                messagebox.showinfo("Not Found", "Employee not found - cannot update")
                return

            cursor.execute("UPDATE employees SET name=?, status=?, position=?, salary=? WHERE emp_id=?",
                           (name, status, position, salary_mapping[position], emp_id))
            conn.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo("Success", "Employee updated successfully")
                clear_fields()
            else:
                messagebox.showinfo("No Changes", "No changes were made to the employee record")

        except Error as e:
            messagebox.showerror("Error", f"Failed to update employee: {e}")
        finally:
            conn.close()

    def delete_employee():
        emp_id = emp_number_entry.get()
        if not emp_id:
            messagebox.showwarning("Warning", "Please enter employee number")
            return

        try:
            conn = connect('employee.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM employees WHERE emp_id=?", (emp_id,))
            conn.commit()
            messagebox.showinfo("Success", "Employee deleted successfully")
            clear_fields()
        except Error as e:
            messagebox.showerror("Error", f"Failed to delete employee: {e}")
        finally:
            conn.close()

    def view_employees():
        try:
            conn = connect('employee.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM employees")
            employees = cursor.fetchall()

            results_text.config(state=NORMAL)
            results_text.delete(1.0, END)

            if employees:
                results_text.insert(END,"Employee ID\t\tName\t\tStatus\t\tPosition\t\tSalary\n")
                results_text.insert(END, "-" * 78 + "\n")
                for emp in employees:
                    results_text.insert(END, f"{emp[0]}\t\t{emp[1]}\t\t{emp[2]}\t\t{emp[3]}\t\t{emp[4]:,.2f}\n") # f"{emp[0]}\nName: {emp[1]}\nStatus: {emp[2]}\nPosition: {emp[3]}\nSalary: {emp[4]:,.2f}\n\n")
            else:
                results_text.insert(END, "No employees found")

            results_text.config(state=DISABLED)
        except Error as e:
            messagebox.showerror("Error", f"Failed to fetch employees: {e}")
        finally:
            conn.close()

    Button(root, text="Add", width=10, command=add_employee).grid(row=8, column=0, padx=5, pady=5)
    Button(root, text="Update", width=10, command=update_employee).grid(row=8, column=1, padx=5, pady=5)
    Button(root, text="Delete", width=10, command=delete_employee).grid(row=8, column=2, padx=5, pady=5)
    Button(root, text="View", width=10, command=view_employees).grid(row=9, column=0, padx=5, pady=5)
    Button(root, text="Exit", width=10, command=root.quit).grid(row=9, column=2, padx=5, pady=5)

    # Results Display
    root.grid_rowconfigure(11, weight=1)
    for col in range(4):
        root.grid_columnconfigure(col, weight=1)

    scroll_y = Scrollbar(root)
    scroll_x = Scrollbar(root, orient='horizontal')
    results_text = Text(root, height=30, width=30,
                      yscrollcommand=scroll_y.set,
                      xscrollcommand=scroll_x.set)
    scroll_y.config(command=results_text.yview)
    scroll_x.config(command=results_text.xview)

    results_text.grid(row=11, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
    scroll_y.grid(row=11, column=4, sticky="ns")
    scroll_x.grid(row=12, column=0, columnspan=4, sticky="ew")

    # Window Configuration
    root.update_idletasks()
    width = 660
    height = 500
    x = (root.winfo_screenwidth() - width) // 2
    y = (root.winfo_screenheight() - height) // 2
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.resizable(False, False)
    root.mainloop()