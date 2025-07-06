from matplotlib import pyplot as gr

def compute_fcfs(curr_track, tracks, seek_rate):
    total_head_movement = 0
    total_seek_rate = float(0)
    thm_order = []
    scan_graph = [tracks]
    previous_track = curr_track

    for track in tracks:

        total_head_movement += abs(track - previous_track)
        if previous_track < track:
            thm_order.append(f"({track}-{previous_track})")
        else:
            thm_order.append(f"({previous_track}-{track})")
        previous_track = track

    thm = "+".join(map(str, thm_order))
    print(f"Total Head Movement: {thm} = {total_head_movement}")
    total_seek_rate += seek_rate * total_head_movement
    tot_sk_secs = float(total_seek_rate / 1000)
    print(f"Seek Rate: {total_head_movement} * {seek_rate}")
    print(f"Seek Rate: {total_seek_rate}ms or {tot_sk_secs}secs")

    tracks.insert(0, curr_track)
    x = tracks
    y = list(range(len(tracks)))

    gr.plot(x,y, color="black", markerfacecolor="yellow", marker="o", markersize=5)
    gr.gca().invert_yaxis()
    gr.gca().xaxis.set_label_position('top')  # Move the label to the top
    gr.gca().xaxis.tick_top()
    gr.title("FIFO DISK ALGORITHM", size=13)
    gr.grid()
    gr.show()

def main():
    no_tracks = int(input("Enter No. of Tracks: "))
    prev_track = int(input("Enter Previous Track: "))
    curr_track = int(input("Enter Current Track: "))
    seek_rate = int(input("Enter Seek Rate: "))
    tracks = []
    no_req_track = int(input("Enter No. of Requested Tracks: "))

    for x in range(1, no_req_track+1):
        while True:
            track = int(input(f"Req Track {x}: "))
            if track < no_tracks:
                tracks.append(track)
                break
            else:
                print("Exceeds the No. of Tracks")

    if curr_track in tracks:
        tracks.remove(curr_track)
    elif prev_track in tracks:
        tracks.remove(prev_track)

    compute_fcfs(curr_track, tracks, seek_rate)

if __name__ == "__main__":
    main()