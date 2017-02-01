#### Author: Fabien Bessez
#### Purpose: This program uses the Netflix Roulette API to 
####		  filter through their database and find films
####		  with certain actors or directors that fall into
####		  a certain rating range. 


# Example Endpoints
# title_url = "http://netflixroulette.net/api/api.php?title=Attack%20on%20titan"
# title_yr_url = "http://netflixroulette.net/api/api.php?title=The%20Boondocks&year=2005"
# director_url = "http://netflixroulette.net/api/api.php?director=Quentin%20Tarantino"
# actor_url = "http://netflixroulette.net/api/api.php?actor=Nicolas%20Cage"
base_url = "http://netflixroulette.net/api/api.php?"


"""
	Keys returned in json: 
		show_title
		release_year
		show_id
		unit
		category
		poster
		show_cast
		rating
		runtime
		mediatype
		director
"""

import urllib.request
import json


# INPUT1: role : string --> either "actor" or "director"
# INPUT2: name : string --> name of actor or director
# OUTPUT: final_url : string --> the url to query in get_json
def url_maker(role, name):
	name = name.replace(" ", "%20")
	global base_url
	final_url = base_url + role + "=" + name
	return final_url

# INPUT1: url : string --> the url to query
# OUTPUT: jload : json --> the query results in json format
def get_json(url):
	try:
		req = urllib.request.urlopen(url)
		red = req.read().decode('utf-8')
		jload = json.loads(red)
		return jload
	except:
		print("Couldn't find anything :(")
		return

# INPUT1: role : string --> either "actor" or "director"
# INPUT2: name : string --> name of actor or director
# OUTPUT: response : json --> the query results in json format
# NOTES: This is simply a compilation of the two helper functions above
def query_netflix(role, name):
	print("Querying", name, "...")
	url = url_maker(role, name)
	response = get_json(url)
	return response

# INPUT1: rating : float --> 0.0 <= rating <= 5.0 the lowest rating you wish to see
# INPUT2: response : json --> just the json response from an earlier query
# OUTPUT: nothing...
def sort_by_rating(rating, response):
	titles = []
	total_rating = 0
	for val in response:
		if float(val["rating"]) >= rating:
			titles.append(val["show_title"])
			total_rating = total_rating + float(val["rating"])
	if len(titles) > 0:
		Avg_Film_Rating = total_rating / len(titles)
		print("Titles:", titles)
		print("Avg_Film_Rating:", Avg_Film_Rating)
	else:
		print("Sorry, no films above a " + str(rating) + " rating")

# An example run through querying Nicolas Cage films above a 4.2 rating
res = query_netflix("actor", "Nicolas Cage")
sort_by_rating(4.2, res)


