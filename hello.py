import requests

url = "https://google-jobs.p.rapidapi.com/"

querystring = {"keyword":"Python developer","location":"Mumbai","offset":"0"}

headers = {
	"X-RapidAPI-Key": "069f5deae7msh39c8af5b39ac14cp1b5a78jsn98ef71307888",
	"X-RapidAPI-Host": "google-jobs.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)