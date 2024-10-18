import random
import time

# Extended list of smooth "rizz" lines
rizz_lines = [
    "Are you a magician? Because every time I look at you, everyone else disappears. ✨",
    "If you were a triangle, you'd be acute one. 🔺",
    "Do you have a sunburn, or are you always this hot? ☀️",
    "I must be a snowflake because I’ve fallen for you. ❄️",
    "Are you Australian? Because when I look at you, I feel down under. 🐨",
    "You must be tired because you've been running through my mind all day. 🏃",
    "Is your name Google? Because you’ve got everything I’m searching for. 🔍",
    "If you were a fruit, you'd be a fineapple. 🍍",
    "Are you from Tennessee? Because you're the only 10 I see. 🤠",
    "Do you have a pencil? Because I want to erase your past and write our future. ✏️",
    "Is your dad a boxer? Because you’re a knockout. 🥊",
    "If kisses were snowflakes, I'd send you a blizzard. ❄️",
    "Do you have a GPS? Because I just got lost in your smile. 😊",
    "If you were a song, you'd be the perfect melody. 🎵",
    "Are you a parking ticket? Because you’ve got FINE written all over you. 🚗",
    "You must be a bank loan, because you’ve got my interest. 💰",
    "Do you believe in fate? Because I think we just clicked. 🖱️",
    "Are you a keyboard? Because you're just my type. ⌨️",
    "Are you an angel? Because you’ve got heaven written all over you. 😇",
    "Are we at a museum? Because you truly are a work of art. 🎨",
    "Do you have a twin? Because I can’t believe someone like you is real. 👯",
    "Are you chocolate? Because you're sweet and irresistible. 🍫",
    "I must be a photographer because I can picture us together. 📸",
    "Is your last name Campbell? Because you’re *mm-mm* good. 🍲",
    "Do you have a library card? Because I’m checking you out. 📚",
    "Are you a star? Because your beauty lights up the night. 🌟",
    "Can you pinch me? You're so stunning I must be dreaming. 💭",
    "If you were a flower, you'd be a blooming miracle. 🌸",
    "Did it hurt when you fell from heaven? 🌤️",
    "Are you a charger? Because you’ve got me feeling energized. 🔋",
    "Can I follow you home? Because my parents always told me to follow my dreams. 🏡",
    "Are you my phone charger? Because without you, I’d die. 🔌",
    "Are you a campfire? Because you're hot and I want s'more. 🔥",
    "Is your heart a Wi-Fi hotspot? Because I feel a strong connection. 📡",
    "Do you believe in parallel universes? Because in every one, I’m falling for you. 🌀",
    "Are you a light bulb? Because you brighten up my day. 💡",
    "Is it okay if I walk you home? My app says we’re a perfect match. 🚶‍♂️",
    "Are you the ocean? Because I’m lost at sea. 🌊",
    "Do you like Star Wars? Because Yoda one for me. 💫",
    "Are you a baker? Because you’ve got the sweetest buns. 🥐",
    "You must be related to the sun, because you light up my world. ☀️",
    "Is your name Spotify? Because you just made my playlist better. 🎧",
    "Can I borrow your heart? Because mine's been stolen. 💖",
    "Are you a painter? Because every time I see you, you make my world more colorful. 🎨",
    "Do you believe in aliens? Because your beauty is out of this world. 👽",
    "You must be a spark, because you’ve ignited a fire in my heart. 🔥",
    "Are you cotton candy? Because you make my life so much sweeter. 🍭",
    "If looks could kill, you'd be a weapon of mass destruction. 💣",
    "Are you a weather forecast? Because you’ve got me feeling under the weather without you. ☁️",
    "Is your aura made of gold? Because you shine brighter than any treasure. 🪙",
    "Are you a gem? Because you’re truly priceless. 💎",
    "Do you like puzzles? Because I think we’re a perfect fit. 🧩",
    "Are you a spell? Because you’ve enchanted my heart. 🪄",
    "If beauty were a currency, you'd make Jeff Bezos look broke. 🤑",
    "Are you on the cover of Vogue? Because you’re a fashion icon. 👗",
    "Do you like rollercoasters? Because my heart races every time I’m around you. 🎢",
    "Are you a guitar? Because every moment with you is music to my ears. 🎸",
    "If I could rearrange the alphabet, I’d put U and I together. 🔤",
    "Are you a satellite? Because you orbit my mind all day. 🛰️",
    "Are you a dictionary? Because you give meaning to my life. 📖",
    "Are you espresso? Because you’re keeping me awake at night. ☕",
    "If you were a cloud, you'd be my silver lining. ☁️",
    "Is your soul a flame? Because you’ve set my heart ablaze. 🔥",
    "Are you a black hole? Because I can’t escape your gravitational pull. 🕳️",
    "Do you have a time machine? Because every moment with you feels timeless. ⏰",
    "Are you a superhero? Because you’ve saved my day. 🦸‍♀️",
    "Can I borrow a kiss? I promise I’ll give it back. 😘",
    "You must be part-time because you make my heart work overtime. 🕒",
    "Are you a cloud? Because you make my day feel lighter. 🌥️",
    "If love were a crime, you'd be the reason I’d serve life. 🔒",
    "Is your laugh contagious? Because I can't stop smiling. 😄",
    "Are you a volcano? Because I lava you. 🌋",
    "Do you have a compass? Because without you, I'm lost. 🧭",
    "Are you a genie? Because you’ve just granted my wish. 🧞",
    "You must be Wi-Fi because I'm feeling a solid connection. 📶",
    "Is your heart a map? Because I’m trying to find my way in. 🗺️",
    "Are you a poet? Because your beauty leaves me speechless. 📝",
    "Are you from a fairytale? Because you’re too good to be true. 🏰",
    "Are you a shooting star? Because I wished for you. 🌠",
    "Is your love a magnet? Because I’m drawn to you. 🧲",
    "Are you a battery? Because my life feels fully charged with you. 🔋",
    "Do you have a magic mirror? Because you just made my day. 🪞",
    "Is your middle name 'Sunshine'? Because you brighten every room. ☀️",
    "If you were a movie, you'd be a blockbuster hit. 🍿",
    "Are you a lighthouse? Because you’ve guided me to you. 🗼",
    "Do you believe in magic? Because you’ve cast a spell on me. ✨",
    "Are you a constellation? Because you light up my night. 🌌",
    "If your smile were a song, it would be my favorite tune. 🎶",
    "Are you a rainbow? Because you color my world. 🌈",
    "You must be a locksmith, because you've unlocked my heart. 🔑",
    "Are you a shooting star? Because I’ve never wished harder. 🌠",
    "Is your laugh the sun? Because you make every day brighter. 😄",
    "If you were a dessert, you’d be too sweet to resist. 🍰",
    "Are you a marathon? Because you’ve got my heart racing. 🏃",
]

def display_rizz():
    print("\n--- Welcome to the Ultimate Rizz Console ---\n")
    time.sleep(1)

    while True:
        line = random.choice(rizz_lines)
        print(f"💬 {line}")
        time.sleep(random.uniform(2, 4))

        cont = input("Want more rizz? (y/n): ").lower()
        if cont != 'y':
            print("👋 Stay smooth out there!")
            break

# Run the rizz generator
if __name__ == "__main__":
    display_rizz()
