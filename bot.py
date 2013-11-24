import praw
import string

username = "abbreviation_bot"

passfile = open('password.txt', 'r')
password = passfile.read()[:-1]
passfile.close()

r = praw.Reddit(user_agent="bot created by /u/wtf_are_my_initials")
r.login(username, password)
sub = r.get_subreddit("all")

already_replied = []

response = "> SINC \n\nSINC stands for 'Strictly Informational, Not Confrontational' \n\nI'm a friendly reddit bot that explains new or confusing abbreviations! You can find more information about me on [github](https://github.com/wtfaremyinitials/abbreviation_bot)!" # In the future I'll probably support multiple abbreviations, but this works for now.

def reply(parent, message):
	if(parent.id in already_replied): # Don't reply to the same comment twice
		return
	if(parent.author.name == username): # Don't talk to yourself
		return
	parent.reply(post)
	already_replied.append(parent.id)

def look_for_abbreviation(comment):
	if(string.count(comment.body.lower(), " SINC") > 0): # The space before SINC is intentional to remove the possibility of SINC being found in a word
		return True;

def crawl():
	for comment in sub.get_comments():
		if(look_for_abbreviation(comment)):
			reply(comment, response)
			
while(True): # Praw keeps track of the 2 request per second limit, so there's no need for delay
	crawl()