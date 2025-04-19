import os
import shutil
import mimetypes

print("\nSupports the following file types:\n")
print("Images   : jpg, jpeg, png, gif")
print("Documents: pdf, docx, txt, xlsx")
print("Music    : mp3, wav")
print("Videos   : mp4, mov")
print("Archives : zip, rar, tar, gz")
print("Programs : exe, bat, py, sh")

folder_path = input("\n--------------\n\nFolder path? : ")

mime_categories = {
    "Images": ["image"],
    "Documents": [
        "application/pdf", "text",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    ],
    "Music": ["audio"],
    "Videos": ["video"],
    "Archives": [
        "application/zip", "application/x-rar-compressed",
        "application/x-tar", "application/gzip"
    ],
    "Programs": ["application/x-msdownload", "text/x-python", "application/x-sh", "application/x-bat"]
}

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isdir(file_path):
        continue

    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is None:
        print(f"Skipped {filename} (unknown MIME type)")
        continue

    moved = False
    for category, types in mime_categories.items():
        if any(mime_type.startswith(t) or mime_type == t for t in types):
            category_path = os.path.join(folder_path, category)

            if not os.path.exists(category_path):
                os.mkdir(category_path)

            shutil.move(file_path, os.path.join(category_path, filename))
            print(f"Moved {filename} to '{category}'")
            moved = True
            break

    if not moved:
        print(f"Skipped {filename} (unrecognized MIME type: {mime_type})")

input("Press any key to exit...")
