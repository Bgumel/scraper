import bs4 as bs, urllib.request as url
from time import sleep

link = "https://www.wattpad.com/373550833-bar-raina-allura-karfe-ce-2016-3"
# creating to main file
novel = open("novel.txt", "w")
novel.write("Starting file")
novel.close()



def getNumberOfEpisode():
    headers={}
    headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0"
    link = "https://www.wattpad.com/373550833-bar-raina-allura-karfe-ce-2016-1"
    req = url.Request(link, headers=headers)
    resp = url.urlopen(req)


    copyFile = open("tableOfContent.txt", "w")
    copyFile.write(str(resp.read()))
    copyFile.close()
    copyFile = open("tableOfContent.txt")
    soup = bs.BeautifulSoup(copyFile.read(), "html.parser")
    ul = soup.find("ul", {"class": "table-of-contents"})
    count = 0
    for li in ul.find_all("li"):
        count += 1
    return count


for count in range(1,getNumberOfEpisode() + 1):


    try:
        sleep(3)
        headers={}
        headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0"
        #link = link+ str(count)
        req = url.Request(link, headers=headers)
        resp = url.urlopen(req)
        data = resp.read()
        episodeName = str("episode" + str(count) + ".txt")
        episodeFile = open("bsFile.txt", "w")
        
        
        episodeFile.write(str(data))
        episodeFile.close()
        print("connection and saving file succeed :", count)
    except Exception as e:
        print("Something happen", str(e))





    # using bs
    try:
        sleep(3)
        episodeFile = open("bsFile.txt")
        episode = bs.BeautifulSoup(episodeFile.read(), "html.parser")
        element = episode.select("#sp373550833-pg1")
        rawEpisode = str(element[0].text.strip())
        content = rawEpisode
        print(str("scrapped succeed:" + str(count)), rawEpisode)

        # write on main file
        file = open("novel.txt","a")
        title = "episode" + str(count)
        file.write(str(title))
        file.write(str(content))
        file.close()
    except Exception as e:
        print("Error in scrapping ",e)





