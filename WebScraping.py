import requests
from bs4 import BeautifulSoup


def tudien(word):
  headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
  url = requests.get(f'https://www.oxfordlearnersdictionaries.com/definition/english/{word}', headers=headers)
  soup = BeautifulSoup(url.text, 'html.parser')
  #operation

  ##POS
  POS_unscraped = soup.find_all('span', attrs={'class':'pos','hclass':'pos','htag':'span'})
  result = POS_unscraped[0]
  POS = result.contents[0].capitalize()

  ##DEF
  DEF_unscraped = soup.find_all('span', attrs={'class':'def','hclass':'def','htag':'span'})
  DEF = DEF_unscraped[0].getText()

  ##EX
  EX_unscraped = soup.find_all('span', attrs={'class':'x'})
  EX = EX_unscraped[0].getText()

  daura = f"DEF : {DEF}\n\npartOfSpeech : {POS}\n\nE.g : {EX}\n\n\n[https://www.oxfordlearnersdictionaries.com] "

  return (daura)

def idiom():
  headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
  url = requests.get('https://fungenerators.com/random/idiom', headers=headers)
  soup = BeautifulSoup(url.text, 'html.parser')
  idm_un = soup.find('h2', attrs={'class':'wow fadeInUp animated'})
  return(idm_un.getText())