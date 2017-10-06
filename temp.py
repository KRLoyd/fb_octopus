#!/usr/bin/python3
"""

"""
# import itunes
import json
import requests

# Search for band Jack Johnson
# artist = itunes.search_artist('Jack Johnson')[0]
# for album in artist.get_albums():
#     print(album)

#search_params = 'term=jack+johnson&entity=musicArtist'
search_params = 'term=jack+johnson'

url='https://itunes.apple.com/search?' + search_params
originalResponse = requests.get(url)
json=originalResponse.json().get("results")
#print(json)

artworkUrl = json[0].get("artworkUrl30")
print(artworkUrl)
#
# artistFullUrl =
# http://is1.mzstatic.com/image/thumb/Music2/v4/a2/66/32/a2663205-663c-8301-eec7-57937c2d0878/source/30x30bb.jpg
#
artworkUrlList = artworkUrl.split('/')
print(artworkUrlList)
imgSize = artworkUrlList[-1]
print(imgSize)
imgSize = imgSize.replace('3', '10')
print(imgSize)
artworkUrl = '/'.join(artworkUrlList[:-1]) + '/' + imgSize
print(artworkUrl)
