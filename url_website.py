def update_url(url):
  file = open("url.txt", "w")
  file.write(url)
  file.close()

  https = url.find("https://www.") + 12
  dot = url.find(".", 12)

  website = url[https:dot]

  file = open("url.txt", "a")
  file.write("\n" + website)
  file.close()

def read_url():
  file = open("url.txt", "r")
  url = file.readlines()
  file.close()

  return url[0]

def read_website():
  file = open("url.txt", "r")
  website = file.readlines()
  file.close()

  return website[1]