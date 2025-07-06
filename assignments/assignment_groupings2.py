from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from sqlite3 import connect

attempts = 0
checkBoxes = []
conn = connect('Votes.db')


def initDb():
    global conn
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Voters (voteID TEXT PRIMARY KEY, voteName TEXT, precNo INT, selCandid TEXT, totVotesPrec INT, grandTotVotes INT)")
    conn.commit()


def clearFields(votersId, votersName, precinctNo, checkBox, isClear=False):
    votersId.delete(0, END)
    votersName.delete(0, END)
    precinctNo.set("245" if isClear else "Select Precinct")
    for var in checkBox:
        var.set(0)


def deleteData(votersId, voter):
    global conn
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Voters WHERE voteID = ?", (votersId,))
    conn.commit()
    mainWindow(voter)


def getVoterData(voterId, window):
    global conn
    cursor = conn.cursor()
    cursor.execute("SELECT voteID, voteName, precNo, selCandid FROM Voters WHERE voteID = ?", (voterId,))
    result = cursor.fetchone()
    if result:
        newWindow(window, isEdit=True, voterData=result, isUpdate=True)
    else:
        messagebox.showwarning("Warning", "Voter does not exist!")


def updateVoterData(new, candidatesWin, voterId, votersName, precinctNo, selectedCandidates):
    global conn
    votersID = voterId.get()
    votersNameVal = votersName.get()
    precinctNoVal = precinctNo.get()
    selCandid = ", ".join(selectedCandidates)

    totVotesPrec, grandTotVotes = countVotes(precinctNo, selectedCandidates)

    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Voters SET voteName=?, precNo=?, selCandid=?, totVotesPrec=?, grandTotVotes=? WHERE voteID = ?",
        (votersNameVal, precinctNoVal, selCandid, votersID, totVotesPrec, grandTotVotes))
    conn.commit()
    messagebox.showinfo("Success", "Voter updated successfully")
    candidatesWin.destroy()
    mainWindow(new)


def countVotes(precinctNoVal, selectedCandidates):
    global conn
    cursor = conn.cursor()
    cursor.execute(
        "SELECT SUM(LENGTH(selCandid) - LENGTH(REPLACE(selCandid, ',', '')) + 1) FROM Voters WHERE precNo = ?",
        (precinctNoVal,))
    result = cursor.fetchone()
    existingPrecVotes = result[0] if result[0] else 0

    cursor.execute("SELECT SUM(LENGTH(selCandid) - LENGTH(REPLACE(selCandid, ',', '')) + 1) FROM Voters")
    result = cursor.fetchone()
    existingTotalVotes = result[0] if result[0] else 0

    totVotesPrec = existingPrecVotes + len(selectedCandidates)
    grandTotVotes = existingTotalVotes + len(selectedCandidates)

    return totVotesPrec, grandTotVotes


def aboutWindow(main):
    main.destroy()
    about = Tk()
    configureWindow(about, "About the System", 500, 300)

    aboutMessage = """
    Voting System GUI

    This system is designed to facilitate secure and user-friendly voting for a set 
    of predefined candidates. Voters can enter their credentials, select up to 8 
    candidates, and submit their choices with ease. All votes are recorded and stored 
    in a database, and the system ensures that each voter can only cast one vote.

    Features:
    - Graphical User Interface for ease of use
    - Candidate selection using check buttons
    - Real-time input validation
    - Vote review before submission
    - Vote recording with precinct tracking and vote totals
    """

    Label(about, text=aboutMessage, justify="left").place(x=25, y=10)
    Button(about, text="Close", command=lambda: mainWindow(about), width=10, background="lightgreen").place(x=190,
                                                                                                            y=250)


def programmersWindow(main):
    main.destroy()
    programmers = Tk()
    configureWindow(programmers, "About the System", 500, 300)

    programmersMessage = """
    Programmers:

    - Cedrick Joseph H. Mariano | Frontend Developer

    - Harold Prince E. dela Pena | Backend Developer

    - Rj Jack A. Florida | Quality Assurance
    """

    Label(programmers, text=programmersMessage, justify="left", font=("Roboto", 11)).place(x=30, y=15)
    Button(programmers, text="Close", command=lambda: mainWindow(programmers), width=10, background="lightgreen").place(
        x=190, y=250)


def votersDataWindow(votersId, name, precinct, search):
    global conn
    search.destroy()
    voter = Tk()
    configureWindow(voter, "Voter's Data", 500, 200)

    Label(voter, text=f"Welcome {name}", font=("Roboto", 11)).place(x=180, y=20)
    Label(voter, text=f"Your voting precinct is at {precinct}", font=("Roboto", 11)).place(x=150, y=50)

    Button(voter, text="Edit", command=lambda: getVoterData(votersId, voter), width=10, background="lightblue",
           padx=10).place(x=130, y=120)
    Button(voter, text="Delete", command=lambda: deleteData(votersId, voter), width=10, background="lightblue",
           padx=10).place(x=280, y=120)


def searchWindow(main):
    global conn
    main.destroy()
    search = Tk()
    configureWindow(search, "My Search", 500, 200)

    Label(search, text="Voter's ID Number:").place(x=30, y=40)
    votersId = Entry(search, width=35)
    votersId.place(x=160, y=40)

    def doSearch():
        cursor = conn.cursor()
        cursor.execute("SELECT voteName, precNo FROM Voters WHERE voteID = ?", (votersId.get(),))
        result = cursor.fetchone()
        if result:
            votersDataWindow(votersId.get(), result[0], result[1], search)
        else:
            messagebox.showwarning("Warning", "Voter does not exist!")

    searchPrecinct = Button(search, text="Search", width=10, background="violet", command=doSearch)
    searchPrecinct.place(x=390, y=40)
    Button(search, text="Cancel", command=lambda: mainWindow(search), width=10, background="orange").place(x=200, y=100)


def viewWindow(selectPrecinct, textField):
    global conn

    selectPrecinct.configure(state="readonly")
    selected = selectPrecinct.get()

    cursor = conn.cursor()
    textField.config(state="normal")
    textField.delete(1.0, END)
    if selected == "All":
        cursor.execute("SELECT SUM(totVotesPrec) FROM Voters")
        result = cursor.fetchone()
        textField.insert(END, f"Grand Total votes: {result[0] if result[0] else 0}\n")
    else:
        cursor.execute(
            "SELECT voteID, voteName, precNo, selCandid FROM Voters WHERE precNo = ?",
            (selected,))
        results = cursor.fetchall()
        for result in results:
            textField.insert(END, f"Voter ID: {result[0]}\n")
            textField.insert(END, f"Voter Name: {result[1]}\n")
            textField.insert(END, f"Precinct Number: {result[2]}\n")
            textField.insert(END, f"Selected Candidates: {result[3]}\n\n")
        cursor.execute("SELECT SUM(totVotesPrec) FROM Voters WHERE precNo = ?", (str(selected),))
        totalVotes = cursor.fetchone()[0]
        if selected == "Select Precinct":
            textField.insert(END, "")
        else:
            textField.insert(END, f"Total votes for Precinct {selected}: {totalVotes if totalVotes else 0}\n")


def castVotes(candidatesWin, votersId, votersName, precinctNo, selectedCandidates):
    global conn
    candidatesWin.destroy()
    votersID = votersId.get()
    votersNameVal = votersName.get()
    precinctNoVal = precinctNo.get()
    selCandidates = ", ".join(selectedCandidates)

    try:
        totVotesPrec, grandTotVotes = countVotes(precinctNoVal, selectedCandidates)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Voters VALUES (?, ?, ?, ?, ?, ?)",
                       (votersID, votersNameVal, precinctNoVal, selCandidates, totVotesPrec, grandTotVotes))
        conn.commit()
        messagebox.showinfo("Success", "Voter added successfully")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add Voter: {e}")


def getSelected(new, votersId, votersName, precinctNo, checkBox, candidatesList, isEdit=False, isUpdate=False):
    selectedCandidates = []

    for i, var in enumerate(checkBox):
        if var.get():
            selectedCandidates.append(candidatesList[i])

    if not (votersId.get() and votersName.get() and precinctNo.get() and selectedCandidates):
        messagebox.showwarning("Warning", "All fields are required")
        return

    if len(selectedCandidates) > 8:
        messagebox.showerror("Error", "You can only select a maximum of 8 candidates.")
        return
    else:
        candidatesStr = "\n".join(map(str, selectedCandidates))

        candidatesWin = Tk()
        configureWindow(candidatesWin, "My Candidates", 300, 200)

        if isEdit and isUpdate:
            command = lambda: updateVoterData(new, candidatesWin, votersId, votersName, precinctNo, selectedCandidates)
        else:
            command = lambda: castVotes(candidatesWin, votersId, votersName, precinctNo, selectedCandidates)

        Label(candidatesWin, text=candidatesStr, padx=10, pady=10, justify="left").grid(row=1, column=0, pady=(5, 0))
        Button(candidatesWin, text="Cast My Votes", command=command, width=10, background="red").place(x=50, y=150)
        Button(candidatesWin, text="Cancel", command=candidatesWin.destroy, width=10, background="red").place(x=170,
                                                                                                              y=150)
        configureWindow(candidatesWin, "My Candidates", 300, 200)


def newWindow(main, isEdit=False, voterData=None, isUpdate=False):
    main.destroy()
    new = Tk()
    configureWindow(new, "New Record Form", 500, 500)
    Label(new, text="Voter's ID Number:", padx=10, pady=10).grid(row=0, column=0, pady=(5, 0))
    Label(new, text="Voter's Name:", padx=10).grid(row=1, column=0, sticky="w", pady=(0, 10))
    Label(new, text="Precinct Number:", padx=10).grid(row=2, column=0, sticky="w", pady=(0, 10))
    Label(new, text="Candidates:", padx=10).grid(row=3, column=0, sticky="w")

    votersId = Entry(new, width=30)
    votersId.grid(row=0, column=1, pady=(5, 0), sticky="w")
    votersName = Entry(new, width=30)
    votersName.grid(row=1, column=1, sticky="w", pady=(0, 5))
    precinctNo = Combobox(new, values=["245", "367", "641", "179"], width=20, state="readonly")
    precinctNo.grid(row=2, column=1, sticky="w", pady=(0, 5))

    candidates = ["Superman", "Batman", "Aquaman", "Flash", "Wolverine", "Cyclops", "Phoenix",
                  "Iceman", "Iron Man", "Spiderman", "Capt. America", "Scarlet Witch"]
    checkBoxesLocal = []

    col = 1
    row = 3
    for i, candidate in enumerate(candidates):
        var = IntVar()
        checkBoxesLocal.append(var)
        Checkbutton(new, text=candidate, variable=var).place(x=col * 120, y=row * 35)

        row += 1
        if (i + 1) % 4 == 0:
            col += 1
            row = 3

    if isEdit and voterData:
        votersId.insert(0, voterData[0])
        votersId.config(state="disabled")
        votersName.insert(0, voterData[1])
        precinct = voterData[2]
        precinctNo.set(precinct)
        selectedCandidates = voterData[3].split(", ")
        for i, cand in enumerate(candidates):
            checkBoxesLocal[i].set(1 if cand in selectedCandidates else 0)

    # TODO: fix the logic in checkboxes for update

    Button(new, text="Review My Votes", width=15, wraplength=60, justify="center", background="lightgreen",
           command=lambda: getSelected(new, votersId, votersName, precinctNo, checkBoxesLocal, candidates, isEdit,
                                       isUpdate)).place(x=120, y=260)
    Button(new, text="Clear My Choices", command=lambda: [variable.set(0) for variable in checkBoxesLocal], width=15,
           wraplength=50, justify="center", background="lightgreen").place(x=270, y=260)
    Button(new, text="Cancel",
           command=lambda: clearFields(votersId, votersName, precinctNo, checkBoxesLocal, isClear=True), height=2,
           width=15, background="lightgreen").place(x=120, y=330)
    Button(new, text="Close", command=lambda: mainWindow(new), height=2, width=15, background="lightgreen").place(x=270,
                                                                                                                  y=330)

    new.mainloop()


def mainWindow(login):
    login.destroy()
    main = Tk()
    configureWindow(main, "Main Form", 460, 310)

    precinct = ["245", "367", "641", "179", "All"]
    selectPrecinct = Combobox(main, values=precinct, width=20, state="disabled")
    selectPrecinct.set("Select Precinct")
    selectPrecinct.bind("<<ComboboxSelected>>", lambda _: viewWindow(selectPrecinct, textField))
    selectPrecinct.place(x=20, y=20)

    yScroll = Scrollbar(main)
    xScroll = Scrollbar(main, orient='horizontal')
    textField = Text(main, height=12, width=50, yscrollcommand=yScroll.set, xscrollcommand=xScroll.set,
                     state="disabled")
    yScroll.config(command=textField.yview)
    xScroll.config(command=textField.xview)

    textField.place(x=20, y=50)
    yScroll.place(x=430, y=50, height=200)
    xScroll.place(x=20, y=250, width=430)

    Button(main, text="Close", command=lambda: [textField.delete("1.0", "end"), selectPrecinct.set("Select Precinct")],
           width=10, background="orange", padx=5, pady=5).place(x=180, y=260)

    menu = Menu(main)
    file = Menu(menu, tearoff=0)
    file.add_command(label="New", command=lambda: newWindow(main))
    file.add_separator()
    file.add_command(label="View", command=lambda: viewWindow(selectPrecinct, textField))
    file.add_separator()
    file.add_command(label="Logout", command=main.destroy)
    menu.add_cascade(label="File", underline=0, menu=file)

    edit = Menu(menu, tearoff=0)
    edit.add_command(label="Search", command=lambda: searchWindow(main))
    menu.add_cascade(label="Edit", underline=0, menu=edit)

    helpMenu = Menu(menu, tearoff=0)
    helpMenu.add_command(label="About", command=lambda: aboutWindow(main))
    helpMenu.add_separator()
    helpMenu.add_command(label="Authors", command=lambda: programmersWindow(main))
    menu.add_cascade(label="Help", underline=0, menu=helpMenu)
    main.configure(menu=menu)

    main.mainloop()


def checkCredentials(login, username, password):
    global attempts

    if username == "admin" and password == "1234":
        mainWindow(login)
    else:
        attempts += 1
        if attempts < 3:
            messagebox.showerror("Login", f"Incorrect username or password. You have {3 - attempts} attempts left.")
        else:
            messagebox.showerror("Login", "Maximum login attempts reached. Please try again later.")
            exit()


def loginWindow():
    login = Tk()
    configureWindow(login, "Login", 300, 200)
    Label(login, text="Username:", padx=10, pady=10).grid(row=0, column=0, pady=(10, 0))
    Label(login, text="Password:", padx=10).grid(row=1, column=0)
    username = Entry(login, width=30)
    username.grid(row=0, column=1, pady=(10, 0))
    password = Entry(login, show="*", width=30)
    password.grid(row=1, column=1)

    Button(login, text="Login", command=lambda: checkCredentials(login, username.get(), password.get()), width=10,
           background="lightblue").place(x=50, y=100)
    Button(login, text="Cancel", command=login.quit, width=10, background="lightblue").place(x=170, y=100)
    login.mainloop()


def configureWindow(window, title, width, height):
    window.title(title)
    x = (window.winfo_screenwidth() - width) // 2
    y = (window.winfo_screenheight() - height) // 2
    window.geometry(f"{width}x{height}+{int(x)}+{int(y) - 100}")
    window.resizable(False, False)


if __name__ == "__main__":
    # loginWindow(login)
    root = Tk()
    initDb()
    mainWindow(root)