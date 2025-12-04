import os #operating system
import time # get seconds 
import shutil #shell utilities 
import logging
from watchdog.observers import Observer #tracks folders
from watchdog.events import FileSystemEventHandler 

main_Folder = r"C:\Users\rafae\Downloads"

destination_Folder = {
    "algo_" : r"C:\Users\rafae\Documents\Kuliah\algoprog",
    "pdm_" : r"C:\Users\rafae\Documents\Kuliah\PDM",
    "cb_" : r"C:\Users\rafae\Documents\Kuliah\Pancasila",
    "linear_" : r"C:\Users\rafae\Documents\Kuliah\Linear",
    "bi_" : r"C:\Users\rafae\Documents\Kuliah\Bindo",
    "bastat_" : r"C:\Users\rafae\Documents\Kuliah\Bastat",
    "video_" : r"C:\Users\rafae\Documents\Video editing",
    "game_" : r"C:\Game",
    "porto_" : r"C:\Users\rafae\Documents\Kuliah\portofolio"
}

logging.basicConfig(filename='sorting_logs.txt',
                    level= logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

class SorterHandler(FileSystemEventHandler):

    def on_modified(self, event):#watchdog get calls automatically when a file in a forldeer is modified
        self.sort_files()
    def sort_files(self):
        for filename in os.listdir(main_Folder):
            #! listdir retrieve a list of all entries within a path
            source_path = os.path.join(main_Folder, filename) #os.path.join help correcting the file address on every os

            if os.path.isdir(source_path): #ensuring folders arent being moved
                continue

            for prefix, destination_folder in destination_Folder.items():
                if filename.lower().startswith(prefix): #filename.lower to makes checking easier
                    
                    if not os.path.exists(destination_folder):
                        os.makedirs(destination_folder) #make folder if the current folder doesnt exist
                    
                    destination_path = os.path.join(destination_folder, filename)
                    
                    if os.path.exists(destination_path):
                        base, extension = os.path.splitext(filename)
                        counter = 1
                        while os.path.exists(destination_path):
                            new_name = f"{base}_{counter}{extension}"
                            destination_path = os.path.join(destination_folder, new_name)
                            counter += 1

                    try:
                        time.sleep(1) 
                        shutil.move(source_path, destination_path)
                        log_message = f"Moved: {filename} -> {destination_folder}"
                        print(log_message)
                        logging.info(log_message)
                    except Exception as e:
                        error_msg = f"Error moving {filename}: {e}"
                        print(error_msg)
                        logging.error(error_msg)
                    
                    break
if __name__ == "__main__":
    logging.info("--- Sorter Service Started ---")
    event_handler = SorterHandler()
    observer = Observer()
    observer.schedule(event_handler, main_Folder, recursive=False)
    observer.start()

    print(f"Monitoring {main_Folder} for file prefixes...")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()