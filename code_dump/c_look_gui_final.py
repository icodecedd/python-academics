import matplotlib.pyplot as plot #used to show the graph/plot of the C-LOOK algorithm

def executeCLook(noOfTracks, presentTrack, seekTime, leftRoute, rightRoute, chosenDirection, alpha):
    cLookTotalHeadMovement = 0
    cLookTotalSeekTime = 0
    sortedThmOrder = []
    plotCLookResults = []
    alphaX = []
    showThm = ""
    
    if chosenDirection == "leftRoute":
        #move from the present track to the lowest track in the left array,
        #then go to the highest track in the right array
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
            sortedThmOrder.append(alpha)
            sortedThmOrder.append(f"({rightRoute[-1]} - {rightRoute[0]})")
            plotCLookResults.append(rightRoute[0])

    elif chosenDirection == "rightRoute":
        # move from the present track to the highest track in the right list,
        #then go to the lowest track in the left list
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
            sortedThmOrder.append(alpha)
            sortedThmOrder.append(f"({leftRoute[0]} - {leftRoute[-1]})")
            plotCLookResults.append(leftRoute[0])

    cLookTotalHeadMovement = cLookTotalHeadMovement + alpha
    cLookTotalSeekTime = float(cLookTotalHeadMovement * seekTime)
    totalSeekInSeconds = float(cLookTotalSeekTime / 1000)

    for i, track in enumerate(sortedThmOrder): #each element in sortedThmOrder will be joined with a '+'
        if i > 0:
            showThm += " + "
        showThm += str(track)
    sentence = f"""
    Total Head Movement: {showThm} = {cLookTotalHeadMovement}
    Seek Time: {cLookTotalSeekTime}ms or {totalSeekInSeconds}secs"""

    #graph of the scan algorithm
    #the subplot() function you can draw multiple plots in one figure
    #fig: the figure object, which represents the entire figure or canvas
    #pt: to configure the plot, such as adding data, titles, labels, grids, or customizing ticks
    fig, pt = plot.subplots()

    #x and y data for plotting
    coordX = plotCLookResults
    coordY = list(range(len(coordX)))
    alphaY = list(range(len(alphaX)))
    alphaY = [i + 0.9 for i in alphaY]
    plotX = round(noOfTracks / 2)

    #header for the clook
    title = "CLOOK Disk Scheduling Algorithms"
    pt.set_title(title.upper(),
                 weight="bold",
                 font="Georgia",
                 color="darkviolet",
                 size="18")
    pt.plot(coordX,
            coordY,
            color="#00008B",
            markerfacecolor="#FFA500",
            marker="o",
            markersize=4,
            linewidth=2)
    pt.plot(alphaX,
            alphaY,
            dashes = [4,1.5],
            color="darkgreen",
            marker='D',
            markersize = 3,
            linewidth = 1)
    for i, (x, y) in enumerate(zip(coordX, coordY)): #shows the number of each dot
        pt.text(x, y, str(x),
                fontsize=8,
                ha='left',
                va='bottom',
                color='red')
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
    pt.text(plotX, 1.3, "α",
            fontsize=15,
            color="darkgreen",
            ha="center",
            va="center")
    pt.spines['bottom'].set_visible(False) #bottom line of the table
    pt.spines['right'].set_visible(False) #right line of the table
    pt.spines['left'].set_visible(False) #left line of the table
    pt.grid(True,
            which='both',
            axis='both',
            color='gray',
            linestyle='--',
            linewidth=0.5)
    pt.set_facecolor("lightgrey") #bg color
    fig.text(0.08, 0.03, sentence,
             ha="left",
             fontsize=10,
             fontfamily="monospace",
             color="darkviolet")
    plot.show()

def determineDirection(trackRoute, presentTrack, pastTrack):
    """this function determines the direction of the graph"""

    #checks if the present and past track is in the list of trackRoute
    excludeTrack = [presentTrack, pastTrack] #100 | #110
    for track in excludeTrack:
        while track in trackRoute:
            trackRoute.remove(track)
    # trackRoute = [85, 70, 120, 135, 60, 115, 105, 50, 35, 140]
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

def main():
    #header for c-look disk scheduling algorithm
    print("""
   \t\t\t\t\t\t\t\t\t\t\t\t\t+-----------------+-----------------+ 
   \t\t\t\t\t\t\t\t\t\t\t\t\t| C-LOOK Disk Scheduling Algorithms |
   \t\t\t\t\t\t\t\t\t\t\t\t\t+-----------------+-----------------+""")

    noOfTracks = int(input("\t\t\t\t\t\t\t\t\t\t\t\t\t  Number of Tracks: "))
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t+-----------------+-----------------+")
    while noOfTracks < 100 or noOfTracks > 350:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t  min: 100 || max: 350 only")
        noOfTracks = int(input("\t\t\t\t\t\t\t\t\t\t\t\t\t  Number of Tracks: "))
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t+-----------------+-----------------+")

    pastTrack = int(input("\t\t\t\t\t\t\t\t\t\t\t\t\t  Previous Track: "))
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t+-----------------+-----------------+")
    while pastTrack < 0 or pastTrack >=noOfTracks:
        print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t  min: 0 || max: {noOfTracks-1}")
        pastTrack = int(input("\t\t\t\t\t\t\t\t\t\t\t\t\t  Previous Track: "))
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t+-----------------+-----------------+")

    presentTrack = int(input("\t\t\t\t\t\t\t\t\t\t\t\t\t  Current Track: "))
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t+-----------------+-----------------+")
    while presentTrack < 0 or presentTrack >=noOfTracks or presentTrack == pastTrack:
        
        if presentTrack < 0 or presentTrack >=noOfTracks:
            print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t  min: 0 || max: {noOfTracks-1}")

        elif presentTrack == pastTrack:
            print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t  Current Track must not == {pastTrack}")

        presentTrack = int(input("\t\t\t\t\t\t\t\t\t\t\t\t\t  Current Track: "))
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t+-----------------+-----------------+")

    seekTime = int(input("\t\t\t\t\t\t\t\t\t\t\t\t\t  Seek Rate: "))
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t+-----------------+-----------------+")
    while seekTime <= 0:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t  Seek Time must be a Positive Number")
        seekTime = int(input("\t\t\t\t\t\t\t\t\t\t\t\t\t  Seek Rate: "))
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t+-----------------+-----------------+")

    alpha = int(input("\t\t\t\t\t\t\t\t\t\t\t\t\t  Alpha[α]: "))
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t+-----------------+-----------------+")
    while alpha <= 0:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t  Alpha must be a Positive Number")
        alpha = int(input("\t\t\t\t\t\t\t\t\t\t\t\t\t  Alpha[α]: "))
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t+-----------------+-----------------+")

    noOfReqTracks = int(input("\t\t\t\t\t\t\t\t\t\t\t\t\t  Number of Requested Tracks: "))
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t+-----------------+-----------------+")
    while noOfReqTracks < 10 or noOfReqTracks > 25:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t  min: 10 || max: 25 only")
        noOfReqTracks = int(input("\t\t\t\t\t\t\t\t\t\t\t\t\t  Number of Requested Tracks: "))
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t+-----------------+-----------------+")
    
    trackRoute = []

    #prompts user to input requested track 
    for x in range(noOfReqTracks):
        while True:
            perTrack = input(f"\t\t\t\t\t\t\t\t\t\t\t\t\t  Requested Track [{x + 1}]: ")
            print("\t\t\t\t\t\t\t\t\t\t\t\t\t+-----------------+-----------------+")
            if perTrack == "":
                print("\t\t\t\t\t\t\t\t\t\t\t\t\t  Please Enter a Valid Track")
                continue
            try:
                perTrack = int(perTrack)
                if perTrack < 0:
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t  Track must be Positive Integers only")
                elif perTrack >= noOfTracks-1:
                    print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t  Exceeds the No. of Tracks ({noOfTracks-1})")
                else:
                    trackRoute.append(perTrack)
                    break
            except ValueError:
                print("\t\t\t\t\t\t\t\t\t\t\t\t\t  Inputs must be INTEGERS only")

    #function call for determineDirection returns the direction and other info
    leftRoute, rightRoute, chosenDirection = determineDirection(trackRoute, presentTrack, pastTrack)

    # function call for executeCLook and does not return any value
    executeCLook(noOfTracks, presentTrack, seekTime, leftRoute, rightRoute, chosenDirection, alpha)

if __name__ == "__main__":
    main()