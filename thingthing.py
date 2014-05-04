import urllib2

i = 1
places = ["Addison", "Algonquin" ,"Arlington Heights", "Barrington",  "Barrington Hills" ,
"Bartlett" ,"Bensenville" ,"Bloomingdale", "Buffalo Grove" ,"Carol Stream" ,"Carpentersville" ,
"Des Plaines" ,"Dundee", "East Dundee", "Elgin" , "Elk Grove Village", "Elmhurst", "Glen Ellyn" ,
"Glendale Heights", "Hanover Park" ,"Hoffman Estates", "Itasca" ,"Lombard", "Medinah" ,"Mount Prospect", 
"Oak Brook", "Oakbrook Terrace", "Palatine","Rolling Meadows","Roselle", "Schaumburg" ,"South Barrington", 
"South Elgin", "Streamwood", "Villa Park", "Wheeling", "Wood Dale"]




while i < 52:
	print "http://housestudentapps.challengepost.com/registrants"+ "?page=" + str(i)
	words = urllib2.urlopen("http://housestudentapps.challengepost.com/registrants"+ "?page=" + str(i)).read().replace(","," ")
	
	#print words
	for k in places:
		if k  in words:
			print "found one on page " + str(i)
	i = i+ 1