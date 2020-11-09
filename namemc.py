import bs4
import cfscrape

class namemc:
     def __init__(self, length, lengthop, language, searches):
      self.length = length
      self.language = language
      self.searches = searches
      self.lengthop = lengthop
     def getDroptime(name):
         scraper = cfscrape.create_scraper() 
         req = scraper.get("https://namemc.com/name/" + name)
         bs = bs4.BeautifulSoup(req.content, "html.parser")
         page = bs.find(class_="card mb-3")
         box = page.find(class_="card-body py-1 position-relative")
         elements = box.find_all(class_="py-0")
         time = ""
         for element in elements:
           ign = element.find(class_="col col-sm").get_text()
           if(ign.upper().strip() == name.upper()):
             return time
           time = element.find_all("time")[0].get_text()

     def getList(self):
         names = []
         scraper = cfscrape.create_scraper() 
         req = scraper.get("https://namemc.com/minecraft-names?length_op="+self.lengthop+"&length="+self.length+"&lang="+self.language+"&searches="+self.searches)
         bs = bs4.BeautifulSoup(req.content, "html.parser")
         page = bs.find(class_="col-lg-7 order-lg-2")
         table = page.find(class_="card-body p-0")
         tablen = table.find_all('a')
         for name in tablen:
           names.append(name.get_text()) 
         return names

print(namemc.getDroptime("_team32_TR"))


         