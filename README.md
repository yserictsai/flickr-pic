# flickr-pic

This Repo is a pratice from a docker tutorial demo, use a open resource code "flickr.py" to download picture from Flickr.

Docker file build

`$ docker build . -t flickr-pic`

Docker run

`$ docker run --rm -e ETAG=model -e ECOUNT=10 -v $PWD/images:/tmp/images flickr-pic`
