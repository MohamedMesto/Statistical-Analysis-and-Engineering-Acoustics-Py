#@title convert the mp3 data Audio files to Wav Audio files
from pydub import AudioSegment
import os
import glob
from pathlib import Path

if not os.path.exists('audio_mp3_files_De'):
    os.mkdir('audio_mp3_files_De')
! cp  /content/drive/MyDrive/QU-DFKI-Thesis-ASR/Experimentation/ASR-Accent-Analysis-De/audio_mp3_files_De/*.* /content/audio_mp3_files_De



# Set the path to the folder containing the MP3 files
mp3_path = "/content/audio_mp3_files_De/*.mp3"

# Use glob to get a list of all MP3 files in the folder
mp3_files = glob.glob(mp3_path)

# Create an empty list to store the file names
file_names = []

# # Loop through the list of MP3 files and add the file names to the list
# for file_path in mp3_files:
#     file_name = os.path.basename(file_path)
#     file_names.append(file_name)

# Set the path to the folder where the converted WAV files will be saved
wav_path = "/content/audio_wav_files_De"

# Create the folder to store the WAV files, if it doesn't exist
if not os.path.exists(wav_path):
    os.makedirs(wav_path)

# Loop through the list of MP3 files
for mp3_file in mp3_files:
    # Load the MP3 file using pydub
    audio = AudioSegment.from_mp3(mp3_file)

    # Set the path and filename for the output WAV file
    wav_file = os.path.join(wav_path, os.path.splitext(os.path.basename(mp3_file))[0] + ".wav")

    # Export the audio to WAV format
    audio.export(wav_file, format="wav")
