# 5. Countdown Timer
# Use a while loop to count down from 10 to 1, then print "Blast off!".

counter = 10

while counter > 0:
    print(counter)
    counter -= 1
    if counter == 0:
        print("Blast off!")