# delete Un Empty Folder

import shutil

shutil.rmtree('/content/audio_mp3_files_De', ignore_errors=True)
shutil.rmtree('/content/audio_wav_files_De', ignore_errors=True)

# It will delte the folders audio_wav_files_De and audio_mp3_files_De with all contents
