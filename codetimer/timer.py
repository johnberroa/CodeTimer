"""
Timer class that can time whatever code you want.  Can run multiple timers with multiple names, and also print
intermediate times while a function is running.

@author: John Berroa
"""

import time


class Timer:
    def __init__(self, name=None):
        """
        Timer to time record times.  Only used for timing, not for using the times in a program (i.e., elapsed times are
        not currently retrievable as a variable).

        Start the timer, print it for current running time, or stop it and print it for total time.
        
        :param name: Name of the timer, optional (use if using multiple timers to know which one is being displayed)
        """
        self.name = "'{}'".format(name)
        self.reset()

    def __str__(self):
        """
        Allow the timer to be directly printed.
        """
        name = " {}".format(self.name) if self.name is not None else ""
        if self._start_time is None:
            return "Timer{} not started.".format(name)
        elif self._end_time is None:
            return "Timer{} still running: ".format(name) + self._time_representation()
        else:
            return self._time_representation()

    def start(self):
        """
        Starts the timer. Throws an error if timer is already started.
        """
        if self._start_time is not None:
            raise RuntimeError("Timer already started!")
        self._start_time = time.time()

    def stop(self):
        """
        Stops the timer.  Throws an error if timer not started.
        """
        if self._start_time is None:
            raise RuntimeError("Timer never started!")
        self._end_time = time.time()

    def reset(self):
        """
        Resets the timer start and stop values to None.
        """
        self._start_time = None
        self._end_time = None

    def _time_representation(self):
        """
        Creates a string which represents the time the timer has/is running in human readable format.
        :return: formatted string
        """
        # Get a temporary end if need be
        if self._end_time is None:
            end = time.time()
        else:
            end = self._end_time

        # Format the string
        name = " for {}".format(self.name) if self.name is not None else ""
        elapsed = end - self._start_time
        seconds = round(elapsed, 2)  # TODO: Have a self representation of this so it can be put into formatted strings
        minutes = round(elapsed / 60, 2)
        hours = round(minutes / 60, 2)
        time_string = "Time elapsed{}: {}s ({}m | {}h)".format(name, seconds, minutes, hours)

        return time_string
