import randomimport urllib.requestdef download_image(url):	# Use random to assign random names to the downloaded images for storage.	name = random.randrange(1, 100)	# Add the extension '.jpg' to the images' names.	file_name = str(name) + '.jpg'	"""	Use request to connect to the internet & download the image given the url. 	The 'file_name' defines where the image will be stored.	"""	urllib.request.urlretrieve(url, file_name)# Pass in the value of the url when calling the function.download_image('')