import os
import shutil

print("\nSupports:\n\n.jpg, .jpeg, .png, .gif, .pdf, .docx, .txt, .xlsx, .mp3, .wav, .mp4, .mov, .zip, .rar, .tar, .gz, .exe, .bat, .py, .sh")
folder_path=input("\n--------------\n\nFolder path? : ")

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mov"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Programs": [".exe", ".bat", ".py", ".sh"]
}

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isdir(file_path):
        continue

    _, ext = os.path.splitext(filename)

    moved = False
    for category, extensions in file_types.items():
        if ext.lower() in extensions:
            category_path = os.path.join(folder_path, category)

            if not os.path.exists(category_path):
                os.mkdir(category_path)

            shutil.move(file_path, os.path.join(category_path, filename))
            print(f"Moved {filename} to '{category}'")
            moved = True
            break

    if not moved:
        print(f"Skipped {filename} (unknown file type)")
input("Press any key to exit...")

