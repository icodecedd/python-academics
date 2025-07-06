# modules and libraries used in this program
from matplotlib import pyplot as plt # used to show the graph/plot of the LOOK algorithm
from tkinter import messagebox # used to show a messagebox containing the result
from colorama import Fore
import time
import os
import pyfiglet
import tkinter

def group_credits():
    os.system("cls")
    print(Fore.MAGENTA + """
          \t\t\t\t\t\t\t    ────────────୨ৎ─────────── 
          \t\t\t\t\t\t\t     𝐆𝐑𝐎𝐔𝐏 𝐂𝐑𝐄𝐃𝐈𝐓𝐒     
          \t\t\t\t\t\t\t    ────────────୨ৎ───────────  
          """ + Fore.RESET)
          
    names = [
        {"name": "Developer", "description": """
         Ysabella Nicole
         Rizza Mae
         Alaiza Claine"""},
        {"name": "Designer", "description": """
         Ysabella Nicole
         Rizza Mae
         Alaiza Claine"""},
        {"name": "Libraries", "description": """
         matplotlib: Library for creating graphs and visualizations.
         colorama: Adds colors to console text.
         tkinter: Toolkit for building desktop GUI apps.
         os: Handles operating system tasks like files and paths.
         time: Manages time-related functions like delays and timestamps."""}, 
        ]
    
    for name in names:
        print(Fore.CYAN + f"{name['name']}:" + Fore.RESET, end="")
        print(f"{name['description']}")
    print()
    while True:
        try:
            ask_again = input(Fore.YELLOW + "𝗚𝗼 𝗕𝗮𝗰𝗸? [𝙔][N]: " + Fore.RESET)
            if ask_again == "Y" or ask_again == "y":
                dashboard()
                break
            elif ask_again == "N" or ask_again =="n":
                exit_program()
                break
            else:
                print(Fore.RED + "Make sure the input is correct [Y][N]" + Fore.RESET)
        except ValueError:
            print(Fore.RED + "Make sure the input is correct [Y][N]" + Fore.RESET)

def exit_program():
    os.system("cls")

    phrase = ["T h a n k", " Y o u !"]

    for word in phrase:
        name_format  = pyfiglet.figlet_format(word)
        print(name_format, end="")
        time.sleep(0.5)

    print("Thank you for using this application!")
          
def use_look():

    os.system("cls")

    # ask the user for input and only accept those numbers, minimum of 100 up to maximum of 350
    track_limit = if_integer("Input Num. of Tracks: ")
    while track_limit < 100 or track_limit > 350:
        if track_limit < 100:
            print("The track minimum isn't reached, Min: 100")
        elif track_limit > 350:
            print("The track maximum is reached, Max: 350")
        track_limit = if_integer("Input Num. of Tracks: ")

    track_limit -= 1

    # other lines of code that request additional information from the user,
    # such as the previous track and the current track
    before_track = if_integer("Input Previous Track: ")
    while before_track < 0 or before_track > track_limit:
        if before_track < 0:
            print("The previous track isn't reached, Min: 0")
        elif before_track > track_limit:
            print(f"The previous track is reached, Min: {track_limit}")
        before_track = if_integer("Input Previous Track: ")

    now_track = if_integer("Input Current Track: ")
    while now_track < 0 or now_track > track_limit:
        if now_track < 0:
            print("The current track isn't reached, Min: 0")
        elif now_track > track_limit:
            print(f"The current track is reached, Min: {track_limit}")
        now_track = if_integer("Input Current Track: ")

    seek = if_integer("Input Seek Rate: ")
    while seek < 1:
        if seek < 1:
            print("The seek rate isn't reached, Min: 1")
        seek = if_integer("Input Seek Rate: ")

    # this is a function call or routine that asks the user to enter disk tracks
    disk_tracks  = input_tracks(track_limit)

    # this is a function call or routine for finding the movement of the graph
    left_wing, right_wing, movement = find_movement(disk_tracks, now_track, before_track, track_limit)

    # this is a function call or routine for computing the sum of the overhead movement and sum of seek rate
    push_graph, overhead_movement, sum_of_overhead_movement, sum_of_seek, sum_of_seek_secs \
        = look_computation(now_track, seek, left_wing, right_wing, movement)

    # this is a function call or routine for showing the graph of look scheduling
    plot_look_algo(push_graph)

    # this is a function call or routine for showing the final result of the look_computation()
    show_result(overhead_movement, sum_of_overhead_movement, seek, sum_of_seek, sum_of_seek_secs)

def if_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(Fore.CYAN + "Make sure the entered track is an integer" + Fore.RESET)

# this is a function or routine that asks the user for input, specifically number of requested tracks and the tracks
def input_tracks(track_limit):

    # ask the user for number of requested tracks and only accepts those between 10 and 25
    user_req_track = if_integer("Enter No. of Requested Tracks: ")
    while user_req_track < 10 or user_req_track > 25:
        if user_req_track < 10:
            print("The track minimum isn't reached, Min: 10")
        elif user_req_track > 25:
            print("The track maximum is reached, Max: 25")
        user_req_track = if_integer("Enter No. of Requested Tracks: ")

    # initializing a disk track (list) where each track will be stored
    disk_tracks = []
    disk_tracks.clear()
    roman = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',
             'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII',
             'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV']

    # a for loop for asking the user to input each track up to the limit
    for x in range(user_req_track): # 0, 1, 2, ... 9
        while True:
            track_choice = if_integer(f"Input Each Track {roman[x]} - ")
            if 0 <= track_choice <= track_limit:
                disk_tracks.append(track_choice)
                break
            else:
                if track_choice < 0:
                    print("Track limit isn't reached, Min: 0")
                elif track_choice > track_limit:
                    print(f"Track limit is reached, Max: {track_limit}")

    # a feature where it will wait for like 5 seconds before showing the graph
    spinner = ["|", "/", "-", "\\"]  # spinner characters
    print(Fore.RED + "\n\t\t\t\t\t\t\t  Calculating " + Fore.RESET, end="")
    for x in range(10):  # Run for 10 iterations
        for char in spinner:
            print(Fore.GREEN + f"\b{char}" + Fore.RESET, end="", flush=True )  # overwrite the previous character
            time.sleep(0.1)

    # returns the number of requested tracks and the disk tracks where each track is stored
    return list(set(disk_tracks))

# this is a function or routine for determining the movement or direction of the line graph
def find_movement(disk_tracks, now_track, before_track, track_limit):

    # checks if the current and prev track is in the list, if these are in the list
    # it will be removed since the current and previous tracks cannot be repeated
    while now_track in disk_tracks:
        disk_tracks.remove(now_track)
    while before_track in disk_tracks:
        disk_tracks.remove(before_track)

    # initializing two lists named left_wing and right_wing
    left_wing = []
    right_wing = []
    # this will iterate in the disk_tracks index by index to identify which track
    # is less than the current track and which are greater than the current track
    for x in disk_tracks:
        if x < now_track:
            left_wing.append(x)
        else:
            right_wing.append(x)

    # to make sure that both lists are sorted from lowest to highest, we use a sorted() function
    left_wing = sorted(left_wing)
    right_wing = sorted(right_wing)

    while len(left_wing) == 0 or len(right_wing) == 0:
        if len(left_wing) == 0:
            print(Fore.CYAN + "\nThe left track should have at least one requested track" + Fore.RESET)
        elif len(right_wing) == 0:
            print(Fore.CYAN + "\nThe right track should have at least one requested track" + Fore.RESET)

        while True:
            try:
                answer = input(Fore.YELLOW + "Try Again?: [Y][N]: " + Fore.RESET)
                if answer == "Y" or answer == "y":
                    print()
                    disk_tracks = input_tracks(track_limit)

                    left_wing = []
                    right_wing = []

                    for x in disk_tracks:
                        if x < now_track:
                            left_wing.append(x)
                        else:
                            right_wing.append(x)

                    left_wing = sorted(left_wing)
                    right_wing = sorted(right_wing)

                    if len(left_wing) > 0 and len(right_wing) > 0:
                        break
                elif answer == "N" or answer == "n":
                    exit_program()
                    break
                else:
                    print(Fore.RED + "Make sure the input is correct [Y][N]" + Fore.RESET)
            except ValueError:
                print(Fore.RED + "Make sure the input is correct [Y][N]" + Fore.RESET)

        if len(left_wing) > 0 and len(right_wing) > 0:
            break

    # these line of codes are used to identify if the movement will be from right to left or vice versa
    movement = None
    if now_track < before_track:
        movement = "left movement"
    elif now_track > before_track:
        movement = "right movement"
    # returns the left and right, as well as the movement/direction of the graph
    return left_wing, right_wing, movement

# this is a function or routine that computes the sum of the overhead movement and sum of seek rate
def look_computation(now_track, seek, left_wing, right_wing, movement):
    # initialization of local variables
    overhead_order = []
    push_graph = [now_track]
    sum_of_overhead_movement = float(0)

    # an if else statement for appending and calculating the sum of the overhead movement
    if movement == "right movement":
        # from max track to the current track
        if right_wing:
            overhead_order.append(f"({right_wing[-1]}-{now_track})")
            push_graph.append(right_wing[-1])
            overhead = abs(right_wing[-1] - now_track)
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
            overhead_order.append(f"({now_track}-{left_wing[0]})")
            push_graph.append(left_wing[0])
            overhead = abs(now_track - left_wing[0])
            sum_of_overhead_movement = sum_of_overhead_movement + overhead
        # from rightmost value in right list to 0
        if right_wing:
            overhead_order.append(f"({right_wing[-1]}-{left_wing[0]})")
            push_graph.append(right_wing[-1])
            overhead = abs(right_wing[-1] - left_wing[0])
            sum_of_overhead_movement = sum_of_overhead_movement + overhead

    # this is the formula for computing the sum of seek rate and seek rate in seconds
    sum_of_seek = float(seek * sum_of_overhead_movement)
    sum_of_seek_secs = float(sum_of_seek / 1000)
    overhead_movement = " + ".join(map(str, overhead_order))

    # returns multiple arguments for the next function
    return push_graph, overhead_movement, sum_of_overhead_movement, sum_of_seek, sum_of_seek_secs

# this is a function or routine that plots the graph of look scheduling
def plot_look_algo(push_graph):
    # separating the figure and axes for better organization
    fig, ax = plt.subplots()
    i = push_graph # passing the values of push_graph list
    j = list(range(len(i))) # getting the length of i and then making it as a value of a list

    # shows the title of the algorithm
    plt.title("'LOOK' DISK SCHEDULING ALGORITHM", color="gold", weight="semibold", size="15", fontstyle="italic", family="DejaVu Sans Mono")
    # shows the actual line
    plt.plot(i, j, color="#000080", markerfacecolor="orange", marker="D", markersize=5, linewidth=2.7)
    # this means that the y-axes' label will be hidden
    plt.gca().set_yticklabels([])
    plt.gca().invert_yaxis()  # invert the value of y from highest to lowest
    plt.gca().xaxis.set_label_position('top')  # move the x-axis label to the top
    plt.gca().xaxis.tick_top()
    plt.gca().set_facecolor("lightyellow") #setting the color of the box as light yellow
    plt.gca().spines['bottom'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    sentence = "-----> Please Close the Window to See Results <-----"
    fig.text(0.5 , 0.03, sentence, weight="bold", color="orange",fontsize=10.5, ha="center", font="DejaVu Sans Mono")
    plt.show() # showing the final illustration of the graph

# this is a function or routine that basically show the final result
def show_result(overhead_movement, sum_of_overhead_movement, seek, sum_of_seek, sum_of_seek_secs):
    """this function basically shows the result of the look scheduling algorithm"""
    final_result = (f"Total Head Movement: {overhead_movement} = {sum_of_overhead_movement}\n"
                        f"\nSeek Rate: {sum_of_overhead_movement} * {seek}\n\n"
                        f"Seek Rate: {sum_of_seek}ms or {sum_of_seek_secs}secs")

    # this is a messagebox that shows the result, imported from tkinter
    messagebox.showinfo(title="Disk Scheduling Calculation Result",  message=final_result)

# the main function that asks user for overall information
def dashboard():

    while True:
        os.system("cls")
        # header for disk scheduling
        print(Fore.MAGENTA + "\t\t\t\t✩♬ ₊˚.🎧⋆☾⋆⁺₊✧ 𝙒𝙚𝙡𝙘𝙤𝙢𝙚 𝙩𝙤 𝙇𝙊𝙊𝙆 𝘼𝙡𝙜𝙤𝙧𝙞𝙩𝙝𝙢 ✩♬ ₊˚.⋆☾⋆⁺₊✧")
        print("""
        \t\t\t\t\t\t    ──────────୨ৎ────────── 
        \t\t\t\t\t\t  𝐌𝐀𝐈𝐍𝐃𝐀𝐒𝐇𝐁𝐎𝐀𝐑𝐃     
        \t\t\t\t\t\t    ──────────୨ৎ──────────  
        \t\t\t\t\t\t    [𝗔] Use Look ⚝
        \t\t\t\t\t\t    [𝗕] Credits  ♪
        \t\t\t\t\t\t    [𝗖] Exit   ☾    
        """ + Fore.RESET)
        user_option = input(Fore.MAGENTA + "\t\t\t\t\t\t\t    Enter Option [𝗔-𝗖]: " + Fore.RESET)

        if user_option == "A" or user_option == "a":
            use_look()
        elif user_option == "B" or user_option == "b":
            group_credits()
            break
        elif user_option == "C" or user_option == "c":
            exit_program()
            break
        else:
            print()
            print(Fore.RED + "\t\t\t\t\t\t\t  Enter Correct Option [𝗔-𝗖]" + Fore.RESET)
            time.sleep(1)
            os.system("cls")

if __name__ == "__main__":
    dashboard()