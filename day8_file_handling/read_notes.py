# 3. read_notes.py
# - Read and print all notes from notes.txt

# Define read_notes() function
def read_notes():
    with open("notes.txt", "r") as file:
       note_list = file.readline() # returns one line in notes.txt as string
       note = file.readline() # returns all each line in notes.txt as a member of a list
    #    note = file.read() # returns the whole content as string
       print(note_list) 
       print(note)

# Define the main() function
def main():
    print("This program reads from file and prints on terminal\n")
    read_notes()

if __name__ == "__main__":
    main()