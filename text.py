import os
file_path = 'Voice-Biometrics\\data\\history\\sample-2.webm'
if os.path.exists(file_path):
    print("File exists")
else:
    print("File does not exist")
