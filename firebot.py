from facepy import GraphAPI
import json
import web

graph = GraphAPI("")

feed = graph.get('373796221942/feed')

mentionsLog = open("mentionslog.txt", 'w')

#graph.get is divided into a few things
#	["data"] and ["paging"]
#	["data"] is a list with ["data"][0] being a dict the first post
#		each post has keys ['to', 'comments', 'is_hidden', 'privacy', 'type', 'link', 'is_expired', 'updated_time', 'likes', 'picture', 'from', 'object_id', 'name', 'id', 'icon', 'status_type', 'message', 'created_time', 'actions']
#		each comment is a dict with keys ['data'] and ['paging'],
#		like with posts, ['data'] is a lsit of comments with 0 being the first comment
#
#	["paging"] is  dict with keys 'previous' and 'next'
#
#
#
#

#feed["data"][0]['message'] #post message
#feed["data"][0]['comments'] #comments on a post
#feed["data"][0]['comments'][0]['message'] #message from first comment

#save time of last read post
lastPostTime = feed["data"][0]['comments'][len(feed["data"][0]['comments']) - 1]['created_time']

for posts in feed["data"]:
	if "fireball" in posts['message']:
		#save post with poster, add to mentions count
		mentionsLog.write(json.dumps(posts, indent=4))
	for comments in posts['comments']
		if "fireball" in comments['message']:
			#save post with poster, add to mentions count
			mentionsLog.write(json.dumps(comments, indent=4))

mentionsLog.close()
