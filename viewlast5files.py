import os
import glob

def get_last_5_files():
    # Set the directory path where you want to search for files
    # You can specify a specific directory or use a home directory like '~'
    directory_path = '~'

    # Use glob to find all files in the directory and sort them by their last access time
    all_files = glob.glob(os.path.join(os.path.expanduser(directory_path), '*'))
    last_5_files = sorted(all_files, key=os.path.getatime, reverse=True)[:5]

    return last_5_files

def main():
    last_5_files = get_last_5_files()

    if not last_5_files:
        print("No files found.")
    else:
        print("Last 5 files you opened:")
        for idx, file_path in enumerate(last_5_files, 1):
            print(f"{idx}. {file_path}")

if __name__ == "__main__":
    main()



# os module accesses file information and glob module finds the most recently accessed files.