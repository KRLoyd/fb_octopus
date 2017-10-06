#!/usr/bin/node

let url = 'https://itunes.apple.com/search?'

$(function (artistList) {

//let artistList = process.argv[2]

    let savedArtistDict = {'artist': 'artUrl'}
    let userDict = {}

    for (let i = 0; i < artistList; i++){
	$(function () {
	    $.ajax({
		url: url,
		type: 'GET',
		success: function (artistList[i]) {
		    if (savedArtistList.get(artistList[i])) {
			userDict[artistList[i]] = savedArtistList.get(artistList[i])
		    }
		    else {
			getArtwork(artistList[i]);
		    }
			}
	    })
	}
    }
}

$(function getArtwork (artist) {
    searchParams = 'term=' + artist.replace(' ', '+')
    
}





// let $=window.$

// let image = $(location.href("https://itunes.apple.com/us/artist/jack-johnson/id909253").querySelector('meta[property="og:image"]').getAttribute("content").substring(0, x.lastIndexOf("/") + 1) + "10000x10000-999.jpg");


// // let x = document.querySelector('meta[property="og:image"]').getAttribute("content");
// // let image = x.substring(0, x.lastIndexOf("/") + 1) + "10000x10000-999.jpg";
// // window.location = image;

// window.open(image);
