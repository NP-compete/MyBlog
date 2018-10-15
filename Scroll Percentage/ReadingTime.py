import math

class CalculateTime():

	def calTime(text):
		length = len(text.split())
		time = length/200
		minutes = math.floor(time)
		seconds = (time-minutes)*60
		seconds = math.ceil(seconds) if math.ceil(seconds)-seconds < 0.5 else math.floor(seconds)
		return str(minutes) + " minutes " + str(seconds) + " seconds "
    
'''    
# ALSO MAKE ENTRIES IN

Place this file in the same directory where is views.py

** models.py --> class Post
avg_time = models.CharField(max_length = 40, default='')

** views.py --> class in which you store post in database
// import
	from .ReadingTime import calculateTime
  //add before saving post in database
    post.avg_time = CalculateTime.calTime(post.text)
'''
