"""
this SCAN Algorithm implementation is designed to be executed in a terminal or
command-line console to ensure proper functionality.
"""
# imported the matplotlib library for plotting the graph
from matplotlib import pyplot as py
from rich.console import Console
from rich.panel import Panel
import os, msvcrt, time  # for 'cls', getch()
from tqdm import tqdm # for progress bar

def scan_header():
    # clears the screen or console window
    os.system("cls")

    # the main header for scan
    console = Console()


    welcome_text = "\t      Welcome to SCAN Disk Scheduling"
    press_text = "\t       »» Press enter to continue ««"

    panel = Panel(
        """ 
       [italic red]Polytechnic University of the Philippines
                    San Juan Campus
                     San Juan City[/italic red]

               [bold bright_magenta]Marquez, Eunice Julianna S.[/bold bright_magenta]
                [bold bright_magenta]Sajulan, Vann Augustine J.[/bold bright_magenta]
                 [bold bright_magenta]Segotier, Jesalyn Seidel[/bold bright_magenta]
        """,
        title="SCAN Disk Scheduling",
        border_style="bold indian_red1",
        width=61
    )

    console.print(panel)

    cons_delay = 0.03

    for letter in welcome_text:
        console.print(letter, end="", style="bold dark_orange")
        time.sleep(cons_delay)
    print()
    
    for letter in press_text:
        console.print(letter, end="", style="bold light_salmon3")
        time.sleep(cons_delay)
    print("\n")
    msvcrt.getch()

    console.print("\n\t\t\t\tStarting", style="bold deep_pink4")
    for num in tqdm(range(100), desc="", ncols=100, colour="cyan"):
        time.sleep(0.02)
    
    start = "Start-Up Complete!"
    for letter in start:
        console.print(letter, end="", style="bold light_salmon3")
        time.sleep(cons_delay)
    
    time.sleep(1)
    os.system("cls")

def check_if_valid(variable_name, sentence, fixed_min, fixed_max):

    console = Console()

    cons_delay = 0.01

    while True:

        for letter in sentence:
            console.print(letter, end="", style="medium_orchid3")
            time.sleep(cons_delay)
        user_value = input() 

        try:
            user_value = int(user_value)
        except ValueError:
            error_message = f"{variable_name} must be an integer"
            for letter in error_message:
                console.print(letter, end="", style="red3")
                time.sleep(cons_delay)
            print()
            continue

        if fixed_min <= user_value <= fixed_max:
            return user_value
        else:
            message = f"{variable_name} must be between {fixed_min} and {fixed_max}"
            for letter in message:
                console.print(letter, end="", style="yellow2")
                time.sleep(cons_delay)
            print()


def ask_requested_tracks(number_of_req_track, number_of_tracks):
    
    console = Console()
    cons_delay = 0.01

    tracks = []  
    # prompts the user to input each track
    for count in range(1, number_of_req_track + 1):
        while not False:
            try:
                track_message = f"Req Track {count}:   "
                for letter in track_message:
                    console.print(letter, end="", style="medium_orchid3")
                    time.sleep(cons_delay)
                entered_track = int(input())

                if entered_track in range(0, number_of_tracks - 1):
                    tracks.append(entered_track)
                    break
                else:
                    error_message = f"Track number must be between 0 and {number_of_tracks - 1}"
                    for letter in error_message:
                        console.print(letter, end="", style="yellow2")
                        time.sleep(cons_delay)
                    print()

            except ValueError:
                value_error = "Track number must be an integer"
                for letter in value_error:
                    console.print(letter, end="", style="red3")
                    time.sleep(cons_delay)
                print()
    
    return tracks

def find_right_left(tracks, current_track, number_of_req_track, number_of_tracks):
    """
    identifies and separates the tracks into two lists:
    - tracks to the right of the current track (greater than current_track).
    - tracks to the left of the current track (less than current_track).
    """
    console = Console()

    # divides the list (tracks) into left list and right list
    while True:
        left, right = [], []
        
        for i in tracks:
            if i > current_track:
                right.append(i)
            else:
                left.append(i)
        
        if left and right:
            break
        else:
            if not left:
                error_message = "Left track list is empty. Please enter new tracks."
                for letter in error_message:
                    console.print(letter, end="", style="red3")
                    time.sleep(0.02)
                print()
            
            if not right:
                error_message = "Right track list is empty. Please enter new tracks."
                for letter in error_message:
                    console.print(letter, end="", style="red3")
                    time.sleep(0.02)
                print()
            
            tracks = ask_requested_tracks(number_of_req_track, number_of_tracks)

    left.sort(reverse=True)  # sort the left list from highest to lowest
    right.sort()  # sort the right list from lowest to highest

    return left, right

def direction_left(right, head_movement_order, scan_graph, total_head_movement, current_track):

    # move from the current track to the lowest track in the left list
    movements = abs(current_track - 0)
    total_head_movement += movements
    head_movement_order.append(f"({current_track} - {0})")
    scan_graph.append(current_track)  # append the value for the graph
    scan_graph.append(0)
    movements = abs(right[-1] - 0)  # from right most value in right list to 0
    total_head_movement += movements
    head_movement_order.append(f"({right[-1]} - {0})")  # the [-1] means it will access the last element
    scan_graph.append(right[-1])

    return head_movement_order, scan_graph, total_head_movement

def direction_right(left, head_movement_order, scan_graph, total_head_movement, current_track, number_of_tracks):

    movements = abs((number_of_tracks - 1) - current_track)
    total_head_movement += movements
    head_movement_order.append(f"({number_of_tracks - 1} - {current_track})")
    scan_graph.append(current_track)
    scan_graph.append(number_of_tracks - 1)
    movements = abs((number_of_tracks - 1) - left[-1])
    total_head_movement += movements
    head_movement_order.append(f"({number_of_tracks - 1} - {left[-1]})")
    scan_graph.append(left[-1])

    return head_movement_order, scan_graph, total_head_movement

# a function that accept multiple arguments, but does not return any value
def show_scan(tracks, number_of_tracks, current_track, previous_track, seek_rate, number_of_req_track):
    """
    this function calculates the Total Head Movement (THM), Seek Rate, and
    generates a graphical representation of the disk arm's movement based
    on a given disk scheduling algorithm.
    """

    # initialization of variables to be used in this function
    total_head_movement, total_seek_rate = 0, float(0)
    head_movement_order, scan_graph = [], []
    direction = ""

    console = Console()

    # a function call for dividing the general track into two separate lists
    left, right = find_right_left(tracks, current_track, number_of_req_track, number_of_tracks)

    # determine whether the direction will start from left or right or vice versa
    if current_track > previous_track:
        direction = "right"
    elif current_track < previous_track:
        direction = "left"

    # this will determine the sequence of the [scan_graph] variable
    # if direction is left the graph will move from left to right
    if direction == "left":

        head_movement_order, scan_graph, total_head_movement = direction_left(right, head_movement_order,
                                                                              scan_graph, total_head_movement,
                                                                              current_track)

    # if direction is right the graph will move from right to left
    elif direction == "right":

        head_movement_order, scan_graph, total_head_movement = direction_right(left, head_movement_order,
                                                                              scan_graph, total_head_movement,
                                                                              current_track, number_of_tracks)

    head_movement_order = map(str, head_movement_order)
    output_thm = " + ".join(head_movement_order)

    os.system("cls")

    cons_delay = 0.02

    total_seek_rate = seek_rate * total_head_movement
    tot_seek_secs = float(total_seek_rate / 1000)

    total_head_message = f"»» Total Head Movement: {output_thm} = {total_head_movement:,}"
    total_seek_message = f"»» Seek Rate: {total_head_movement:,} * {seek_rate}"
    total_seek_sec_message = f"»» Seek Rate: {total_seek_rate:,} milliseconds or {tot_seek_secs} seconds"
    title = "SCAN Disk Scheduling Algorithm Results"
    description = "The SCAN (Elevator) Disk Scheduling Algorithm is designed to\noptimize the movement of the disk read/write head, reducing\nseek time and improving overall disk performance."
    
    for letter in title:
        console.print(letter, end="", style="bold deep_pink4")
        time.sleep(0.02)

    print("\n")

    for letter in description:
        console.print(letter, end="", style="hot_pink3")
        time.sleep(0.03)

    print("\n")
    

    for letter in total_head_message:
        console.print(letter, end="", style="light_pink1")
        time.sleep(cons_delay)
    print()
    
    for letter in total_seek_message:
        console.print(letter, end="", style="light_pink1")
        time.sleep(cons_delay)
    print()
    
    for letter in total_seek_sec_message:
        console.print(letter, end="", style="light_pink1")
        time.sleep(cons_delay)
    print()

    # this will show the graph using matplotlib
    x = scan_graph
    y = list(range(len(scan_graph)))

    if number_of_tracks <= 100:
        partition = 10
    elif number_of_tracks <= 150:
        partition = 15
    elif number_of_tracks <= 200:
        partition = 20
    elif number_of_tracks <= 250:
        partition = 25
    elif number_of_tracks <= 300:
        partition = 30
    else:
        partition = 35

    py.title("Disk Scheduling: SCAN Algorithm", color="#FF6F61", weight="bold")
    py.plot(x, y, color="#4CAF50", markerfacecolor="#FFFFFF", marker="o", markersize=4.5, linewidth=2.5)
    for i, (x, y) in enumerate(zip(x, y)):  # shows the number of each dot
        py.text(x, y, str(x), fontsize=8, ha="left", va="bottom", color="#E63946")
    py.gca().set_yticklabels([])  # removes the y-axis label
    py.xticks(range(0, number_of_tracks + 1, partition))
    py.gca().invert_yaxis()  # gca - get current axes and invert the y-axis values
    py.gca().xaxis.tick_top()  # move the x-axis to the top
    py.gca().set_facecolor("#FFD8D2")
    py.gcf().set_facecolor("#FFEDEB")
    py.show()

def main_interface():
    # initialization of local variables
    tracks = []

    console = Console()

    title = "Welcome to the Scan Algorithm Simulation!"
    description = "The Scan Algorithm, also known as the Elevator\nAlgorithm, is a disk scheduling algorithm used to\noptimize the movement of a disk's read/write head."

    scan_header() # function call for the header

    for letter in title:
        console.print(letter, end="", style="bold deep_pink4")
        time.sleep(0.02)

    print("\n")

    for letter in description:
        console.print(letter, end="", style="hot_pink3")
        time.sleep(0.03)

    print("\n")

    # prompts the user to input number of requested track
    number_of_req_track = check_if_valid("No. of Req Track", "Enter Number of Requested Tracks:    ", 10, 25)

    # prompts the user to input number of tracks
    number_of_tracks = check_if_valid("No. of Track", "Enter Number of Tracks:              ", 100, 350)

    # prompts the user to input previous track
    previous_track = check_if_valid("Previous Track", "Enter Previous Track:                ", 0, number_of_tracks-1)

    # prompts the user to input current track
    current_track = check_if_valid("Current Track", "Enter Current Track:                 ", 0, number_of_tracks-1)

    # prompts the user to input seek rate
    seek_rate = check_if_valid("Seek Rate", "Enter Seek Rate:                     ", 1, float('inf'))

    tracks = ask_requested_tracks(number_of_req_track, number_of_tracks)

    # remove the current track and previous track in the list (tracks)
    for i in [current_track, previous_track]:
        while i in tracks:
            tracks.remove(i)
    
    # remove the duplicated track so it won't be plotted later on
    check_duplicate = set()
    # it's called list comprehension when a function or expression is directly embedded inside a list
    processed_tracks = [x for x in tracks if x not in check_duplicate and not check_duplicate.add(x)]  
    tracks = processed_tracks

    # a function call for show_scan, this will process the entered data from the user
    show_scan(tracks, number_of_tracks, current_track, previous_track, seek_rate, number_of_req_track)

main_interface()  # a function call for main_interface() function