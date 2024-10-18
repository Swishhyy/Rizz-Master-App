import random
import time

# List of smooth "rizz" lines
rizz_lines = [
    "Are you French? Because Eiffel for you. ❤️",
    "Do you have a name, or can I call you mine? 😏",
    "Do you believe in love at first sight, or should I walk by again? 😉",
    "Is your name Wi-Fi? Because I'm feeling a connection. 📶",
    "Can you lend me a map? I keep getting lost in your eyes. 👀",
    "If beauty were time, you'd be an eternity. ⏳",
    "Do you have a Band-Aid? I just scraped my knee falling for you. 🥰",
    "Your hand looks heavy. Can I hold it for you? ✋",
    "I was blinded by your beauty... I’m going to need your name and number for insurance purposes. 😎",
    "If you were a vegetable, you'd be a *cute-cumber*. 🥒",
]

def display_rizz():
    print("\n--- Welcome to the Rizz Master Console ---\n")
    time.sleep(1)

    while True:
        # Pick a random rizz line and display it
        line = random.choice(rizz_lines)
        print(f"💬 {line}")
        
        # Small delay before the next line
        time.sleep(random.uniform(2, 4))

        # Add a fun user input for interactivity
        cont = input("Do you want more rizz? (y/n): ").lower()
        if cont != 'y':
            print("👋 Alright, keep slaying! See you soon!")
            break

# Run the script
if __name__ == "__main__":
    display_rizz()
