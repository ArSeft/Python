import os

directory = input("Enter the full path of the directory: ").strip()
word_to_remove = input("Enter the word to remove from filenames: ").strip()

if not os.path.isdir(directory):
    print("Error: Directory not found!")
else:
    for filename in os.listdir(directory):
        old_path = os.path.join(directory, filename)
        
        if os.path.isfile(old_path) and word_to_remove in filename:
            new_filename = filename.replace(word_to_remove, "").strip()
            new_path = os.path.join(directory, new_filename)

            os.rename(old_path, new_path)
            print(f'Renamed: {filename} -> {new_filename}')

    print("Renaming complete!")
