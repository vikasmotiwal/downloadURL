

## Function reads text file line by line and downloads the url.
def downloadURL(file):
    import urllib.request
    import os
    with open(file) as input:
        for line in input:
            if not line == '\n': ## Ignores the empty lines
                try:
                    urllib.request.urlretrieve(line.rstrip('\n'), os.path.join(os.getcwd(), line.rstrip('\n').split('/')[-1])) ## Download URLs with same filename in current directory
                except: ## catch exceptions for invalid URLs
                    print("Oops! "+ line.rstrip('\n')+" is not a valid URL.")

## Sample script which asks you select the file containing URLs
## file is then passed through the downloadURL function
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
## Select a file through file dialog and if it's valid, call the function
inputfile = filedialog.askopenfilename()
if not inputfile == '':
    downloadURL(inputfile)



