# Running the Program
1. In the user's IDE of choice clone this repository (or open using VS codespace)
2. Navigate to a terminal within the IDE
3. Change the directory to the project folder where the repo is saved locally
4. Install all program dependencies. This can be done using the command: `pip install -r requirements.txt` (make sure pip is installed).
5. Now run the program by typing `python main.py`. If this does not work try typing `python3 main.py`.
6. A UI will now appear asking the user to use the arrow keys to select the column to sort. With the column highlighted, press the enter key to begin sorting using `merge_sort`, `quick_sort`, and Python's native `sorted` function.
7. The time it takes the program to execute depends on the column selected to sort. Please know that for certain columns (like `year` and `gender`), `quick_sort` may take up to 5 minutes to execute depending on your machine.