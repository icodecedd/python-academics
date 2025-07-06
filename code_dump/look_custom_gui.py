import customtkinter as windows
from CTkMessagebox import CTkMessagebox
from PIL import Image
from matplotlib import pyplot as plt

def main_windows(root):
    for widget in root.winfo_children():
        widget.destroy()

    main_frame = windows.CTkFrame(master=root,
                                  width=650,
                                  height=370,
                                  fg_color="#3f2182",
                                  corner_radius=15)
    main_frame.place(relx=0.5, rely=0.55, anchor="center")

    image1 = windows.CTkImage(light_image=Image.open("../Image/photo1.png"), size=(350, 290))
    show_image1 = windows.CTkLabel(master=main_frame,
                                   text="", image=image1)
    show_image1.place(x=280, y=40)

    main_text = windows.CTkLabel(master=main_frame,
                                 text="KARINA Scheduling\nAlgorithm",
                                 font=("Impact", 25, "bold"),
                                 text_color="white",
                                 justify="left")
    main_text.place(x=25, y=90)

    body_text = windows.CTkLabel(master=main_frame,
                                 text="Circular look is like C-Scan which\n"
                                      "uses a return sweep before\n"
                                      "processing a set of disk requests. Like\n"
                                      "the Look Algorithm, C-Look does not\n"
                                      "reach the end of the tracks unless\n"
                                      "there is a request, either a read or a\n"
                                      "write, on such disk location.",
                                 font=("Hp Simplified", 15),
                                 text_color="white",
                                 justify="left")
    body_text.place(x=25, y=160)

    hashtag = windows.CTkButton(master=main_frame,
                                text="#operatingsystems",
                                text_color="black",
                                width=80,
                                font=("Hp Simplified", 12),
                                corner_radius=50,
                                state="disable",
                                fg_color="#b3aaff")
    hashtag.place(x=25, y=55)

    image2 = windows.CTkImage(light_image=Image.open("../Image/arrow-right (2).png"))
    button1 = windows.CTkButton(master=main_frame,
                                width=150,
                                height=30,
                                text="Start Now!    ",
                                text_color="black",
                                hover_color="lightgray",
                                font=("Hp Simplified", 15),
                                fg_color="white",
                                corner_radius=100,
                                image=image2,
                                compound="right", command=lambda :submit_disk(root))
    button1.place(x=25, y=300)

    logo = windows.CTkImage(light_image=Image.open("../Image/[BSIT] Icon Logo.png"), size=(20, 20))
    show_logo = (windows.CTkLabel(master=root, text="", image=logo))
    show_logo.place(x=50, y=20)

    show_logo_name = windows.CTkLabel(master=root,
                                      text="Abyss of Perception",
                                      text_color="white",
                                      font=("Impact", 16)
                                      )
    show_logo_name.place(x=75, y=20)

    image3 = windows.CTkImage(Image.open("../Image/info.png"))
    button2 = windows.CTkButton(master=root,
                                width=15,
                                text="About Us",
                                text_color="black",
                                hover_color="lightgray",
                                font=("Hp Simplified", 12),
                                fg_color="white",
                                corner_radius=100,
                                image=image3,
                                compound="right",
                                command=lambda : about_us(root))
    button2.place(x=595, y=20)

def about_us(root):
    for widget in root.winfo_children():
        widget.destroy()

    main_frame = windows.CTkFrame(master=root,
                                  width=650,
                                  height=370,
                                  fg_color="#3f2182",
                                  corner_radius=15)
    main_frame.place(relx=0.5, rely=0.55, anchor="center")

    image1 = windows.CTkImage(light_image=Image.open("../Image/who are we.png"), size=(590, 350))
    show_image1 = windows.CTkLabel(master=main_frame,
                                   text="", image=image1)
    show_image1.place(relx=0.5, rely=0.5, anchor="center")

    header = windows.CTkLabel(master=main_frame,
                              text="°❀⋆.ೃ࿔*:･WHO ARE WE?°❀⋆.ೃ࿔*:･",
                              text_color="white",
                              font=("Impact", 30))
    header.place(x=110, y=45)

    lore = windows.CTkLabel(master=main_frame,
                            text="Karina, born Yoo Ji-min, is a captivating member of the K-pop girl group aespa, formed by\n"
                                 "SM Entertainment. Known for her stunning visuals, powerful stage presence, and versatile\n"
                                 "talent, Karina has quickly become a standout figure in the K-pop industry.",
                            text_color="white",
                            font=("Hp Simplified", 15),
                            )
    lore.place(x=45, y=290)

    logo = windows.CTkImage(light_image=Image.open("../Image/[BSIT] Icon Logo.png"), size=(20, 20))
    show_logo = (windows.CTkLabel(master=root, text="", image=logo))
    show_logo.place(x=50, y=20)

    show_logo_name = windows.CTkLabel(master=root,
                                      text="Abyss of Perception",
                                      text_color="white",
                                      font=("Impact", 16)
                                      )
    show_logo_name.place(x=75, y=20)

    image3 = windows.CTkImage(Image.open("../Image/back-button.png"))
    button2 = windows.CTkButton(master=root,
                                width=25,
                                text="  Go Back ",
                                text_color="black",
                                hover_color="lightgray",
                                font=("Hp Simplified", 12),
                                fg_color="white",
                                corner_radius=100,
                                image=image3,
                                compound="right",
                                command=lambda : main_windows(root))
    button2.place(x=595, y=20)

def submit_disk(root):
    for widget in root.winfo_children():
        widget.destroy()

    main_frame = windows.CTkFrame(master=root,
                                  width=650,
                                  height=370,
                                  fg_color="#3f2182",
                                  corner_radius=15)
    main_frame.place(relx=0.5, rely=0.55, anchor="center")

    logo = windows.CTkImage(light_image=Image.open("../Image/[BSIT] Icon Logo.png"), size=(20, 20))
    show_logo = (windows.CTkLabel(master=root, text="", image=logo))
    show_logo.place(x=50, y=20)

    show_logo_name = windows.CTkLabel(master=root,
                                      text="Abyss of Perception",
                                      text_color="white",
                                      font=("Impact", 16)
                                      )
    show_logo_name.place(x=75, y=20)

    info = windows.CTkLabel(master=main_frame, text=">> Enter Information for Disk Processing <<", font=("Impact", 20, "bold"))
    info.place(x=125, y=40)

    windows.CTkLabel(master=main_frame, text="No. of Tracks", font=("Hp Simplified", 13), text_color="white").place(x=100, y=100, anchor="w")
    no_tracks_entry = windows.CTkEntry(master=main_frame, width=200, text_color="black", placeholder_text="e.g. 150", fg_color="white")
    no_tracks_entry.place(x=100, y=130, anchor="w")

    windows.CTkLabel(master=main_frame, text="Previous Track", font=("Hp Simplified", 13)).place(x=100, y=170, anchor="w")
    prev_track_entry = windows.CTkEntry(master=main_frame, width=200, text_color="black", placeholder_text="e.g. 100", fg_color="white")
    prev_track_entry.place(x=100, y=200, anchor="w")

    windows.CTkLabel(master=main_frame, text="Current Track", font=("Hp Simplified", 13)).place(x=100, y=240, anchor="w")
    curr_track_entry = windows.CTkEntry(master=main_frame, width=200, text_color="black", placeholder_text="e.g. 110", fg_color="white")
    curr_track_entry.place(x=100, y=270, anchor="w")

    windows.CTkLabel(master=main_frame, text="Seek Rate", font=("Hp Simplified", 13)).place(x=350, y=100, anchor="w")
    seek_rate_entry = windows.CTkEntry(master=main_frame, width=200, text_color="black", placeholder_text="e.g. 10", fg_color="white")
    seek_rate_entry.place(x=350, y=130, anchor="w")

    windows.CTkLabel(master=main_frame, text="No. of Requested Tracks", font=("Hp Simplified", 13)).place(x=350, y=170, anchor="w")
    no_of_req_entry = windows.CTkEntry(master=main_frame, width=200, text_color="black", placeholder_text="e.g. 25", fg_color="white")
    no_of_req_entry.place(x=350, y=200, anchor="w")

    windows.CTkLabel(master=main_frame, text="Requested Tracks", font=("Hp Simplified", 13)).place(x=350, y=240, anchor="w")
    req_entry = windows.CTkEntry(master=main_frame, width=200, text_color="black", placeholder_text="e.g. 25", fg_color="white")
    req_entry.place(x=350, y=270, anchor="w")

    image1 = windows.CTkImage(Image.open("../Image/sign-in (1).png"))
    submit = windows.CTkButton(master=main_frame,
                               width=100,
                               text="Submit  ",
                               text_color="black",
                               hover_color="#7165d5",
                               font=("Hp Simplified", 12),
                               fg_color="#b3aaff",
                               corner_radius=100,
                               image=image1,
                               compound="right",
                               command=lambda: calculate_disk(root, no_tracks_entry, prev_track_entry, curr_track_entry,
                                                            seek_rate_entry, no_of_req_entry, req_entry)
                               )
    submit.place(x=450, y=300)
    image3 = windows.CTkImage(Image.open("../Image/back-button.png"))
    back = windows.CTkButton(master=root,
                                width=25,
                                text="  Go Back ",
                                text_color="black",
                                hover_color="lightgray",
                                font=("Hp Simplified", 12),
                                fg_color="white",
                                corner_radius=100,
                                image=image3,
                                compound="right",
                                command=lambda : main_windows(root))
    back.place(x=595, y=20)

def calculate_disk(root, no_tracks_entry, prev_track_entry, curr_track_entry, seek_rate_entry, no_of_req_entry, req_entry):

    try:
    # Get values from windows.CTkEntry widgets
        no_of_tracks = int(no_tracks_entry.get().strip())
        prev_track = int(prev_track_entry.get().strip())
        curr_track = int(curr_track_entry.get().strip())
        seek_rate = int(seek_rate_entry.get().strip())
        req_tracks_limit = int(no_of_req_entry.get().strip())
        req_tracks = [int(entry) for entry in req_entry.get().split(",")]

    except ValueError:
            CTkMessagebox(master=root, title="Warning!!!", message="Please Fill Up Required Information", icon="warning",
                      option_1="Close", font=("Hp Simplified", 14),
                      button_width=50, cancel_button="circle")

    # checks if the current and prev track is in the list, if these are in the list
    # it will be removed since the current and previous tracks cannot be repeated
    while curr_track in req_tracks:
        req_tracks.remove(curr_track)
    while prev_track in req_tracks:
        req_tracks.remove(prev_track)

    # initializing two lists named left_wing and right_wing
    left_wing = []
    right_wing = []
    # this will iterate in the disk_tracks index by index to identify which track
    # is less than the current track and which are greater than the current track
    for track in req_tracks:
        if track < curr_track:
            left_wing.append(track)
        else:
            right_wing.append(track)
    # to make sure that both lists are sorted from lowest to highest, we use a sort() function
    left_wing.sort()
    right_wing.sort()

    # these line of codes are used to identify if the movement will be from right to left or vice versa
    movement = None
    if curr_track < prev_track:
        movement = "left movement"
    elif curr_track > prev_track:
        movement = "right movement"
    # returns the left and right, as well as the movement/direction of the graph

    look_computation(root, no_of_tracks, curr_track, seek_rate, left_wing, right_wing, movement)

def look_computation(root, no_of_tracks, curr_track, seek_rate, left_wing, right_wing, movement):
    # initialization of local variables
    overhead_order = []
    push_graph = [curr_track]
    sum_of_overhead_movement = float(0)
    sum_of_seek: float = float(0)

    # an if else statement for appending and calculating the sum of the overhead movement
    if movement == "right movement":
        # from max track to the current track
        if right_wing:
            overhead_order.append(f"({right_wing[-1]}-{curr_track})")
            push_graph.append(right_wing[-1])
            overhead = abs(right_wing[-1] - curr_track)
            sum_of_overhead_movement = sum_of_overhead_movement + overhead
        # from max track to leftmost track in the list
        if left_wing:
            overhead_order.append(f"({right_wing[-1]}-{left_wing[0]})")
            push_graph.append(left_wing[0])
            overhead = abs(right_wing[-1] - left_wing[0])
            sum_of_overhead_movement = sum_of_overhead_movement + overhead

    else:
        # move from the current track to the lowest track in the left list
        if left_wing:
            overhead_order.append(f"({curr_track}-{left_wing[0]})")
            push_graph.append(left_wing[0])
            overhead = abs(curr_track - left_wing[0])
            sum_of_overhead_movement = sum_of_overhead_movement + overhead
        # from rightmost value in right list to 0
        if right_wing:
            overhead_order.append(f"({right_wing[-1]}-{left_wing[0]})")
            push_graph.append(right_wing[-1])
            overhead = abs(right_wing[-1] - left_wing[0])
            sum_of_overhead_movement = sum_of_overhead_movement + overhead

    # this is the formula for computing the sum of seek rate and seek rate in seconds
    sum_of_seek = float(seek_rate * sum_of_overhead_movement)
    sum_of_seek_secs = float(sum_of_seek / 1000)
    overhead_movement = " + ".join(map(str, overhead_order))

    if no_of_tracks <= 175:
        interval = 25
    else:
        interval = 50

    plot_look_algo(push_graph, no_of_tracks, interval)

    show_result(root, overhead_movement, sum_of_overhead_movement, seek_rate, sum_of_seek, sum_of_seek_secs)

def plot_look_algo(push_graph, track_limit, interval):
    # separating the figure and axes for better organization
    fig, ax = plt.subplots()
    i = push_graph  # passing the values of push_graph list
    j = list(range(len(i)))  # getting the length of i and then making it as a value of a list

    # shows the title of the algorithm
    plt.title("'LOOK' DISK SCHEDULING ALGORITHM", color="gold", weight="semibold", size="15", fontstyle="italic",
              family="DejaVu Sans Mono")
    # shows the actual line
    plt.plot(i, j, color="#000080", markerfacecolor="orange", marker="D", markersize=5, linewidth=2.7)
    # xticks means showing the x-axes' label with the right interval
    plt.xticks(range(0, track_limit + 1, interval))
    # this means that the y-axes' label will be hidden
    plt.gca().set_yticklabels([])
    plt.gca().invert_yaxis()  # invert the value of y from highest to lowest
    plt.gca().xaxis.set_label_position('top')  # move the x-axis label to the top
    plt.gca().xaxis.tick_top()
    plt.gca().set_facecolor("lightyellow")  # setting the color of the box as light yellow
    plt.grid(axis="y", linestyle="dotted", color="brown")  # adding a grid lines for y-axis
    sentence = "-----> Please Close the Window to See Results <-----"
    fig.text(0.5, 0.03, sentence, weight="bold", color="orange", fontsize=10.5, ha="center",
             font="DejaVu Sans Mono")

    manager = plt.get_current_fig_manager()
    plot_width = 750
    plot_height = 470
    scrn_width = root.winfo_screenwidth()
    scrn_height = root.winfo_screenheight()

    xcoord = (scrn_width / 1.5) - (plot_width / 1.5)
    ycoord = (scrn_height / 1.5) - (plot_height / 1.5)

    manager.window.geometry(f"{plot_width}x{plot_height}+{int(xcoord)}+{int(ycoord)}")

    plt.show()  # showing the final illustration of the graph

def show_result(root, overhead_movement, sum_of_overhead_movement, seek, sum_of_seek, sum_of_seek_secs):
    """this function basically shows the result of the look scheduling algorithm"""
    final_result = (f"Total Head Movement: {overhead_movement} = {sum_of_overhead_movement}\n"
                        f"\nSeek Rate: {sum_of_overhead_movement} * {seek}\n\n"
                        f"Seek Rate: {sum_of_seek}ms or {sum_of_seek_secs}secs")

    # this is a messagebox that shows the result, imported from tkinter
    CTkMessagebox(master=root, title="Disk Scheduling Calculation Result",  message=final_result, icon="info",
                      option_1="Close", font=("Hp Simplified", 14),
                      button_width=50, cancel_button="circle")

if __name__ == "__main__":

    root = windows.CTk() # create a customtkinter root window
    root.title("Dashboard Disk Information")
    root.iconbitmap("Image/OS.ico")
    # setting the main window pops in the middle screen
    root_width = 750
    root_height = 470
    scr_width = root.winfo_screenwidth()
    scr_height = root.winfo_screenheight()

    x = (scr_width / 1.7) - (root_width / 1.7)
    y = (scr_height / 1.7) - (root_height / 1.7)

    root.geometry(f"{root_width}x{root_height}+{int(x)}+{int(y)}")
    root.configure(fg_color="#13072e")
    windows.set_appearance_mode("system")
    windows.set_default_color_theme("blue")
    root.resizable(False, False)
    main_windows(root)  # call the function to create the half-colored window
    root.mainloop()