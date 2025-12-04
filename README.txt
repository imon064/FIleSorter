
README: CONFIGURATION & SETUP

Before running the script, you must update the file paths to match your computer's 
directory structure. Open the Python file and look for the configuration variables 
near the top:

1. Set the Monitored Folder (main_Folder):
   Change the value of 'main_Folder' to the directory path you want the script 
   to watch (usually your Downloads folder).

2. Define Sorting Rules (destination_Folder):
   This dictionary maps file prefixes to target folders.
   - Key (Left): The prefix string the script looks for (e.g., "work_").
   - Value (Right): The folder path where matching files will be moved.
   - You can add as many lines as you like.

IMPORTANT: 
Keep the 'r' before the opening quote (e.g., r"C:\...") to ensure Windows file 
paths are read correctly.

--------------------------------------------------------------------------------
EXAMPLE CONFIGURATION CODE
--------------------------------------------------------------------------------

# 1. The folder you want to watch for new files
main_Folder = r"C:\Users\YOUR_USERNAME\Downloads" 

# 2. Where files should go based on their prefix
destination_Folder = {
    "work_" : r"C:\Users\YOUR_USERNAME\Documents\Work",
    "video_": r"C:\Users\YOUR_USERNAME\Documents\Videos",
    "img_"  : r"C:\Users\YOUR_USERNAME\Pictures\Saved",
    # Add new rules here: "prefix_" : r"C:\Target\Path"
}
