import requests
from bs4 import BeautifulSoup 

#input github username

github_user = input("Enter Username: ")
url = f"https://github.com/{github_user}"

response = requests.get(url)

#after get the response next beautiful soap to manipulate html


user_info = BeautifulSoup(response.content, "html.parser")
user_image = user_info.find("img")["src"]
print(user_image)