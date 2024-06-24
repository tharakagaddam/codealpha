import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Define the mapping of file extensions to folder names
file_type_mapping = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.mkv', '.flv', '.avi', '.mov'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Scripts': ['.py', '.js', '.html', '.css']
}

def organize_files(directory_to_organize):
    # Create folders if they don't exist
    for folder in file_type_mapping.keys():
        folder_path = os.path.join(directory_to_organize, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to their corresponding folders
    for filename in os.listdir(directory_to_organize):
        file_path = os.path.join(directory_to_organize, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            moved = False
            for folder, extensions in file_type_mapping.items():
                if file_extension in extensions:
                    shutil.move(file_path, os.path.join(directory_to_organize, folder, filename))
                    moved = True
                    break
            if not moved:
                # Move files that don't match any specified extension to an 'Others' folder
                other_folder_path = os.path.join(directory_to_organize, 'Others')
                if not os.path.exists(other_folder_path):
                    os.makedirs(other_folder_path)
                shutil.move(file_path, os.path.join(other_folder_path, filename))

    messagebox.showinfo("Success", "Files have been organized successfully!")

def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        organize_files(directory)

# Set up the GUI
root = tk.Tk()
root.title("File Organizer")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Select a directory to organize:")
label.pack(pady=5)

browse_button = tk.Button(frame, text="Browse", command=browse_directory)
browse_button.pack(pady=5)

exit_button = tk.Button(frame, text="Exit", command=root.quit)
exit_button.pack(pady=5)

root.mainloop()


