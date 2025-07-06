import time
import sys


def backspace_animation(message, countdown):
    for i in range(countdown, -1, -1):
        # Update the countdown number
        current_message = f"{message} [{i}]"
        sys.stdout.write("\r" + current_message)  # Overwrite the current line
        sys.stdout.flush()
        time.sleep(1)  # Wait for 1 second

        # Simulate backspace effect at the end
        if i == 0:
            for _ in range(len(current_message)):
                sys.stdout.write("\b \b")  # Backspace and erase
                sys.stdout.flush()
                time.sleep(0.05)  # Adjust speed of backspace animation


# Example usage
backspace_animation("Exiting OPT Simulator in...", 5)