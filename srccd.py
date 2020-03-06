import webbrowser
import time

total_breaks = 3
break_count = 0
print("This program started on " +time.ctime())
print("thank vibhuti later")
while (break_count < total_breaks ):
    time.sleep(5) #delays upto 5 second
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=BPNTC7uZYrI")
    break_count = break_count + 1
