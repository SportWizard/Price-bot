import requests
from bs4 import BeautifulSoup
from url_website import *

got_original_cost = False
current_cost = 0

def price():
  cost = 0
  website = read_website()

  if website == "newegg":
    cost = newegg()
  elif website == "ihlcanada":
    cost = ihl()

  return cost

def return_price():
  return "$" + str(price())

def original_price_check():
  global got_original_cost
  global current_cost
  
  if got_original_cost == False:
    current_cost = price()
    got_original_cost = True

  return current_cost

def price_change():
  difference = None
  website = read_website()

  if website == "newegg":
    difference = newegg_new()
  elif website == "ihlcanada":
    difference = ihl_new()

  return difference

def newegg():
  result = requests.get(read_url())
  doc = BeautifulSoup(result.text, "html.parser")
  
  prices = doc.find_all(text = "$")
  parent = prices[0].parent
  strong = parent.find("strong")
  cost = int(strong.string)
  
  return cost

def newegg_new():
  price_check = original_price_check()

  if price_check != None:
    current_cost = price_check

  result = requests.get(read_url())
  doc = BeautifulSoup(result.text, "html.parser")
  
  prices = doc.find_all(text = "$")
  parent = prices[0].parent
  strong = parent.find("strong")
  new_cost = int(strong.string)

  if new_cost != current_cost:
    got_original_cost = False
    
    current_cost = "$" + str(current_cost)
    new_cost = "$" + str(new_cost)
    
    difference = [current_cost, new_cost]
    return difference

def ihl():
  result = requests.get(read_url())
  doc = BeautifulSoup(result.text, "html.parser")

  span = doc.find("span", class_ = "lbl-price")
  cost = span.text
  if "$" in cost:
    cost = round(float(cost[1:]))
  else:
    cost = round(float(cost.text))

  return cost

def ihl_new():
  price_check = original_price_check()

  if price_check != None:
    current_cost = price_check

  result = requests.get(read_url())
  doc = BeautifulSoup(result.text, "html.parser")

  span = doc.find("span", class_ = "lbl-price")
  new_cost = span.text
  if "$" in new_cost:
    new_cost = round(float(new_cost[1:]))
  else:
    new_cost = round(float(new_cost.text))

  if new_cost != current_cost:
    got_original_cost = False
    
    current_cost = "$" + str(current_cost)
    new_cost = "$" + str(new_cost)
    
    difference = [current_cost, new_cost]
    return difference
