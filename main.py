import flickr
import urllib, urlparse
import os
import sys


tag = []
i = 0
folder = "images"
input_tag = sys.argv[1]


tag.append(input_tag)
if not os.path.exists(os.path.join(folder, input_tag)):
	os.makedirs(os.path.join(folder, input_tag))

images_count = sys.argv[2]
print "input_tag:", input_tag, "images_count:", images_count

f = flickr.photos_search(tags = tag, tag_mode = "all", per_page = images_count)
urllist = []

for k in f:
	url = k.getURL(size = "Medium", urlType = "source")
	urllist.append(url)
	image = urllib.URLopener()
	image.retrieve(url, os.path.join(folder, input_tag.decode('utf-8'), os.path.basename(urlparse.urlparse(url).path)))
	print "downloading:", url
