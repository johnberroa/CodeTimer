# Code Timer
This lightweight timer can time any section of code desired, and makes converting run times to minutes/hours a lot easier than having to fiddle with your ```time.time() - start_time``` output.

## Usage
Printing the timer while running or when stopped will return the current run time in seconds, minutes, and hours.
```
timer = Timer("Repeating Calculation")
timer.start()
for i in range(2):
    function.apply()
    print(timer)
timer.stop()
print(timer)
```
Output will be:
```
Timer 'Repeating Calculation' still running: Time elapsed 'Repeating Calculation': 6s (.1m | 0h)
Timer 'Repeating Calculation' still running: Time elapsed 'Repeating Calculation': 12s (.2m | 0h)
Time elapsed 'Repeating Calculation': 7s (.1m | 0h)
```


