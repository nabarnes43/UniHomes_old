import requests

url = "https://zillow56.p.rapidapi.com/search"

querystring = {"location":"Atlanta, ga","status":"forRent","isApartment":"true","isCondo":"true","doz":"any","onlyWithPhotos":"true"}

headers = {
	"X-RapidAPI-Key": "2e617df064msh2be268d22e037abp1d77ddjsn18a98458acca",
	"X-RapidAPI-Host": "zillow56.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

