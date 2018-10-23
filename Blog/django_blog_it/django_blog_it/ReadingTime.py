import math

class CalculateTime():
    def CalTime(text):
        length = len(text.split())
        time = length/200
        minutes = math.floor(time)
        seconds = (time - minutes)*60
        seconds = math.ceil(seconds) if math.ceil(seconds) - seconds < 0.5 else math.floor(seconds)
        if minutes < 1:
            return "less than 1 minute"
        elif seconds < 30:
            return "about " + str(minutes) + " min"
        else:
            return "about " + str(minutes + 1) + " min"
