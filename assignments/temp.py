import tkinter as tk
from tkinter import messagebox, ttk, font
from tkinter.font import BOLD, NORMAL
import sqlite3


class MainPage:
    def __init__(self, root):
        self.root = root
        self.setup_window("Main Page", "600x400")
        self.precinct_num = [245, 367, 641, 179, "ALL"]
        self.precinct = [245, 367, 641, 179]
        self.setup_menu()
        self.setup_ui()

    def setup_window(self, title, size, resizable=(False, False)):
        self.root.title(title)
        self.root.geometry(size)
        self.root.resizable(*resizable)

    def setup_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        # File Menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new, accelerator="Crtl+N")
        file_menu.add_command(label="View", command=self.view, accelerator="Crtl+V")
        file_menu.add_separator()
        file_menu.add_command(label="Logout", command=self.logout, accelerator="Crtl+L")
        menu_bar.add_cascade(label="File", menu=file_menu, underline=0)

        # Edit Menu
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Search", command=self.search, accelerator="Crtl+S")
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        # Help Menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.about, accelerator="Crtl+Z")
        help_menu.add_command(label="Authors", command=self.authors, accelerator="Crtl+X")
        menu_bar.add_cascade(label="Help", menu=help_menu)

        # Keyboard shortcuts
        shortcuts = {
            "<Control-n>": self.new, "<Control-v>": self.view,
            "<Control-l>": self.logout, "<Control-s>": self.search,
            "<Control-z>": self.about, "<Control-x>": self.authors
        }
        for key, func in shortcuts.items():
            self.root.bind_all(key, lambda e, f=func: f())

    def setup_ui(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10)

        # Search Frame with Precinct Combobox
        search_frame = tk.Frame(self.main_frame)
        search_frame.pack(pady=5)
        tk.Label(search_frame, font=('Arial', 11, BOLD), text="Precinct: ").pack(side=tk.LEFT)

        self.search_combo = ttk.Combobox(
            search_frame,
            values=self.precinct_num,
            state="readonly",
            font=("Arial", 11, BOLD),
        )
        self.search_combo.pack(side=tk.LEFT, padx=5)
        self.search_combo.set("Select precinct")
        self.search_combo.bind("<<ComboboxSelected>>", lambda e: self.display())

        # Results Frame with Text Widget and Scrollbar
        results_frame = tk.Frame(self.main_frame)
        results_frame.pack(pady=10, padx=10)

        self.results_text = tk.Text(
            results_frame, wrap=tk.WORD, height=15, width=60, state="disabled"
        )
        self.results_text.pack(side=tk.LEFT)

        scrollbar = tk.Scrollbar(results_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.results_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.results_text.yview)

        # Close Button
        tk.Button(
            self.main_frame, text="Close", font=('Arial', 11), bg='DarkOrange',
            fg='Black', activebackground='orange', width=20, command=self.close
        ).pack(pady=5)

    def display(self):
        self.results_text.config(state="normal")
        self.results_text.delete(1.0, tk.END)

        selected = self.search_combo.get()
        if selected == "Select precinct":
            self.results_text.insert(tk.END, "Please select a precinct to display results.")
        else:
            try:
                conn = sqlite3.connect('votes.db')
                cursor = conn.cursor()

                if selected == "ALL":
                    cursor.execute("SELECT precinct, COUNT(*) FROM votes GROUP BY precinct")
                    precinct_counts = cursor.fetchall()
                    cursor.execute("SELECT COUNT(*) FROM votes")
                    overall_count = cursor.fetchone()[0]

                    self.results_text.insert(tk.END, "Votes per Precinct:\n")
                    for precinct, count in precinct_counts:
                        self.results_text.insert(tk.END, f"Precinct {precinct}: {count} votes\n")
                    self.results_text.insert(tk.END, f"\nTotal Votes: {overall_count}\n")
                else:
                    cursor.execute("SELECT * FROM votes WHERE precinct = ?", (selected,))
                    records = cursor.fetchall()

                    if records:
                        for record in records:
                            self.results_text.insert(
                                tk.END,
                                f"Voter ID: {record[0]} \nName: {record[1]} \nPrecinct: {record[2]} \nCandidates: {record[3]}\n"
                            )
                    else:
                        self.results_text.insert(tk.END, "No records found for the selected precinct.")

                conn.close()
            except sqlite3.Error as e:
                self.results_text.insert(tk.END, f"Database error: {e}")

        self.results_text.config(state="disabled")

    # Menu handlers
    def new(self):
        self.root.destroy()
        New(tk.Tk(), self.precinct).root.mainloop()

    def view(self):
        self.results_text.config(state="normal")
        self.results_text.delete(1.0, tk.END)
        self.search_combo.focus()
        self.results_text.config(state="disabled")

    def logout(self):
        if messagebox.askokcancel("Logout", "Are you sure you want to logout?"):
            self.root.destroy()
            LoginPage(tk.Tk()).root.mainloop()

    def close(self):
        self.results_text.config(state="normal")
        self.results_text.delete(1.0, tk.END)
        self.results_text.config(state="disabled")

    def search(self):
        self.root.destroy()
        Search(tk.Tk()).root.mainloop()

    def about(self):
        self.root.destroy()
        AboutPage(tk.Tk()).root.mainloop()

    def authors(self):
        self.root.destroy()
        AuthorsPage(tk.Tk()).root.mainloop()


class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        self.entry_counts = 0
        self.setup_ui()
        self.root.bind('<Return>', lambda e: self.login())

    def setup_ui(self):
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(pady=50)

        # Username and Password fields
        fields = [
            ("Username:", False),
            ("Password:", True)
        ]

        self.entries = {}
        for i, (label, is_password) in enumerate(fields):
            frame = tk.Frame(main_frame, bg='#f0f0f0')
            frame.grid(row=i * 2 + 1, column=0, padx=10)

            tk.Label(frame, text=label, bg='#f0f0f0', font=('Arial', 11)).pack(side=tk.LEFT, padx=5, pady=(0, 5))
            entry = tk.Entry(
                frame,
                show="*" if is_password else "",
                font=('Arial', 11),
                relief=tk.FLAT
            )
            entry.pack(side=tk.LEFT, padx=5, pady=(0, 10 if i == 0 else 20))
            self.entries[label.replace(":", "")] = entry

        # Buttons
        button_frame = tk.Frame(main_frame, bg='#f0f0f0')
        button_frame.grid(row=4, column=0)

        btn_props = {
            'bg': 'blue', 'fg': 'white', 'relief': tk.FLAT,
            'width': 10, 'font': ('Arial', 11)
        }

        tk.Button(
            button_frame, text="Login", command=self.login,
            activebackground='lightblue', **btn_props
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            button_frame, text="Cancel", command=self.cancel,
            activebackground='darkblue', **btn_props
        ).pack(side=tk.RIGHT, padx=5)

    def login(self):
        username = self.entries["Username"].get()
        password = self.entries["Password"].get()

        if username == "admin" and password == "admin":
            self.root.destroy()
            MainPage(tk.Tk()).root.mainloop()
        else:
            self.entry_counts += 1
            if self.entry_counts >= 3:
                messagebox.showerror("Login Failed", "Too many login attempts!")
                self.root.destroy()
            else:
                messagebox.showerror("Login Failed", f"Incorrect username or password! ({self.entry_counts}/3)")

    def cancel(self):
        self.root.destroy()


class New:
    def __init__(self, root, precinct_num):
        self.root = root
        self.root.title("New Record Form")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        self.counter = 0
        self.setup_ui(precinct_num)

    def setup_ui(self, precinct_num):
        main_frame = tk.Frame(self.root)
        main_frame.pack(pady=10)

        # Field setup
        fields = [
            ("Voter's ID Number:", "voter"),
            ("Voter's Name:", "name")
        ]

        self.entries = {}
        for i, (label, key) in enumerate(fields):
            frame = tk.Frame(main_frame)
            frame.pack(pady=5, anchor="w")

            tk.Label(
                frame, text=label, bg='#f0f0f0', font=('Arial', 11, BOLD)
            ).pack(side=tk.LEFT, padx=20, pady=(0, 5))

            entry = tk.Entry(
                frame, font=('Arial', 11), width=20 if i == 0 else None
            )
            entry.pack(side=tk.RIGHT if i == 0 else tk.LEFT, padx=(35 if i == 1 else 0, 0))
            self.entries[key] = entry

        # Precinct selection
        precinct_frame = tk.Frame(main_frame)
        precinct_frame.pack(pady=5, anchor="w")

        tk.Label(precinct_frame, font=('Arial', 11, BOLD), text="Precinct:").pack(side=tk.LEFT, padx=20, pady=(0, 5))

        self.search_combo = ttk.Combobox(
            precinct_frame, values=precinct_num, state="readonly", font=("Arial", 11, BOLD)
        )
        self.search_combo.pack(side=tk.LEFT, padx=(70, 0), pady=(0, 0))
        self.search_combo.set("Select precinct")

        # Candidate checkboxes
        checkbox_label = tk.Frame(main_frame)
        checkbox_label.pack(pady=10, anchor="w")
        tk.Label(checkbox_label, font=('Arial', 11, BOLD), text="Candidates:").pack(side=tk.LEFT, padx=20)

        checkbox_frame = tk.Frame(main_frame)
        checkbox_frame.pack(padx=120, pady=(0, 5))
        options = ["Superman", "Wolverine", "Iron man", "Batman", "Cyclops", "Spider man",
                   "Aquaman", "Phoenix", "Captain America", "Flash", "Iceman", "Scarlet Witch"]

        self.vars = {}
        for i, option in enumerate(options):
            var = tk.IntVar()
            self.vars[option] = var
            row, col = divmod(i, 3)
            tk.Checkbutton(
                checkbox_frame, text=option, variable=var, font=('Arial', 11, BOLD), fg='Blue'
            ).grid(row=row, column=col, sticky="w", padx=(20, 0), pady=2)

        # Button frames
        buttons = [
            {"frame": "first", "buttons": [
                {"text": "Review my Votes", "command": self.review},
                {"text": "Clear my Votes", "command": self.clear}
            ]},
            {"frame": "second", "buttons": [
                {"text": "Cancel Button", "command": self.cancel},
                {"text": "Close", "command": self.close}
            ]}
        ]

        for button_group in buttons:
            frame = tk.Frame(main_frame)
            frame.pack(pady=10 if button_group["frame"] == "second" else 0)

            for btn in button_group["buttons"]:
                tk.Button(
                    frame, text=btn["text"], command=btn["command"],
                    font=('Arial', 11), bg='Green', fg='White',
                    activebackground='DarkGreen', width=15
                ).pack(padx=5, side=tk.LEFT if btn is button_group["buttons"][0] else tk.RIGHT)

    def review(self):
        voter_id = self.entries["voter"].get()
        name = self.entries["name"].get()
        precinct = self.search_combo.get()

        # Validate inputs
        if not voter_id or not name or precinct == "Select precinct":
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Get selected candidates
        selected = [k for k, v in self.vars.items() if v.get() == 1]
        if not selected:
            messagebox.showerror("Error", "You must select at least one candidate.")
            return

        # Check if voter already exists
        if self.check_voter_exists(voter_id):
            if messagebox.askyesno("Voter Exists", "This voter has already voted. Do you want to update their record?"):
                self.update_record(voter_id, name, precinct, ", ".join(selected))
            return

        # Cast votes
        self.cast(voter_id, name, precinct, ", ".join(selected))

    def check_voter_exists(self):
        voter_id = self.entries["voter"].get()
        try:
            conn = sqlite3.connect('votes.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM votes WHERE voter_id = ?", (voter_id,))
            result = cursor.fetchone()
            conn.close()
            return result is not None
        except sqlite3.Error:
            # Create the table if it doesn't exist
            conn = sqlite3.connect('votes.db')
            cursor = conn.cursor()
            cursor.execute('''
                           CREATE TABLE IF NOT EXISTS votes
                           (
                               voter_id
                               TEXT
                               PRIMARY
                               KEY,
                               name
                               TEXT,
                               precinct
                               TEXT,
                               candidates
                               TEXT
                           )
                           ''')
            conn.commit()
            conn.close()
            return False

    def cast(self, voter_id, name, precinct, candidates):
        try:
            conn = sqlite3.connect('votes.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO votes VALUES (?, ?, ?, ?)",
                           (voter_id, name, precinct, candidates))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Votes cast successfully!")
            self.clear()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))

    def update_record(self, voter_id, name, precinct, candidates):
        try:
            conn = sqlite3.connect('votes.db')
            cursor = conn.cursor()
            cursor.execute("UPDATE votes SET name = ?, precinct = ?, candidates = ? WHERE voter_id = ?",
                           (name, precinct, candidates, voter_id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Record updated successfully!")
            self.clear()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))

    def clear(self):
        self.entries["voter"].delete(0, tk.END)
        self.entries["name"].delete(0, tk.END)
        self.search_combo.set("Select precinct")
        for var in self.vars.values():
            var.set(0)

    def cancel(self):
        self.root.destroy()
        MainPage(tk.Tk()).root.mainloop()

    def close(self):
        self.root.destroy()


class Search:
    def __init__(self, root):
        self.root = root
        self.root.title("My search")
        self.root.geometry("600x200")
        self.root.resizable(False, False)
        self.setup_ui()

    def setup_ui(self):
        main_frame = tk.Frame(self.root)
        main_frame.pack(pady=20, anchor="w")

        voter_frame = tk.Frame(main_frame)
        voter_frame.pack(pady=5)

        tk.Label(
            voter_frame, text="Voter's ID Number:", bg='#f0f0f0', font=('Arial', 11, BOLD)
        ).pack(side=tk.LEFT, padx=20, pady=(0, 5))

        self.entry_voter = tk.Entry(voter_frame, font=('Arial', 11), width=30)
        self.entry_voter.pack(side=tk.LEFT, pady=(0, 0))

        tk.Button(
            voter_frame, text="Search", command=self.search_voter,
            font=('Arial', 11), bg='Violet', fg='Black',
            activebackground='purple', width=10, border=5
        ).pack(side=tk.RIGHT, padx=20)

        tk.Button(
            self.root, text="Close", command=self.close,
            bg='red', fg='white', activebackground='DarkRed',
            width=10, border=5, font=('Arial', 11)
        ).pack(pady=10)

    def search_voter(self):
        voter_id = self.entry_voter.get()
        if not voter_id:
            messagebox.showerror("Error", "Please enter a voter ID")
            return

        try:
            conn = sqlite3.connect('votes.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM votes WHERE voter_id = ?", (voter_id,))
            record = cursor.fetchone()
            conn.close()

            if record:
                result = f"Voter ID: {record[0]}\nName: {record[1]}\nPrecinct: {record[2]}\nCandidates: {record[3]}"
                messagebox.showinfo("Voter Found", result)

                if messagebox.askyesno("Edit/Delete", "Do you want to edit this record?"):
                    self.edit_voter(record)
                elif messagebox.askyesno("Edit/Delete", "Do you want to delete this record?"):
                    self.delete_voter(voter_id)
            else:
                messagebox.showinfo("Not Found", "No voter found with that ID")
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))

    def edit_voter(self, record):
        self.root.destroy()
        edit_root = tk.Tk()
        new_form = New(edit_root, [245, 367, 641, 179])

        new_form.entries["voter"].insert(0, record[0])
        new_form.entries["voter"].config(state="disabled")
        new_form.entries["name"].insert(0, record[1])
        new_form.search_combo.set(record[2])

        candidates = record[3].split(", ")
        for candidate in candidates:
            if candidate in new_form.vars:
                new_form.vars[candidate].set(1)

        edit_root.mainloop()

    def delete_voter(self, voter_id):
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this record?"):
            try:
                conn = sqlite3.connect('votes.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM votes WHERE voter_id = ?", (voter_id,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Record deleted successfully!")
                self.entry_voter.delete(0, tk.END)
            except sqlite3.Error as e:
                messagebox.showerror("Database Error", str(e))

    def close(self):
        self.root.destroy()
        MainPage(tk.Tk()).root.mainloop()


class BasePage:
    def __init__(self, root, title, size="300x200", text=""):
        self.root = root
        self.root.title(title)
        self.root.geometry(size)
        self.root.resizable(False, False)

        tk.Label(
            root, text=text, font=('Arial', 11 if title == "About" else 12, BOLD if title != "About" else NORMAL),
            justify=tk.CENTER, padx=10, pady=10
        ).pack(pady=20)

        tk.Button(
            root, text="Close", command=self.close,
            bg='blue', fg='white', activebackground='lightblue',
            relief=tk.FLAT, width=10, font=('Arial', 11)
        ).pack(pady=10)

    def close(self):
        self.root.destroy()
        MainPage(tk.Tk()).root.mainloop()


class AboutPage(BasePage):
    def __init__(self, root):
        super().__init__(root, "About", text="This is the About Page.\n\nExplains the program.")


class AuthorsPage(BasePage):
    def __init__(self, root):
        super().__init__(root, "Authors",
                         text="\nDevelopers:\n Harold Dela Pena \n Cedrick Joseph Mariano \n Rj Jack Florida")


if __name__ == "__main__":
    root = tk.Tk()
    login = LoginPage(root)
    root.mainloop()
