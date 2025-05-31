# 4. students_average.py
# - Given a file students.txt:
#   - Ada,80
#   - Chidi,60
#   - Grace,75
# - Read file, calculate average score, print highest and lowest

import os

# Define students_average() function
def students_average():
    filename = "students.txt"
    total_score = 0
    highest = 0
    lowest = 0
    counter = 0
    try:
        with open("students.txt", "r") as file:
            for line in file.readlines():
                counter += 1
                name, score = line.strip().split(",")
                score = int(score)
                if score > highest:
                    highest = score
                    lowest = score
                if score < lowest and score > 0:
                    lowest = score
                total_score += int(score)
    except FileNotFoundError:
        print(f"{filename} does not exist in this path")
    
    if counter > 0:
        print(f"Average score: {total_score / counter}")
        print(f"Highest and Lowest are {highest} and {lowest} respectively")

# Define the main() function
def main():
    print("This program calculate the students average score")
    students_average()

if __name__ == "__main__":
    main()
