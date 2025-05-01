import os
import shutil
import mimetypes

# Display supported file types categorized by content
print("\nSupports the following file types:\n")
print("Images   : jpg, jpeg, png, gif")
print("Documents: pdf, docx, txt, xlsx")
print("Music    : mp3, wav")
print("Videos   : mp4, mov")
print("Archives : zip, rar, tar, gz")
print("Programs : exe, bat, py, sh")

# Prompt the user to input the path of the folder to organize
folder_path = input("\n--------------\n\nFolder path? : ")

# Define categories of MIME types to classify files into folders
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
    "Programs": [
        "application/x-msdownload", "text/x-python",
        "application/x-sh", "application/x-bat"
    ]
}

# Iterate over every item in the specified folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    # Guess the MIME type of the file based on its extension
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is None:
        print(f"Skipped {filename} (unknown MIME type)")
        continue

    moved = False

    # Match the file's MIME type to one of the categories
    for category, types in mime_categories.items():
        if any(mime_type.startswith(t) or mime_type == t for t in types):
            category_path = os.path.join(folder_path, category)

            # Create the category folder if it doesn't exist
            if not os.path.exists(category_path):
                os.mkdir(category_path)

            # Move the file into the corresponding category folder
            shutil.move(file_path, os.path.join(category_path, filename))
            print(f"Moved {filename} to '{category}'")
            moved = True
            break

    # Report if the file could not be categorized
    if not moved:
        print(f"Skipped {filename} (unrecognized MIME type: {mime_type})")

# Pause to let the user view results before script exits
input("Press any key to exit...")
