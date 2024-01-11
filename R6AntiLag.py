import subprocess
import time

def run_game_with_url_and_bat(game_url, bat_file_path):
    # Launch the game using the URL
    game_process = subprocess.Popen(["start", game_url], shell=True)

    # Wait for some time to allow the game to start
    time.sleep(10)

    # Run the bat file
    bat_process = subprocess.Popen([bat_file_path])

    # Wait for the game and bat file processes to finish
    game_process.wait()
    bat_process.wait()


if __name__ == "__main__":
    game_url = "uplay://launch/635/0"
    bat_file_path = "C:/Users/Vantsa/Desktop/r6.bat"

    run_game_with_url_and_bat(game_url, bat_file_path)
