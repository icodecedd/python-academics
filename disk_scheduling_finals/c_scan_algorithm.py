import time
from matplotlib import pyplot as show
import os

def ComputeCScan(NoTracks, CurrTrack, SeekRate, Alpha, Left, Right, Direction):
    TotalHeadMovement = 0
    TotalSeekRate = float(0)
    TotalHeadMovementOrder = []
    DefaultTracks = [0, CurrTrack, NoTracks - 1]
    GraphCScan = []

    if Direction == "Left":

        InitialHeadMovement = abs(CurrTrack - 0)
        TotalHeadMovement += InitialHeadMovement
        TotalHeadMovementOrder.append(f"({CurrTrack} - {0})")
        GraphCScan.insert(0, DefaultTracks[1])
        GraphCScan.insert(1, DefaultTracks[0])
        GraphCScan.insert(2, DefaultTracks[2])
        InitialHeadMovement = abs(DefaultTracks[2] - Right[0])
        TotalHeadMovement += InitialHeadMovement
        TotalHeadMovementOrder.append(f"({DefaultTracks[2]} - {Right[0]})")
        TotalHeadMovementOrder.append(f"{Alpha}")
        GraphCScan.extend([Right[0]])
    else:
        InitialHeadMovement = abs(NoTracks - 1 - CurrTrack)  # From current track to the rightmost track
        TotalHeadMovement += InitialHeadMovement
        TotalHeadMovementOrder.append(f"({NoTracks - 1} - {CurrTrack})")
        GraphCScan.insert(0, DefaultTracks[1]) # 110
        GraphCScan.insert(1, DefaultTracks[2]) # 149
        GraphCScan.insert(2, DefaultTracks[0]) # 0
        InitialHeadMovement = abs(Left[1] - 0)  # From rightmost to leftmost track
        TotalHeadMovement += InitialHeadMovement
        TotalHeadMovementOrder.append(f"({Left[1]} - {0})")
        TotalHeadMovementOrder.append(f"{Alpha}")
        GraphCScan.extend([Left[1]])

    FinalHeadMovement = TotalHeadMovement + Alpha
    ShowTotalHeadMovement = " + ".join(map(str, TotalHeadMovementOrder))
    TotalSeekRate += SeekRate * FinalHeadMovement
    TotalSeekRateInSeconds = float(TotalSeekRate / 1000)

    print(f"""
    ════════════════════════════════════════════════════════════════════════════
        Total Head Movement: {ShowTotalHeadMovement} = {FinalHeadMovement} 
        Seek Rate: {FinalHeadMovement} * {SeekRate}                             
        Seek Rate [ms]: {TotalSeekRate}ms                                       
        Seek Rate [sec]: {TotalSeekRateInSeconds}sec                               
    ════════════════════════════════════════════════════════════════════════════   
         """)

    Domain = GraphCScan
    Range = []
    GetDomainLength = len(Domain)
    for Value in range(GetDomainLength):
        Range.append(Value)
    LinesTypes = ["-", "--", "-"]

    if NoTracks <= 150:
        Gap = 25
    else:
        Gap = 50

    show.title("CIRCULAR SCAN DISK SCHEDULING ALGORITHM", color="#13072e", font="Algerian", size=18)
    for segment in range(GetDomainLength - 1):
        show.plot(Domain[segment:segment + 2], Range[segment:segment + 2], color="black", markerfacecolor='#b3aaff',
                  marker='o', markersize=4, linewidth=2, linestyle=LinesTypes[segment])
    show.yticks([])
    show.xticks(range(0, NoTracks + 1, Gap))
    show.gca().invert_yaxis()
    show.gca().xaxis.set_label_position('top')  # Move the label to the top
    show.gca().xaxis.tick_top()
    ShowAlphaSymbol = round(NoTracks / 2)
    show.gca().spines['bottom'].set_visible(False)
    show.gca().spines['right'].set_visible(False)
    show.gca().spines['left'].set_visible(False)
    show.text(ShowAlphaSymbol, 1.2, "α", fontsize=20, color="#3f2182", ha="center", va="center")
    show.show()

def StartCScan():
    os.system("cls") # clearscreen

    # this serves as the main header for the C-Scan
    print("""\n
    \t\t\t\t\t╔════════════════════════════════════════╗  
    \t\t\t\t\t║                                        ║
    \t\t\t\t\t║    Welcome Back! Let’s Get Started!    ║
    \t\t\t\t\t║          GROUP CIRCULAR SCAN           ║
    \t\t\t\t\t║                                        ║
    \t\t\t\t\t╚════════════════════════════════════════╝   
        """)

    Name = input("Please enter your name [Press enter to skip]: ")
    CapName = Name.capitalize()

    Welcome1 = "\nHello there, User. Welcome to C-SCAN!"
    Welcome2 = f"\nHello, {CapName}. Welcome to C-SCAN!"
    if Name == "":
        for char in Welcome1:
            print(char, end="", flush=True)
            time.sleep(0.05)
    else:
        for char in Welcome2:
            print(char, end="", flush=True)
            time.sleep(0.05)
    
    print("\n")
    while True:
        YesOrNo = input("Ready to Begin? [Press Y]: ")
        if YesOrNo == 'Y' or YesOrNo == 'y':
            break
        else:
            print("Invalid input. Please press 'Y' to start.")
    
    os.system("cls") # clearscreen

    # this is the starting point of asking the user for inputs
    while True:
        NoTracks = input("Enter No. of Tracks: ")
        if NoTracks.isdigit():
            NoTracks = int(NoTracks)
            if 100 <= NoTracks <= 350:
                break
            else:
                print("Invalid input. Please input [100 - 350]")
        else:
            print("Invalid input. Please input natural numbers only")

    while True:
        PrevTrack = input("Enter Previous Track: ")
        if PrevTrack.isdigit():
            PrevTrack = int(PrevTrack)
            if 0 <= PrevTrack <= NoTracks-1:
                break
            else:
                print(f"Invalid input. Please input [0 - {NoTracks-1}]")
        else:
            print("Invalid input. Please input natural numbers only")

    while True:
        CurrTrack = input("Enter Current Track: ")
        if CurrTrack.isdigit():
            CurrTrack = int(CurrTrack)
            if 0 <= CurrTrack <= NoTracks-1:
                break
            else:
                print(f"Invalid input. Please input [0 - {NoTracks-1}]")
        else:
            print("Invalid input. Please input natural numbers only")

    Tracks = []
    UnFilteredLeft = []
    UnFilteredRight = []
    Direction = None

    while True:
        NoRequestedTrack = input("Enter No. of Requested Tracks: ")
        if NoRequestedTrack.isdigit():
            NoRequestedTrack = int(NoRequestedTrack)
            if 10 <= NoRequestedTrack <= 25: 
                break
            else:
                print("Invalid input. Please input [10 - 25]")
        else:
            print("Invalid input. Please input natural numbers only")

        while True:
            StringTracks = input("Enter Requested Tracks(Separated by Commas):\n=> ")
            SeparateTrack = StringTracks.split(",")

            if len(SeparateTrack) != NoRequestedTrack:
                print(f"Invalid input. Please enter the correct number of requested tracks [{NoRequestedTrack}]")
                continue

            IsValid = True
            for TrackEntry in SeparateTrack:
                TrackEntry = TrackEntry.strip()
                if TrackEntry.isdigit():
                    TrackInteger = int(TrackEntry)
                    if TrackInteger < NoTracks-1:
                        Tracks.append(TrackInteger)
                    else:
                        print(f"Invalid Input. Please make sure all of the tracks are between  0 and {NoTracks-1}")
                        IsValid = False
                else:
                    print("Invalid input. Please make sure all of the tracks are natural numbers")
                    IsValid = False
                    break

            LessThanTracks = False
            GreaterThanTracks = False

            if IsValid:
                for Track in Tracks:
                    if Track < CurrTrack:
                        LessThanTracks = True
                        break

                for Track in Tracks:
                    if Track > CurrTrack:
                        GreaterThanTracks = True
                        break

                if not LessThanTracks or not GreaterThanTracks:
                    print(f"Invalid input. At least one track must be higher or lower than the current track [{CurrTrack}].")
                else:
                    break

    while True:
        SeekRate = input("Enter Seek Rate: ")
        if SeekRate.isdigit():
            SeekRate = int(SeekRate)
            if 0 < SeekRate :
                break
            else:
                print("Invalid input. Please input [1 and above numbers]")
        else:
            print("Invalid input. Please input natural numbers only")

    while True:
        Alpha = input("Enter Alpha: ")
        if Alpha.isdigit():
            Alpha = int(Alpha)
            if 0 < Alpha:
                break
            else:
                print("Invalid input. Please input [1 and above numbers]")
        else:
            print("Invalid input. Please input natural numbers only")

    FilteredTracks = []
    for Track in Tracks:
        if Track != CurrTrack and Track != PrevTrack:
            FilteredTracks.append(Track)

    Tracks = FilteredTracks

    IsSeen = set()
    FilteredDiskTracks = []
    for Track in Tracks:
        if Track not in IsSeen:
            FilteredDiskTracks.append(Track)
            IsSeen.add(Track)
    Tracks = FilteredDiskTracks

    for track in Tracks:
        if track < CurrTrack:
            UnFilteredLeft.append(track) # 85, 70, 60, 50, 35. 105
        else:
            UnFilteredRight.append(track)

    Left = []
    Right = []
    Left.append(min(UnFilteredLeft))
    Left.append(max(UnFilteredLeft))
    Right.append(min(UnFilteredRight))
    Right.append(max(UnFilteredRight)) 

    if CurrTrack < PrevTrack:
        Direction = "Left"
    elif CurrTrack > PrevTrack:
        Direction = "Right"

    print("Requested Tracks:", end=" ")
    # map(str, Tracks) - converts each element of Tracks to a string. returns an iterator
    # " | ".join(...) - joins the elements of the iterator into a single string, with " | " as the separator
    ReqTracks = " | ".join(map(str, Tracks))
    print(ReqTracks)
    print()

    ComputeCScan(NoTracks, CurrTrack, SeekRate, Alpha, Left, Right, Direction)

if __name__ == "__main__":
    StartCScan()