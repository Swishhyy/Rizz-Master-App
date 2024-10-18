import json
import random
import time
import os

CONFIG_FILE = "config.json"
LEADERBOARD_FILE = "index.md"  # To be served on GitHub Pages

def load_config():
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("⚠️ Error: config.json not found or invalid. Creating a new one.")
        return {"RizzLines": [], "UserStats": {}}

def save_config(data):
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("📁 Data saved successfully.")

def generate_leaderboard(user_stats):
    sorted_stats = sorted(user_stats.items(), key=lambda x: x[1]["RizzRequests"], reverse=True)

    # Write leaderboard to index.md for GitHub Pages
    with open(LEADERBOARD_FILE, 'w', encoding='utf-8') as f:
        f.write("# 🏆 Rizz Master Leaderboard\n\n")
        f.write("| Rank | User | Rizz Requests |\n")
        f.write("|------|------|---------------|\n")

        for rank, (user, stats) in enumerate(sorted_stats, start=1):
            f.write(f"| {rank} | {user} | {stats['RizzRequests']} |\n")

    print("📊 Leaderboard updated successfully.")

def get_user_info():
    print("\n--- Welcome to the Ultimate Rizz Console ---\n")
    name = input("What's your name? ").strip()

    try:
        age = int(input(f"Nice to meet you, {name}! How old are you? "))
    except ValueError:
        print("Please enter a valid age.")
        return get_user_info()

    if age < 18:
        years_left = 18 - age
        print(f"Sorry, {name}, you cannot be rizzed for {years_left} more year(s). 👶")
        return None

    return name

def display_rizz(name, config):
    rizz_lines = config.get("RizzLines", [])
    user_stats = config.setdefault("UserStats", {})

    if not rizz_lines:
        print("No rizz lines available. Please check your config.json.")
        return

    if name not in user_stats:
        user_stats[name] = {"RizzRequests": 0}
    user_stats[name]["RizzRequests"] += 1

    while True:
        line = random.choice(rizz_lines)
        print(f"💬 {line}")
        time.sleep(random.uniform(1, 2))

        cont = input("Want more rizz? (y/n): ").lower()
        if cont != 'y':
            print(f"👋 Stay smooth, {name}! You asked for rizz {user_stats[name]['RizzRequests']} time(s).")
            break

    save_config(config)
    generate_leaderboard(user_stats)

if __name__ == "__main__":
    config = load_config()
    user_name = get_user_info()

    if user_name:
        display_rizz(user_name, config)
