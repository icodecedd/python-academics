import customtkinter as windows
from CTkMessagebox import CTkMessagebox
from PIL import Image
from matplotlib import pyplot as plt

# Function to process user input
def submit_values(no_tracks_entry, prev_track_entry, curr_track_entry, seek_rate_entry, no_req_tracks_entry, req_tracks_entry):

    try:
    # Get values from windows.CTkEntry widgets
        no_of_tracks = int(no_tracks_entry.get().strip())
        prev_track = int(prev_track_entry.get().strip())
        curr_track = int(curr_track_entry.get().strip())
        seek_rate = int(seek_rate_entry.get().strip())
        req_tracks_limit = int(no_req_tracks_entry.get().strip())
        req_tracks = [int(x) for x in req_tracks_entry.get().split(",")]

    except ValueError:
            CTkMessagebox(master=root, title="Warning!!!", message="Please Fill Up Required Information", icon="warning",
                      option_1="Close", font=("consolas", 11),
                      button_width=50, cancel_button="circle")

    # CTkMessagebox(master=root,title="Disk Info", message=f"Tracks: {no_of_tracks}\n\n"
    #                                        f"Previous Track: {prev_track}\n\n"
    #                                        f"Current Track: {curr_track}\n\n"
    #                                        f"Seek Rate: {seek_rate}\n\n"
    #                                        f"No. of Req Track: {req_tracks_limit}\n\n"
    #                                        f"Tracks: {req_tracks}",
    #                                        option_1="Close", font=("consolas", 11),
    #                                        button_width=50, cancel_button="circle")

    x = req_tracks
    y = list(range(len(x)))
    plt.plot(x, y, color="#000080", markerfacecolor="orange", marker="o", markersize=3, linewidth=2.7)
    plt.show()

def next_page(root):
    for widget in root.winfo_children():
        widget.destroy()

    image2 = windows.CTkImage(light_image=Image.open('../Image/inverted.png'), size=(50, 50))
    imagetwo = windows.CTkLabel(master=root, text="", image=image2)
    imagetwo.place(x=10, y=0)

    info = windows.CTkLabel(master=root, text=">> Enter Information for Disk Processing <<", font=("consolas", 18, "bold"))
    info.place(x=115, y=70)

    windows.CTkLabel(root, text="No. of Tracks:", font=("consolas", 14)).place(x=25, y=150, anchor="w")
    no_tracks_entry = windows.CTkEntry(root, placeholder_text="Enter No. of Tracks")
    no_tracks_entry.place(x=150, y=150, anchor="w")

    windows.CTkLabel(root, text="Previous Track:", font=("consolas", 14)).place(x=25, y=190, anchor="w")
    prev_track_entry = windows.CTkEntry(root, placeholder_text="Enter Previous Track")
    prev_track_entry.place(x=150, y=190, anchor="w")

    windows.CTkLabel(root, text="Current Track:", font=("consolas", 14)).place(x=25, y=230, anchor="w")
    curr_track_entry = windows.CTkEntry(root, placeholder_text="Enter Current Track")
    curr_track_entry.place(x=150, y=230, anchor="w")

    windows.CTkLabel(root, text="Seek Rate:", font=("consolas", 14)).place(x=310, y=150, anchor="w")
    seek_rate_entry = windows.CTkEntry(root, placeholder_text="Enter Seek Rate")
    seek_rate_entry.place(x=460, y=150, anchor="w")

    windows.CTkLabel(root, text="No. of Req Tracks:", font=("consolas", 14)).place(x=310, y=190, anchor="w")
    no_req_tracks_entry = windows.CTkEntry(root, placeholder_text="Enter No. of Req Tracks")
    no_req_tracks_entry.place(x=460, y=190, anchor="w")

    windows.CTkLabel(root, text="Requested Tracks:", font=("consolas", 14,)).place(x=310, y=230, anchor="w")
    req_tracks_entry = windows.CTkEntry(root, placeholder_text="Separated By Commas")
    req_tracks_entry.place(x=460, y=230, anchor="w")

    image3 = windows.CTkImage(light_image=Image.open("../Image/submit.png"))
    submit_button = windows.CTkButton(root, text="SUBMIT", font=("consolas", 12), corner_radius=50,
    command= lambda: submit_values(no_tracks_entry, prev_track_entry, curr_track_entry,
                                   seek_rate_entry, no_req_tracks_entry, req_tracks_entry),
                                   image=image3, compound="right")
    submit_button.place(x=240, y=270)

    image4 = windows.CTkImage(light_image=Image.open("../Image/go back.png"))
    go_back = windows.CTkButton(root, text="GO BACK", font=("consolas", 12), corner_radius=50,command=lambda: main_window(root),
                                image=image4, compound="right")
    go_back.place(x=240, y=320)

def main_window(root):
    for widget in root.winfo_children():
        widget.destroy()

    left_frame = windows.CTkFrame(root, width=260, height=300, corner_radius=0, fg_color="#f9ebff")
    left_frame.pack(side="left", fill="both", expand=True)

    right_frame = windows.CTkFrame(root, width=250, height=300, corner_radius=0, fg_color="#293aab")
    right_frame.pack(side="right", fill="both", expand=True)

    image1 = windows.CTkImage(light_image=Image.open('../Image/CLOOK.png'), size=(390, 390))
    image = windows.CTkLabel(master=left_frame, text="", image=image1)
    image.pack(anchor="center")

    image2 = windows.CTkImage(light_image=Image.open('../Image/inverted.png'), size=(50, 50))
    imagetwo = windows.CTkLabel(master=left_frame, text="", image=image2)
    imagetwo.place(x=10, y=0)

    image3 = windows.CTkImage(light_image=Image.open('../Image/[BSIT] Logo C.png'), size=(150, 150))
    imagethree = windows.CTkLabel(master=right_frame, text="", image=image3)
    imagethree.place(x=45, y=40)

    image4 = windows.CTkImage(light_image=Image.open('../Image/open.png'), size=(20, 20))
    open_button = windows.CTkButton(master=right_frame, text="OPEN ", font=("consolas", 12), corner_radius=50,
                                    image=image4, compound="right", command=lambda: next_page(root))
    open_button.place(x=50, y=210)

    image5 = windows.CTkImage(light_image=Image.open('../Image/close.png'))
    close_button = windows.CTkButton(master=right_frame, text="CLOSE", font=("consolas", 12), corner_radius=50,
                                     image=image5, compound="right", command=lambda: root.destroy())
    close_button.place(x=50, y=260)

# Run the application
if __name__ == "__main__":

    root = windows.CTk() # create a customtkinter root window
    root.title("Fill in Disk Information")
    root.iconbitmap("Image/OS.ico")
    root_width = 750
    root_height = 470
    scr_width = root.winfo_screenwidth()
    scr_height = root.winfo_screenheight()

    x = (scr_width / 1.7) - (root_width / 1.7)
    y = (scr_height / 1.7) - (root_height / 1.7)
    root.resizable(False, False)
    root.geometry(f"{root_width}x{root_height}+{int(x)}+{int(y)}")
    root.configure(fg_color="#f9ebff")
    windows.set_appearance_mode("light")
    windows.set_default_color_theme("blue")
    main_window(root)  # call the function to create the half-colored window
    root.mainloop()
