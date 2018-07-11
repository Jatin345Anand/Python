import urllib.request

# url = "https://www.sideshowtoy.com/assets/products/400310-iron-man-mark-iii/lg/marvel-iron-man-mark-3-life-size-figure-400310-03.jpg"
# filename = "img_1.jpg"

url = "https://downpwnew.com/11985/01%20Jiyo%20Re%20Bahubali%20-%20Bahubali%202%20-%20190Kbps.mp3"
filename = "music_1.mp3"

urllib.request.urlretrieve(url, filename)
print("File Downloaded successfully...")