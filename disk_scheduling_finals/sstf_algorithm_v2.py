from matplotlib import pyplot
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.theme import Theme
from rich.progress import track
import time  # sleep
import os  # clear screen


def find_shortest_seek(active_track, last_track, track_queue):
    cons_active_track = active_track
    total_head_movement = 0
    head_access_sequence = []
    sorted_tracks = []

    # determine initial direction
    if last_track < active_track:
        direction = "up"
    else:
        direction = "down"

    while track_queue:  # continue until all tracks are processed
        # initialize variables for finding the closest track
        min_distance = float("inf")  # 25
        closest_tracks = []

        # find the minimum distance
        for track in track_queue:
            distance = abs(track - active_track)
            if distance < min_distance:
                min_distance = distance
                closest_tracks = [track]
            elif distance == min_distance:
                closest_tracks.append(track)

        # resolve ties based on direction
        if len(closest_tracks) > 1:
            if direction == "up":
                nearest_track = max(closest_tracks)  # prefer the higher track
            else:
                nearest_track = min(closest_tracks)  # prefer the lower track
        else:
            nearest_track = closest_tracks[0]

        # update direction
        if nearest_track > active_track:
            direction = "up"
        else:
            direction = "down"

        # update total head movement and track order

        total_head_movement = total_head_movement + abs(nearest_track - active_track)

        # update current track
        active_track = nearest_track

        # record the sequence of tracks accessed
        sorted_tracks.append(nearest_track)

        # remove the processed track
        for i in range(len(track_queue)):
            if track_queue[i] == nearest_track:
                del track_queue[i]
                break

    filtered_sorted_tracks = [cons_active_track]
    for index in range(1, len(sorted_tracks) - 1):
        previous = sorted_tracks[index - 1]
        current = sorted_tracks[index]
        next = sorted_tracks[index + 1]
        # Check for a change in direction
        if (previous < current > next) or (previous > current < next):
            filtered_sorted_tracks.append(current)
        else:
            continue

    filtered_sorted_tracks.append(sorted_tracks[-1])

    for track in filtered_sorted_tracks[1:]:

        if cons_active_track > track:
            head_access_sequence.append(f"({cons_active_track}-{track})")
        else:
            head_access_sequence.append(f"({track}-{cons_active_track})")
        cons_active_track = track

    return total_head_movement, head_access_sequence, filtered_sorted_tracks, sorted_tracks


def plot_sstf(total_head_movement, head_access_sequence, filtered_sorted_tracks, sorted_tracks, seek_duration,
              active_track, screen):
    total_seek_duration = float(0)
    result = " + ".join(map(str, head_access_sequence))
    total_seek_duration = seek_duration * total_head_movement
    total_seek_duration_secs = float(total_seek_duration / 1000)

    os.system("cls")

    panel_result = Panel(
        f"""
    [bold cyan]Total Head Movement:[/bold cyan] {result} = {total_head_movement}
    [bold cyan]Total Seek Rate Calculation:[/bold cyan] {total_head_movement} * {seek_duration}
    [bold cyan]Total Seek Rate:[/bold cyan] {total_seek_duration}ms or {total_seek_duration_secs}secs
    """,
        border_style="green",
        title="[bold yellow]SSTF Disk Scheduling Results[/bold yellow]",
    )

    screen.print(panel_result)

    sorted_tracks.insert(0, active_track)
    x = sorted_tracks
    y = list(range(len(x)))

    x_estimated = filtered_sorted_tracks
    y_estimated = []
    for x_val in x_estimated:
        if x_val in x:
            # direct match, find the corresponding y
            y_estimated.append(y[x.index(x_val)])
        else:
            continue

    pyplot.plot(x, y, color="black", markerfacecolor="yellow", marker="o", markersize=5, label="Sorted Tracks")
    pyplot.plot(x_estimated, y_estimated, color="red", linestyle="--", markerfacecolor="yellow", marker="o",
                markersize=5, label="Filtered Sorted Tracks")
    pyplot.gca().invert_yaxis()
    pyplot.gca().xaxis.set_label_position('top')  # Move the label to the top
    pyplot.gca().xaxis.tick_top()
    pyplot.title("Shortest Seek Time First", size=13, weight="bold", font="monospace", color="darkred")
    pyplot.gca().spines['bottom'].set_visible(False)
    pyplot.gca().spines['right'].set_visible(False)
    pyplot.gca().spines['left'].set_visible(False)
    pyplot.legend()
    pyplot.grid()
    pyplot.show()


def goodbye(screen, seconds=5):
    os.system("cls")

    goodbye_panel = Panel(
        "[bold yellow]Goodbye![/bold yellow]\n"
        "Thank you for using the program. Exiting in...\n",
        border_style="magenta",
        title="[bold red]Farewell[/bold red]",
        expand=False,
    )
    screen.print(goodbye_panel, justify="center")

    for i in range(seconds, 0, -1):
        screen.print(f"[bold green]{i}[/bold green] seconds left...", justify="center")
        time.sleep(1)

    screen.print("\n[bold yellow]Goodbye! See you next time![/bold yellow]", justify="center")


def main():
    os.system("cls")

    custom_theme = Theme({
        "info": "dim cyan",
        "warning": "magenta",
        "error": "bold red"
    })

    screen = Console(theme=custom_theme)

    panel = Panel("[bold blue]Welcome to Shortest Seek Time First Disk Scheduling[/bold blue]",
                  border_style="bold green", width=300, subtitle="Operating Systems")

    panel_info = Panel(
        """
    [bold]Please follow the instructions below for SSTF Disk Scheduling:[/bold]

    - Enter the [bold cyan]number of tracks (num_tracks) | (100 - 350)[/bold cyan]
    - Enter the [bold cyan]previous track position (last_track) | (e.g., 225)[/bold cyan]
    - Enter the [bold cyan]current track position (active_track) | (e.g., 275)[/bold cyan]
    - Enter the [bold cyan]seek rate (seek_duration) | (e.g., 25)[/bold cyan]
    - Enter the [bold cyan]number of requested tracks (num_requested_tracks) | (10 - 25)[/bold cyan]
    - Enter the [bold cyan]desired track (desired_track) | (e.g., 150)[/bold cyan]

    """,
        border_style="cyan",
        title="[bold yellow]SSTF Disk Scheduling Instructions[/bold yellow]",
        width=300,
    )

    screen.print(panel, justify="center")
    screen.print()
    screen.print(panel_info, justify="left")
    screen.print()

    screen.print("[bold green]Enter Number of Tracks[/bold green]", end="")
    num_tracks = int(Prompt.ask(""))

    while num_tracks not in range(100, 351):
        screen.print("Error: Please enter a number between 100 and 350.", style="error")
        screen.print("[bold green]Enter Number of Tracks:[/bold green]", end="")
        num_tracks = int(Prompt.ask(""))

    screen.print("[bold green]Enter a Number for Previous Track[/bold green]", end="")
    last_track = int(Prompt.ask(""))

    screen.print("[bold green]Enter a Number for Current Track[/bold green]", end="")
    active_track = int(Prompt.ask(""))

    screen.print("[bold green]Enter a Number for Seek Duration[/bold green]", end="")
    seek_duration = int(Prompt.ask(""))

    screen.print("[bold green]Enter Number of Requested Tracks[/bold green]", end="")
    num_requested_tracks = int(Prompt.ask(""))

    while num_requested_tracks not in range(10, 26):
        screen.print("Error: Please enter a number between 10 and 25.", style="error")
        screen.print("[bold green]Enter Number of Requested Tracks[/bold green]", end="")
        num_requested_tracks = int(Prompt.ask(""))

    track_queue = []

    for x in range(1, num_requested_tracks + 1):
        while True:
            screen.print(f"[bold green]Enter Desired Requested Track [{x}][/bold green]", end="")
            desired_track = int(Prompt.ask(""))
            if desired_track < num_tracks - 1:
                track_queue.append(desired_track)
                break
            else:
                screen.print(f"Error: Input exceeds maximum allowed length of {num_tracks - 1}.", style="error")

    while active_track in track_queue:
        track_queue.remove(active_track)
    while last_track in track_queue:
        track_queue.remove(last_track)

    for x in track(range(5), description="[bold green]Calculating[/bold green]"):
        time.sleep(0.5)

    total_head_movement, head_access_sequence, filtered_sorted_tracks, sorted_tracks = find_shortest_seek(active_track,
                                                                                                          last_track,
                                                                                                          track_queue)

    plot_sstf(total_head_movement, head_access_sequence, filtered_sorted_tracks, sorted_tracks, seek_duration,
              active_track, screen)

    screen.print()

    panel_repeat = Panel(
        "[bold yellow]Do you want to input values again?[/bold yellow]\n"
        "Enter '[bold green]yes[/bold green]' to continue or '[bold red]no[/bold red]' to exit.",
        border_style="cyan",
        title="[bold magenta]Input Prompt[/bold magenta]",
        expand=False,
    )
    screen.print(panel_repeat)
    answer = Prompt.ask("[bold green]Enter here: [/bold green]")

    while True:
        try:
            if answer == "Yes" or answer == "yes":
                main()
            else:
                goodbye(screen)
                break
        except ValueError:
            screen.print(
                "Error: Invalid input! Please enter '[bold green]yes[/bold green]' or '[bold red]no[/bold red]'.",
                style="error")


# It is a conditional statement that checks if the script
# is being executed directly (not imported as a module).
if __name__ == "__main__":
    main()  # function call
