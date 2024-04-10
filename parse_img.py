from urllib import response
import requests

image_url = 'https://media.istockphoto.com/photos/trees-forming-a-heart-picture-id537373196?k=20&m=537373196&s=612x612&w=0&h=Y6zpQNFrhLp9lusVP5xbJ8s6H9i0hOZlQwhhPxHlGXU='

response = requests.get(image_url)
print(response.text)


with open('image.jpg','wb') as f:
    f.write(response.content)
