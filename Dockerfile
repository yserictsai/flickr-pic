FROM python:2.7.13-alpine

ENV ETAG cat. # use 'cat' as a keyword to search on flicker
ENV ECOUNT 5  # to download 5 pictures

COPY main.py /tmp
COPY flickr.py /tmp

WORKDIR /tmp
RUN mkdir -p /tmp/images
CMD /usr/local/bin/python ./main.py $ETAG $ECOUNT