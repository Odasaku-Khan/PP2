import tkinter as tk
from tkinter import ttk
import pygame
import os
class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Music Player")
        self.root.geometry("400x300")

        # String variable to display the current track
        self.current_track = tk.StringVar()
        self.current_track.set("No Track Playing")

        # Initialize playing and paused flags
        self.playing = False
        self.paused = False

        # Path to the music folder
        music_folder = "music"

        # List all the music files in the music folder
        self.tracks = [os.path.join(music_folder, file) for file in os.listdir(music_folder) if file.endswith(".mp3")]

        # Index of the currently playing track
        self.current_track_index = 0

        # Create GUI widgets
        self.create_widgets()

        # Setup keyboard controls
        self.setup_keyboard_controls()

    def create_widgets(self):
        # Label to display the current track
        self.track_label = ttk.Label(self.root, textvariable=self.current_track)
        self.track_label.pack(pady=15)

        # Progress bar to show the track progress
        self.progress_bar = ttk.Scale(self.root, from_=0, to=100, orient="horizontal", command=self.set_progress)
        self.progress_bar.pack(fill="x")

        # Button to play or pause the music
        self.play_button = ttk.Button(self.root, text="Play", command=self.toggle_play_pause)
        self.play_button.pack(side="left", padx=5)

        # Button to stop the music
        self.stop_button = ttk.Button(self.root, text="Stop", command=self.stop)
        self.stop_button.pack(side="left", padx=5)

        # Button to play the next track
        self.next_button = ttk.Button(self.root, text="Next", command=self.next_track)
        self.next_button.pack(side="left", padx=5)

        # Button to play the previous track
        self.prev_button = ttk.Button(self.root, text="Previous", command=self.previous_track)
        self.prev_button.pack(side="left", padx=5)

    def setup_keyboard_controls(self):
        # Bind space key to toggle play/pause
        self.root.bind("<space>", self.toggle_play_pause)

        # Bind right arrow key to play the next track
        self.root.bind("<Right>", lambda event: self.change_track(1))

        # Bind left arrow key to play the previous track
        self.root.bind("<Left>", lambda event: self.change_track(-1))

    def toggle_play_pause(self, event=None):
        # Check if there are tracks available
        if not self.tracks:
            return

        # If music is not playing, start playing
        if not self.playing:
            pygame.mixer.music.load(self.tracks[self.current_track_index])
            pygame.mixer.music.play()
            self.current_track.set(os.path.basename(self.tracks[self.current_track_index]))
            self.play_button.config(text="Pause")
            self.playing = True
            self.paused = False
        else:
            # If music is playing, pause it
            if self.paused:
                pygame.mixer.music.unpause()
                self.play_button.config(text="Pause")
            else:
                pygame.mixer.music.pause()
                self.play_button.config(text="Play")
            self.paused = not self.paused

    def stop(self, event=None):
        # Stop the music
        pygame.mixer.music.stop()
        self.play_button.config(text="Play")
        self.playing = False
        self.paused = False

    def set_progress(self, value):
        # Set the progress of the currently playing track
        length = pygame.mixer.Sound(self.tracks[self.current_track_index]).get_length()
        pygame.mixer.music.set_pos(float(value) / 100 * length)

    def change_track(self, direction):
        # Change to the next or previous track
        self.current_track_index = (self.current_track_index + direction) % len(self.tracks)
        self.current_track.set(os.path.basename(self.tracks[self.current_track_index]))
        self.stop()
        self.toggle_play_pause()
        self.progress_bar.set(0)

    def next_track(self):
        # Play the next track
        self.change_track(1)
        self.progress_bar.set(0)

    def previous_track(self):
        # Play the previous track
        self.change_track(-1)  
        self.progress_bar.set(0)   

    def run(self):
        # Initialize pygame and run the GUI
        pygame.init()
        pygame.mixer.init()
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    music_player.run()
