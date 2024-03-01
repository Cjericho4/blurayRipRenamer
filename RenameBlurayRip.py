#!/usr/bin/python3
import os as os
import csv as csv
import sys as sys

def csv_to_dict(csv_file):
    data_dict = {}
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            episode = row['Episode']
            filename = row['Filename']
            data_dict[episode] = {'Filename': filename}
    return data_dict

def rename_files(folder, dict):
    for episode, info in dict.items():
        old_filename = os.path.join(folder, info['Filename'])
        new_filename = os.path.join(folder, f'{episode}.mkv')
        try: 
            os.rename(old_filename, new_filename)
            print(f'Renamed: {old_filename} -> {new_filename}')
        except FileNotFoundError:
            print(f'File not found: {old_filename}')

def main():
    if len(sys.argv) < 3:
        print("Command should be ./RenameBlurayRip.py <CSV_FILE_PATH> <FolderOfFiles>")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    path_to_folder = sys.argv[2]

    episode_dict = csv_to_dict(csv_file)
    rename_files(path_to_folder, episode_dict)

if __name__ == "__main__":
    main()
