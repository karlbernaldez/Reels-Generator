## Video Reels Processor

### Description

The Video Reels Processor is a Python script that automates the creation of video reels from a series of short video and audio clips. The script combines video clips with fade-in and fade-out effects and pairs them with a composite audio track created from background and voice-over audios. The script operates within a simple Tkinter GUI, allowing users to specify the base directory and start date for the processing of video reels.

### Prerequisites

- Python 3.x
- MoviePy Python package
- Tkinter Python package

### Installation

1. Ensure that Python and pip (Python's package installer) are installed on your system. If not, download and install Python from the [official website](https://www.python.org/).
   
2. Install the necessary Python packages by running the following commands in your terminal or command prompt:

   ```
   pip install moviepy
   pip install tk
   ```

3. Clone or download this repository to your local machine.

### Usage

1. Prepare your base directory with the following structure:

   ```
   Base Directory
   ├─ Day 1
   │  ├─ Video Elements
   │  └─ Audio Elements
   ├─ Day 2
   │  ├─ Video Elements
   │  └─ Audio Elements
   ...
   ├─ Day 50
   │  ├─ Video Elements
   │  └─ Audio Elements
   └─ Reels_TYF.csv
   ```

2. Inside each "Day X" folder, populate "Video Elements" with five video files named from 1.mp4 to 5.mp4, and "Audio Elements" with background audio (`bg.mp3`), silent audio (`silent.wav`), and a voice-over audio file either in `.mp3` or `.mp4` format named `vo.mp3` or `vo.mp4`.

3. Populate `Reels_TYF.csv` with two columns, where the second column contains the unique filenames for each day's reel (no header row is required).

4. Run the script in a terminal or command prompt with the command:

   ```
   python script_name.py
   ```

5. In the GUI:
   
   - **Base Directory**: Specify the path to your base directory.
   - **Start Date**: Specify the day number from which to start processing (between 1 and 50, inclusive).
   
   Click "Browse" to select your base directory through a file dialog, and then click "Process Videos" to start the processing.

6. The script will create a "Reels" folder inside the base directory, where it will save the processed video reels with names based on the day number and the filenames specified in the `Reels_TYF.csv` file.

7. You will see the processing status and any messages in the scrolled text widget in the GUI.

### Note

- Ensure that all the necessary files are correctly placed in the respective folders to avoid file not found errors.
- The voice-over file can be either an `.mp3` or an `.mp4`. If neither is found, the script will raise an error.
- The script is set to process up to 50 days of reels; modify the range in the script if you want to process a different number of days.

### License

This script is for personal use and should be used responsibly and ethically. It is not endorsed for commercial use.

---

Remember to replace `script_name.py` with the actual filename of your script. Adjust the details as necessary to suit the specific requirements and structure of your project.
