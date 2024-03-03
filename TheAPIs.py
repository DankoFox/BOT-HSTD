import requests
import json


def dark():
	url = 'https://v2.jokeapi.dev/joke/Dark'
	reponse = requests.get(url)
	json_data = json.loads(reponse.text)
	joke_type = json_data["type"]
	if joke_type == 'single':
		dajoke = json_data["joke"]
		return dajoke
	else:
		setup = json_data["setup"]
		delivery = json_data["delivery"]
		dajoke = setup + f'\n\n||{delivery}||'
		return dajoke


def pune():
	url = 'https://v2.jokeapi.dev/joke/Pun'
	reponse = requests.get(url)
	json_data = json.loads(reponse.text)
	joke_type = json_data["type"]
	if joke_type == 'single':
		dajoke = json_data["joke"]
		return dajoke
	else:
		setup = json_data["setup"]
		delivery = json_data["delivery"]
		dajoke = setup + f'\n\n||{delivery}||'
		return dajoke

def weatha():
  url = 'http://api.openweathermap.org/data/2.5/weather?id=1566083&appid=25b1db1009761e5a18540bcf99798633&units=metric'
  response = requests.get(url)
  json_data = json.loads(response.text)
  thoitiet = f'Area : {json_data["name"]} \n Weather : {json_data["weather"][0]["main"]} \n Detail : {json_data["weather"][0]["description"]} \n Temp : {json_data["main"]["temp"]} °C \n RealFeel : {json_data["main"]["feels_like"]} °C'
  return thoitiet



def synon(a):
  url = f'https://www.abbreviations.com/services/v2/syno.php?uid=9263&tokenid=SPfAGvY6W0sXInLU&word={a}&format=json'
  response = requests.get(url)
  json_data = json.loads(response.text)
  try:
    return json_data['result'][0]['synonyms']
  except:
    return json_data['result']['synonyms']


def daoly():
	tutuongdaoli = requests.get("https://zenquotes.io/api/random")
	json_data = json.loads(tutuongdaoli.text)
	quote = json_data[0]['q'] + " - " + json_data[0]['a']
	return (quote)


def fact():
	fact = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
	json_data = json.loads(fact.text)
	useless = json_data['text']
	return (useless)


def kaynewest():
	fact = requests.get("https://api.kanye.rest")
	json_data = json.loads(fact.text)
	useless = json_data['quote']
	return (useless)


def encourage():
	happy = requests.get("https://www.affirmations.dev")
	json_data = json.loads(happy.text)
	happier = json_data['affirmation']
	return (happier)