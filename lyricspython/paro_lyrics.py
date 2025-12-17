import time
import pygame
import sys


def play_lyrics_with_music():
    # Color setup (ANSI). Works on most Linux/macOS terminals.
    RESET = "\033[0m"
    # 256-color rainbow-ish palette, cycled per character
    RAINBOW_COLORS = [
        "\033[38;5;196m",
        "\033[38;5;202m",
        "\033[38;5;208m",
        "\033[38;5;214m",
        "\033[38;5;220m",
        "\033[38;5;190m",
        "\033[38;5;118m",
        "\033[38;5;82m",
        "\033[38;5;46m",
        "\033[38;5;51m",
        "\033[38;5;45m",
        "\033[38;5;39m",
        "\033[38;5;33m",
        "\033[38;5;27m",
        "\033[38;5;93m",
        "\033[38;5;129m",
        "\033[38;5;165m",
        "\033[38;5;201m",
    ]
    enable_color = sys.stdout.isatty()

    # 1. Initialize the Music Player
    pygame.mixer.init()

    # REPLACE 'paro.mp3' with your actual filename
    music_file = r"paro.mp3"

    try:
        pygame.mixer.music.load(music_file)
        print(f"Loaded {music_file}...")
    except pygame.error:
        print(
            f"Error: Could not find '{music_file}'. Please make sure the MP3 file is in the same folder."
        )
        return

    # 2. Define Full Lyrics and their approximate durations
    # (Text, Delay until next line starts)
    lyrics_data = [
        ("\n(Music starts...)", 7.7),  # Approximate intro time
        ("Ke ab kuch hosh nahi hai", 3.5),
        ("Tu mujhko pila degi kya", 3.3),
        ("Mein pi kar jo bhi kahunga", 3.3),
        ("Tu subha bhula degi kya", 3.3),
        ("Tu bahon mein rakhle do pal", 3.0),
        ("Phir chahe dur hata de", 3.0),
        ("Mein godh mein rakh lun agar sar", 3.0),
        ("Tu mujhko sula degi kya", 3.1),
        ("Jaati nahi teri yaadein kasam se", 3.0),
        ("Ke dil ka bharam hai tu", 3.0),
        ("Baaki nahi ab koi sharam jana", 3.0),
        ("Ek dharam hai tu", 3.3),
        ("Jo kehti thi mat piyo na", 3.0),
        ("Meri jaan zeher hai yeh", 3.2),
        ("Usey dekhta hoon koi gair chhuye", 3.0),
        ("Ab aur zeher kya piyu...", 5.0),
    ]

    # 3. Start Music
    print("🎵Playing paro music...❤️")
    pygame.mixer.music.play()

    # 4. Loop through lyrics and sync
    for line, delay in lyrics_data:
        # Print effect (typing style) with rainbow colors per character
        for i, char in enumerate(line):
            if enable_color and char != "\n":
                color = RAINBOW_COLORS[i % len(RAINBOW_COLORS)]
                sys.stdout.write(f"{color}{char}")
            else:
                sys.stdout.write(char)
            sys.stdout.flush()
            # Typing speed (faster for longer lines)
            time.sleep(0.04)

        # Reset color and add newline after the line completes
        if enable_color:
            sys.stdout.write(RESET)
        sys.stdout.write("\n")
        sys.stdout.flush()

        # Calculate how much time is left in the 'delay' bucket after typing
        typing_duration = len(line) * 0.04
        remaining_time = delay - typing_duration

        if remaining_time > 0:
            time.sleep(remaining_time)

    # Keep script running until music ends
    while pygame.mixer.music.get_busy():
        time.sleep(1)


if __name__ == "__main__":
    play_lyrics_with_music()
