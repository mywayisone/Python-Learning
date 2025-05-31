# 2. append_notes.py
# - Ask user to type a note
# - Append the note to a file called notes.txt
# - Add timestamp using datetime module (optional)
import datetime

# Define append_notes() function
def append_notes(note: str):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("notes.txt", "a") as file:
        file.writelines(f"{timestamp}: {note}\n")

# Define main() function
def main():
    short_intro = input("Enter a short introduction about yourself: ")
    with open("notes.txt", "w") as file:
        file.writelines(f"{short_intro}\n")
    
    note = input("Enter your the note you want to save: ")
    append_notes(note)

if __name__ == "__main__":
    main()