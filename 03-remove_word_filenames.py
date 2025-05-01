import os

# Prompt user to enter the target directory and word to remove from filenames
directory = input("Enter the full path of the directory: ").strip()
word_to_remove = input("Enter the word to remove from filenames: ").strip()

# Check if the directory exists
if not os.path.isdir(directory):
    print("Error: Directory not found!")
else:
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        old_path = os.path.join(directory, filename)
        
        # Proceed if it's a file and contains the target word
        if os.path.isfile(old_path) and word_to_remove in filename:
            new_filename = filename.replace(word_to_remove, "").strip()
            new_path = os.path.join(directory, new_filename)

            # Rename the file and show the renaming operation
            os.rename(old_path, new_path)
            print(f'Renamed: {filename} -> {new_filename}')

    print("Renaming complete!")

