from idlelib.debugger_r import wrap_info

import customtkinter as windows
from CTkMessagebox import CTkMessagebox
from PIL import Image
from fontTools.cffLib import TopDict
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def navigationBar(root, text, x, y, command):

    button = windows.CTkButton(
        master=root,
        text=text,
        text_color="white",
        font=("Roboto", 15, "bold"),
        fg_color="black",
        bg_color="black",
        hover_color="black",
        command=command
    )
    button.place(x=x, y=y)

    # Bind hover effects
    button.bind("<Enter>", lambda event: button.configure(text_color="#FF520E"))
    button.bind("<Leave>", lambda event: button.configure(text_color="white"))
    return button

def mainWindows(root):
    for widget in root.winfo_children():
        widget.destroy()

    background = windows.CTkImage(
        dark_image=Image.open("../Image/background.png"),
        size=(1536, 864)
    )
    showBackground = windows.CTkLabel(
        master=root, text="",
        image=background
    )
    showBackground.place(x=0, y=0, relwidth=1, relheight=1)

    labelOne = windows.CTkLabel(
        master=root,
        text="Schedule with Precision,\nNavigate with C-LOOK.",
        text_color="white",
        anchor="center",
        font=("Broadway", 48 , "bold"),
        fg_color="black"
    )
    labelOne.place(x=430, y=200)
    labelTwo = windows.CTkLabel(
        master=root,
        text="Streamline disk access with C-LOOK, the efficient\n"
             "algorithm for optimized scheduling.",
        text_color="lightgray",
        font=("Roboto", 24),
        fg_color="black"
    )
    labelTwo.place(x=490, y=325)

    logo = windows.CTkImage(
        dark_image=Image.open("../Image/logo.png"),
        size=(75, 65)
    )
    showLogo = windows.CTkButton(
        master=root,
        text="",
        image=logo,
        fg_color="black",
        bg_color="black",
        hover_color="black",
        command=lambda : mainWindows(root)
    )
    showLogo.place(x=100, y=45)

    processNavigation = navigationBar(root, "Process", 575, 75, lambda: learnMore(root))
    aboutNavigation = navigationBar(root, "About", 675, 75, lambda: aboutUs(root))
    faqsNavigation = navigationBar(root, "FAQs", 775, 75, lambda: learnMore(root))

    startButton = windows.CTkButton(
        master=root,
        text="Get Started",
        text_color="white",
        width=80,
        height=50,
        font=("Roboto", 15, "bold"),
        corner_radius=12,
        fg_color="#FF520E",
        bg_color="black",
        hover_color="#D9430C",
        command=lambda : secondWindows(root)
    )
    startButton.place(x=630, y=425)

    learnButton = windows.CTkButton(
        master=root,
        text="Learn More",
        text_color="white",
        width=80,
        height=50,
        font=("Roboto", 15, "bold"),
        corner_radius=12,
        fg_color="black",
        bg_color="black",
        border_color="#FF520E",
        border_width=1,
        hover_color="#D9430C",
        command=lambda : learnMore(root)
    )
    learnButton.place(x=760, y=425)

def secondWindows(root):
    for widget in root.winfo_children():
        widget.destroy()

    background = windows.CTkImage(
        dark_image=Image.open("../Image/background.png"),
        size=(1536, 864)
    )
    showBackground = windows.CTkLabel(
        master=root,
        text="",
        image=background
    )
    showBackground.place(x=0, y=0, relwidth=1, relheight=1)

    logo = windows.CTkImage(
        dark_image=Image.open("../Image/logo.png"),
        size=(75, 65)
    )
    showLogo = windows.CTkButton(
        master=root,
        text="",
        image=logo,
        fg_color="black",
        bg_color="black",
        hover_color="black",
        command=lambda : mainWindows(root)
    )
    showLogo.place(x=100, y=45)

    processNavigation = navigationBar(root, "Process", 575, 75, lambda: learnMore(root))
    aboutNavigation = navigationBar(root, "About", 675, 75, lambda: aboutUs(root))
    faqsNavigation = navigationBar(root, "FAQs", 775, 75, lambda: learnMore(root))

    mainFrame = windows.CTkFrame(
        master=root,
        width=800,
        height=600,
        fg_color="#1E1E1E",
        bg_color="black",
        corner_radius=12,
        border_color="#3A3A3A",
        border_width=1
    )
    mainFrame.place(relx=0.5, rely=0.5, anchor="center")

    info = windows.CTkLabel(
        master=mainFrame,
        text="Input Details for Disk\nScheduling Process",
        text_color="white",
        anchor="center",
        font=("Broadway", 32, "bold"),
    )
    info.place(x=200, y=40)

    windows.CTkLabel(
        master=mainFrame,
        text="Number of Tracks",
        font=("Roboto", 15),
        text_color="white").place(x=110, y=180, anchor="w"
    )
    noOfTracksEntry = windows.CTkEntry(
        master=mainFrame,
        width=250,
        height=30,
        text_color="black",
        placeholder_text="e.g., within the range 100-350",
        fg_color="white"
    )
    noOfTracksEntry.place(x=110, y=210, anchor="w")

    windows.CTkLabel(
        master=mainFrame,
        text="Previous Track",
        font=("Roboto", 15),
        text_color="white").place(x=110, y=250, anchor="w"
    )
    pastTrackEntry = windows.CTkEntry(
        master=mainFrame,
        width=250,
        height=30,
        text_color="black",
        placeholder_text="e.g., 250",
        fg_color="white"
    )
    pastTrackEntry.place(x=110, y=280, anchor="w")

    windows.CTkLabel(
        master=mainFrame,
        text="Current Track",
        font=("Roboto", 15),
        text_color="white").place(x=110, y=320, anchor="w"
    )
    presentTrackEntry = windows.CTkEntry(
        master=mainFrame,
        width=250,
        height=30,
        text_color="black",
        placeholder_text="e.g., 230",
        fg_color="white"
    )
    presentTrackEntry.place(x=110, y=350, anchor="w")

    windows.CTkLabel(
        master=mainFrame,
        text="Seek Rate",
        font=("Roboto", 15),
        text_color="white").place(x=110, y=390, anchor="w"
    )
    seekTimeEntry = windows.CTkEntry(
        master= mainFrame,
        width=250,
        height=30,
        text_color="black",
        placeholder_text="e.g. 15",
        fg_color="white"
    )
    seekTimeEntry.place(x=110, y=420, anchor="w")

    windows.CTkLabel(
        master=mainFrame,
        text="Alpha",
        font=("Roboto", 15),
        text_color="white").place(x=425, y=180, anchor="w"
    )
    alphaTimeEntry = windows.CTkEntry(
        master= mainFrame,
        width=250,
        height=30,
        text_color="black",
        placeholder_text="e.g. 25",
        fg_color="white"
    )
    alphaTimeEntry.place(x=425, y=210, anchor="w")

    windows.CTkLabel(
        master=mainFrame,
        text="Number of Requested Tracks",
        font=("Roboto", 15),
        text_color="white").place(x=425, y=250, anchor="w"
    )
    noOfReqTracksEntry = windows.CTkEntry(
        master=mainFrame,
        width=250,
        height=30,
        text_color="black",
        placeholder_text="e.g., within the range 10-25",
        fg_color="white"
    )
    noOfReqTracksEntry.place(x=425, y=280, anchor="w")

    windows.CTkLabel(
        master=mainFrame,
        text="Requested Tracks",
        font=("Roboto", 15),
        text_color="white").place(x=425, y=320, anchor="w"
    )
    trackRouteEntry = windows.CTkEntry(
        master=mainFrame,
        width=250,
        height=30,
        text_color="black",
        placeholder_text="must be separated by commas",
        fg_color="white"
    )
    trackRouteEntry.place(x=425, y=350, anchor="w")

    submitButton = windows.CTkButton(
        master=mainFrame,
        text="Submit",
        text_color="white",
        width=80,
        height=40,
        font=("Roboto", 15, "bold"),
        corner_radius=12,
        fg_color="#FF520E",
        hover_color="#D9430C",
        command=lambda : processCLook(root, noOfTracksEntry, pastTrackEntry,
                                       presentTrackEntry, seekTimeEntry, alphaTimeEntry,
                                       noOfReqTracksEntry, trackRouteEntry)
    )
    submitButton.place(x=300, y=450)

    cancelButton = windows.CTkButton(
        master=mainFrame,
        text="Cancel",
        text_color="white",
        width=80,
        height=40,
        font=("Roboto", 15, "bold"),
        corner_radius=12,
        fg_color="black",
        border_color="#FF520E",
        border_width=1,
        hover_color="#D9430C",
        command=lambda :mainWindows(root)
    )
    cancelButton.place(x=400, y=450)

def processCLook(root, noOfTracksEntry, presentTrackEntry, pastTrackEntry,
                 seekTimeEntry, alphaTimeEntry, noOfReqTracksEntry, trackRouteEntry):

    errors = []

    try:
        noOfTracks = int(noOfTracksEntry.get().strip())
    except ValueError:
        errors.append("Number of Tracks")
    
    try:
        presentTrack = int(presentTrackEntry.get().strip())
    except ValueError:
        errors.append("Current Track")
    
    try:
        pastTrack = int(pastTrackEntry.get().strip())
    except ValueError:
        errors.append("Previous Track")
    
    try:
        seekTime = int(seekTimeEntry.get().strip())
    except ValueError:
        errors.append("Seek Rate")
    
    try:
        alphaTime = int(alphaTimeEntry.get().strip())
    except ValueError:
        errors.append("Alpha")
    
    try:
        noOfReqTracks = int(noOfReqTracksEntry.get().strip())
    except ValueError:
        errors.append("Number of Requested Tracks")
    
    try:
        trackRoute = [int(entry) for entry in trackRouteEntry.get().split(",")]
    except ValueError:
        errors.append("Requested Tracks")

    if errors:
        error_message = "Please Fill Up Required Fields: " + ",\n".join(errors)
        CTkMessagebox(
            master=root,
            title="Warning!",
            message=error_message,
            icon="warning",
            option_1="Close",
            font=("Roboto", 15),
            button_width=50,
          cancel_button="circle"
        )
        return

    #function call for determineDirection returns the direction and other info
    leftRoute, rightRoute, chosenDirection = determineDirection(trackRoute, presentTrack, pastTrack)

    # function call for executeCLook and does not return any value
    plotCLookResults, noOfTracks, alphaX, sentence = executeCLook(noOfTracks, presentTrack, seekTime,
                                                                  leftRoute, rightRoute, chosenDirection, alphaTime)

    #function call for showPlot
    showPlot(root, plotCLookResults, noOfTracks, alphaX, sentence)

def determineDirection(trackRoute, presentTrack, pastTrack):
    """this function determines the direction of the graph"""

    #checks if the present and past track is in the list of trackRoute
    excludeTrack = [presentTrack, pastTrack]
    for track in excludeTrack:
        while track in trackRoute:
            trackRoute.remove(track)

    #splits the requested trackRoute depending on the present track
    leftRoute, rightRoute = [], []
    for perTrack in trackRoute:
        if perTrack < presentTrack:
           leftRoute.append(perTrack)
        else:
           rightRoute.append(perTrack)

    #checks the direction of the graph whether from leftRoute to rightRoute or vice versa
    chosenDirection = ""
    if presentTrack < pastTrack:
        chosenDirection = "leftRoute"
    elif presentTrack > pastTrack:
        chosenDirection = "rightRoute"

    leftRoute.sort(reverse=True) #reverse sort the left list
    rightRoute.sort()

    return leftRoute, rightRoute, chosenDirection

def executeCLook(noOfTracks, presentTrack, seekTime, leftRoute, rightRoute, chosenDirection, alphaTime):
    cLookTotalHeadMovement = 0
    cLookTotalSeekTime = 0
    sortedThmOrder = []
    plotCLookResults = []
    alphaX = []
    showThm = ""

    if chosenDirection == "leftRoute":
        # move from the present track to the lowest track in the left array,
        # then go to the highest track in the right array
        if leftRoute:
            perMovement = abs(presentTrack - leftRoute[-1])
            cLookTotalHeadMovement += perMovement
            sortedThmOrder.append(f"({presentTrack} - {leftRoute[-1]})")
            plotCLookResults.append(presentTrack)
            plotCLookResults.append(leftRoute[-1])
            plotCLookResults.append(rightRoute[-1])
            alphaX.append(leftRoute[-1])
            alphaX.append(rightRoute[-1])

        if rightRoute:
            perMovement = abs(rightRoute[-1] - rightRoute[0])
            cLookTotalHeadMovement += perMovement
            sortedThmOrder.append(alphaTime)
            sortedThmOrder.append(f"({rightRoute[-1]} - {rightRoute[0]})")
            plotCLookResults.append(rightRoute[0])

    elif chosenDirection == "rightRoute":
        # move from the present track to the highest track in the right list,
        # then go to the lowest track in the left list
        if rightRoute:
            perMovement = abs(rightRoute[-1] - presentTrack)
            cLookTotalHeadMovement += perMovement
            sortedThmOrder.append(f"({rightRoute[-1]} - {presentTrack})")
            plotCLookResults.append(presentTrack)
            plotCLookResults.append(rightRoute[-1])
            plotCLookResults.append(leftRoute[-1])
            alphaX.append(rightRoute[-1])
            alphaX.append(leftRoute[-1])

        if leftRoute:
            perMovement = abs(leftRoute[0] - leftRoute[-1])
            cLookTotalHeadMovement += perMovement
            sortedThmOrder.append(alphaTime)
            sortedThmOrder.append(f"({leftRoute[0]} - {leftRoute[-1]})")
            plotCLookResults.append(leftRoute[0])

    cLookTotalHeadMovement = cLookTotalHeadMovement + alphaTime
    cLookTotalSeekTime = float(cLookTotalHeadMovement * seekTime)
    totalSeekInSeconds = float(cLookTotalSeekTime / 1000)

    for i, track in enumerate(sortedThmOrder):  # each element in sortedThmOrder will be joined with a '+'
        if i > 0:
            showThm += " + "
        showThm += str(track)
    sentence = f"""
    Total Head Movement: {showThm} = {cLookTotalHeadMovement}
    Seek Time: {cLookTotalSeekTime}ms or {totalSeekInSeconds}secs"""

    return plotCLookResults, noOfTracks, alphaX, sentence

def showPlot(root, plotCLookResults, noOfTracks, alphaX, sentence):

    for widget in root.winfo_children():
        widget.destroy()

    background = windows.CTkImage(
        dark_image=Image.open("../Image/background.png"),
        size=(1536, 864)
    )
    showBackground = windows.CTkLabel(
        master=root, text="",
        image=background
    )
    showBackground.place(x=0, y=0, relwidth=1, relheight=1)

    logo = windows.CTkImage(
        dark_image=Image.open("../Image/logo.png"),
        size=(75, 65)
    )
    showLogo = windows.CTkButton(
        master=root,
        text="",
        image=logo,
        fg_color="black",
        bg_color="black",
        hover_color="black",
        command=lambda : mainWindows(root)
    )
    showLogo.place(x=100, y=45)

    processNavigation = navigationBar(root, "Process", 575, 75, lambda: learnMore(root))
    aboutNavigation = navigationBar(root, "About", 675, 75, lambda: aboutUs(root))
    faqsNavigation = navigationBar(root, "FAQs", 775, 75, lambda: learnMore(root))

    mainFrame = windows.CTkFrame(
        master=root,
        width=800,
        height=600,
        fg_color="#1E1E1E",
        bg_color="black",
        corner_radius=12,
        border_color="#3A3A3A",
         border_width=1
    )
    mainFrame.place(relx=0.5, rely=0.5, anchor="center")

    # graph of the scan algorithm
    # the subplot() function you can draw multiple plots in one figure
    # fig: the figure object, which represents the entire figure or canvas
    # pt: to configure the plot, such as adding data, titles, labels, grids, or customizing ticks

    fig, pt = plt.subplots()

    canvas = FigureCanvasTkAgg(fig, master=mainFrame)
    canvas.get_tk_widget().place(
        relx=0.5,
        rely=0.5,
        anchor='center',
        width=800,
        height=600
    )

    # x and y data for plotting
    coordX = plotCLookResults
    coordY = list(range(len(coordX)))
    alphaY = list(range(len(alphaX)))
    alphaY = [i + 0.9 for i in alphaY]
    plotX = round(noOfTracks / 2)

    # header for the clook
    title = "CLOOK Disk Scheduling Algorithms"
    pt.set_title(
        title.upper(),
        weight="bold",
        font="Broadway",
        color="darkviolet",
        size="18"
    )
    pt.plot(
        coordX,
        coordY,
        color="#00008B",
        markerfacecolor="#FFA500",
        marker="o",
        markersize=4,
        linewidth=2
    )
    pt.plot(
        alphaX,
        alphaY,
        dashes=[4, 1.5],
        color="darkgreen",
        marker='D',
        markersize=3,
        linewidth=1
    )
    for i, (x, y) in enumerate(zip(coordX, coordY)):  # shows the number of each dot
        pt.text(
            x, y,
            str(x),
            fontsize=8,
            ha='left',
            va='bottom',
            color='red'
        )
    pt.set_yticklabels([])
    if noOfTracks <= 150:
        spacing = 15
    elif noOfTracks <= 250:
        spacing = 25
    else:
        spacing = 35
        pt.set_xticks(range(0, noOfTracks + 1, spacing))
    pt.invert_yaxis()
    pt.xaxis.tick_top()
    pt.xaxis.set_label_position('top')
    pt.text(
        plotX, 1.3, "α",
        fontsize=15,
        color="darkgreen",
        ha="center",
        va="center"
    )
    pt.spines['bottom'].set_visible(False)  # bottom line of the table
    pt.spines['right'].set_visible(False)  # right line of the table
    pt.spines['left'].set_visible(False)  # left line of the table
    pt.grid(
        True,
        which='both',
        axis='both',
        color='gray',
        linestyle='--',
        linewidth=0.5
    )
    pt.set_facecolor("lightgrey")  # bg color
    fig.text(
        0.10, 0.03,
        sentence,
        ha="left",
        fontsize=11,
        fontfamily="Arial",
        color="darkviolet"
    )
    canvas.draw()

    backButton = windows.CTkButton(
        master=mainFrame,
        text="Back",
        text_color="white",
        width=80,
        height=40,
        font=("Roboto", 15, "bold"),
        corner_radius=12,
        fg_color="#FF520E",
        hover_color="#D9430C",
        command=lambda :secondWindows(root)
    )
    backButton.place(x=640, y=550)

def aboutUs(root):
    for widget in root.winfo_children():
        widget.destroy()

    processNavigation = navigationBar(root, "Process", 575, 75, lambda: learnMore(root))
    aboutNavigation = navigationBar(root, "About", 675, 75, lambda: aboutUs(root))
    faqsNavigation = navigationBar(root, "FAQs", 775, 75, lambda: learnMore(root))

    main_frame = windows.CTkFrame(
        master=root,
        width=650,
        height=370,
        fg_color="#3f2182",
        corner_radius=15
    )

def learnMore(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(fg_color="black")

    logo = windows.CTkImage(
        dark_image=Image.open("../Image/logo.png"),
        size=(75, 65)
    )
    showLogo = windows.CTkButton(
        master=root,
        text="",
        image=logo,
        fg_color="black",
        bg_color="black",
        hover_color="black",
        command=lambda :mainWindows(root)
    )
    showLogo.place(x=100, y=45)

    processNavigation = navigationBar(root, "Process", 575, 75, lambda: learnMore(root))
    aboutNavigation = navigationBar(root, "About", 675, 75, lambda: aboutUs(root))
    faqsNavigation = navigationBar(root, "FAQs", 775, 75, lambda: learnMore(root))

    info = windows.CTkLabel(
        master=root,
        text="Learn More About C-LOOK",
        text_color="white",
        anchor="center",
        font=("Broadway", 32, "bold"),
    )
    info.place(x=520, y=125)

    firstFrame = windows.CTkFrame(
        master=root,
        width=500,
        height=300,
        fg_color="#1E1E1E",
        bg_color="black",
        corner_radius=12,
        border_color="#3A3A3A",
        border_width=1
    )
    firstFrame.place(x=235,y=185)

    secondFrame = windows.CTkFrame(
        master=root,
        width=500,
        height=300,
        fg_color="#1E1E1E",
        bg_color="black",
        corner_radius=12,
        border_color="#3A3A3A",
        border_width=1
    )
    secondFrame.place(x=750,y=185)

    thirdFrame = windows.CTkFrame(
        master=root,
        width=500,
        height=300,
        fg_color="#1E1E1E",
        bg_color="black",
        corner_radius=12,
        border_color="#3A3A3A",
        border_width=1
    )
    thirdFrame.place(x=235,y=500)

    fourthFrame = windows.CTkFrame(
        master=root,
        width=500,
        height=300,
        fg_color="#1E1E1E",
        bg_color="black",
        corner_radius=12,
        border_color="#3A3A3A",
        border_width=1
    )
    fourthFrame.place(x=750,y=500)

    firstTitle = windows.CTkLabel(
        master=firstFrame,
        text="What is C-LOOK Disk Scheduling?",
        text_color="white",
        font=("Broadway", 24)
    )
    firstTitle.place(x=25, y=40)

    firstParagraph = windows.CTkLabel(
        master=firstFrame,
        text="The C-LOOK (Circular LOOK) disk scheduling\n"
             "algorithm optimizes seek time by scanning in\n"
             "one direction until it reaches the last request,\n"
             "then jumping back to the first request on the\n"
             "opposite end. Unlike LOOK, it skips intermediate\n"
             "cylinders when resetting, forming a circular\npattern.",
        text_color="white",
        justify="left",
        font=("Roboto", 19)
    )
    firstParagraph.place(x=35, y=90)

    secondTitle = windows.CTkLabel(
        master=secondFrame,
        text="Key Features of C-LOOK",
        text_color="white",
        font=("Broadway", 24)
    )
    secondTitle.place(x=25, y=40)

    secondParagraph = windows.CTkLabel(
        master=secondFrame,
        text="1. Efficient Seek Time: Reduces unnecessary\n    head movements.\n"
             "2. Directional Scanning: Services requests in\n"
             "    one direction before reversing.\n"
             "3. Circular Approach: \"Jumps\" back to the closest\n"
             "    starting point after reaching the furthest request.\n"
             "4. Fairness: Ensures all requests are serviced\n"
             "    efficiently.",
        text_color="white",
        justify="left",
        font=("Roboto", 19)
    )
    secondParagraph.place(x=35, y=90)

    thirdTitle = windows.CTkLabel(
        master=thirdFrame,
        text="Why Choose C-LOOK?",
        text_color="white",
        font=("Broadway", 24)
    )
    thirdTitle.place(x=25, y=40)

    thirdParagraph = windows.CTkLabel(
        master=thirdFrame,
        text="• Minimized Latency: Ensures faster request\n   handling.\n"
               "• Reduced Wear: Limits disk head movement,\n"
               "   increasing hardware longevity.\n"
               "• Optimized for Heavy Loads: Suitable for\n"
               "   systems with high I/O operations.\n"
               "• Predictability: Maintains a clear service order.",
        text_color="white",
        justify="left",
        font=("Roboto", 19)
    )
    thirdParagraph.place(x=35, y=90)

    thirdTitle = windows.CTkLabel(
        master=fourthFrame,
        text="When to Use C-LOOK?",
        text_color="white",
        font=("Broadway", 24)
    )
    thirdTitle.place(x=25, y=40)

    fourthParagraph = windows.CTkLabel(
        master=fourthFrame,
        text="C-LOOK is ideal for:\n"
             "  • Data Servers: High-demand environments\n"
             "     with frequent disk access.\n"
             "  • Real-Time Systems: Where predictable\n"
             "     performance is crucial.\n"
             "  • Optimizing Efficiency: When minimizing seek\n"
             "     time is a priority.",
        text_color="white",
        justify="left",
        font=("Roboto", 19)
    )
    fourthParagraph.place(x=35, y=90)

if __name__ == "__main__":

    root = windows.CTk() # create a customtkinter root window
    root.title("Dashboard Disk Information")
    root.iconbitmap("Image/OS.ico")

    scr_width = root.winfo_screenwidth()
    scr_height = root.winfo_screenheight()

    root.geometry(f"{scr_width}x{scr_height}+0+0")
    windows.set_appearance_mode("system")
    windows.set_default_color_theme("dark-blue")
    root.resizable(False, False)
    mainWindows(root)  # call the function to create the half-colored window
    root.mainloop()