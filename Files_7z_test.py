import subprocess
import tkinter as tk
from tkinter import filedialog
import random
import string

root = tk.Tk()
root.withdraw()

#7zip location
seven_zip = r"C:\Applications\7-Zip\7z.exe" #change the directory to where your 7zip is located

def generate_password(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))

files_to_compress = filedialog.askopenfilenames(
    title="Select files to compress", 
    filetypes=(("All files", "*.*"),))

for file in files_to_compress:
    password = generate_password(127)
    subprocess.run([seven_zip, 'a', '-t7z', '-p'+password, file + '.7z', file])
    print("File compressed successfully with password: ", password)
