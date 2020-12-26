import praw
import time
import schedule
import urllib.request
import subprocess
import random

path_list = []
# gets the images from r/CityPorn
def get_images(amount, time):
    # authenticates app
    reddit = praw.Reddit(client_id='Client id for your reddit app', client_secret='secret id', user_agent='name of app')
    posts = []
    hot_posts = reddit.subreddit('CityPorn').top(limit=amount, time_filter=str(time)) 
    for post in hot_posts:
        posts.append(post.url)
    # creates jpg file for image
    for i in range(amount):
        name = "file{}.jpg".format(str(i))
        resource = urllib.request.urlopen(posts[i])
        output = open(str(name),"wb")
        output.write(resource.read())
        output.close()
        path = 'Path/to/current/project/folader/' + str(name)
        path_list.append(path)

get_images('How Many Images you want', 'when you want images from, 'today', this 'week', this month, etc...')

# gets random image's path
def get_random():
    global x
    x = random.randrange(0, len(path_list))
    global y
    y = path_list[x]

get_random()
# Scheduler runs get_random every x seconds
schedule.every(x).seconds.do(get_random)

# Script to set image as wallpaper
tell_script = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""
# sets background to image
def set_background(filename):
    subprocess.Popen(tell_script%filename, shell=True)

# runs set_background every x amount of minutes
schedule.every(x).minutes.do(set_background, y)

while True:
    schedule.run_pending()
    time.sleep(1)
