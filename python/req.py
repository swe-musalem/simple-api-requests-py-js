import requests
# using requests library

# make the user choose the word
userWord = input("enter the word to search: ")

# the url with userWord as parameter
url = "https://wordsapiv1.p.rapidapi.com/words/{}/typeOf".format(userWord)


# headers are required for some Apis
headers = {
	"X-RapidAPI-Key": "62f039a6fdmsh793b811dd438a78p1647b5jsn87e8a2e142bf",
	"X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
}

# send request to the url 
response = requests.request("GET", url, headers=headers)

#the response in json format
res = response.json()


data = res['typeOf']

# looping in data and print the results
for info in data:
    print(info)

