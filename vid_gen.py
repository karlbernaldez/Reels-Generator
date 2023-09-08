import sys
from moviepy.editor import *
import os
import csv
import tkinter as tk
from tkinter import filedialog, scrolledtext

class RedirectText:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.insert(tk.END, string)
        self.text_widget.see(tk.END)

    def flush(self):
        pass

def process_videos():
    base_dir = dir_entry.get()
    start_date = int(date_entry.get())

    # Create a new folder named "Reels" inside the base directory
    reels_dir = os.path.join(base_dir, "Reels")
    if not os.path.exists(reels_dir):
        os.makedirs(reels_dir)

    # Read filenames from the CSV file
    csv_path = os.path.join(base_dir, "Reels_TYF.csv")
    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip header row
        filenames = [row[1] for row in csvreader]

    for day in range(start_date, 51):  # For days 1 to 50
        video_dir = os.path.join(base_dir, f"Day {day}/Video Elements/")
        audio_dir = os.path.join(base_dir, f"Day {day}/Audio Elements/")

        # Load video clips and apply effects
        clips = [VideoFileClip(os.path.join(video_dir, f"{i}.mp4")).subclip(0, 6).fx(vfx.fadeout, 1) if i == 1 else VideoFileClip(os.path.join(video_dir, f"{i}.mp4")).subclip(0, 6).fx(vfx.fadein, 1).fx(vfx.fadeout, 1) for i in range(1, 6)]

        # Get the resolution of the first video clip
        target_resolution = clips[0].size

        # Resize all video clips to match the resolution of the first video clip
        for i in range(1, len(clips)):
            clips[i] = clips[i].resize(newsize=target_resolution)

        # Load audio clips and apply effects
        bg1 = AudioFileClip(os.path.join(audio_dir, "bg.mp3")).fx(afx.audio_fadein, 1).fx(afx.volumex, 0.35)
        silent = AudioFileClip(os.path.join(audio_dir, "silent.wav"))

        # Check for vo.mp3 or vo.mp4 and load the audio accordingly
        vo_mp3_path = os.path.join(audio_dir, "vo.mp3")
        vo_mp4_path = os.path.join(audio_dir, "vo.mp4")
        if os.path.exists(vo_mp3_path):
            bg2 = AudioFileClip(vo_mp3_path).fx(afx.audio_fadein, 1).fx(afx.volumex, 2.0)
        elif os.path.exists(vo_mp4_path):
            bg2 = AudioFileClip(vo_mp4_path).fx(afx.audio_fadein, 1).fx(afx.volumex, 2.0)
        else:
            raise FileNotFoundError("Neither vo.mp3 nor vo.mp4 found.")

        bg2 = concatenate_audioclips([silent, bg2])

        # Trim audio clips to 30 seconds
        max_audio_duration = bg2.duration + 3
        bg1 = bg1.subclip(0, max_audio_duration)
        bg2 = bg2.subclip(0, max_audio_duration)

        # Concatenate video clips
        combined = concatenate_videoclips(clips)

        # Trim the video to not exceed 30 seconds
        max_duration = bg2.duration + 3
        if combined.duration > max_duration:
            combined = combined.subclip(0, max_duration)

        # Create a CompositeAudioClip with the trimmed audio clips
        combined_audio = CompositeAudioClip([bg1.set_duration(max_duration), bg2.set_duration(max_audio_duration)])

        # Set the combined audio to the video
        combined = combined.set_audio(combined_audio)

        # Write the final output video using the filename from the CSV
        output_filename = f"Day {day}_{filenames[day - 1]}.mp4"  # Updated format
        output_path = os.path.join(reels_dir, output_filename)
        combined.write_videofile(output_path)

    print("All videos processed successfully!")

root = tk.Tk()
root.title("Video Processor")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

dir_label = tk.Label(frame, text="Base Directory:")
dir_label.grid(row=0, column=0, padx=5, pady=5)
dir_entry = tk.Entry(frame, width=40)
dir_entry.grid(row=0, column=1, padx=5, pady=5)
dir_button = tk.Button(frame, text="Browse", command=lambda: dir_entry.insert(0, filedialog.askdirectory()))
dir_button.grid(row=0, column=2, padx=5, pady=5)

date_label = tk.Label(frame, text="Start Date:")
date_label.grid(row=1, column=0, padx=5, pady=5)
date_entry = tk.Entry(frame, width=10)
date_entry.grid(row=1, column=1, padx=5, pady=5)

process_button = tk.Button(frame, text="Process Videos", command=process_videos)
process_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

output_text = scrolledtext.ScrolledText(root, width=80, height=15)
output_text.pack(padx=10, pady=10)

sys.stdout = RedirectText(output_text)

root.mainloop()
