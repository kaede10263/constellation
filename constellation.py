from bs4 import BeautifulSoup
import requests
import pandas as pd


def web_scrapy(date,iAstro):
    temp_list = []
    url = "http://astro.click108.com.tw/daily_%d.php?iAstro=%d&iAcDay=%s"%(int(iAstro),int(iAstro),date)
    res = requests.get(url)
    #res.content
    soup = BeautifulSoup(res.text, "lxml")
    #print(soup.text)
    #print("日期 :",date)
    print("星座 :",iAstro_name[iAstro])
    #print("幸運數字 :",soup.findAll("div", class_="LUCKY")[0].text.split()[0])
    #print("今日吉時 :",soup.findAll("div", class_="LUCKY")[1].text.split()[0])
    #print("幸運顏色 :",soup.findAll("div", class_="LUCKY")[2].text.split()[0])
    #print("開運方位 :",soup.findAll("div", class_="LUCKY")[3].text.split()[0])
    #print("幸運星座 :",soup.findAll("div", class_="LUCKY")[4].text.split()[0])
    print("-----------")
    #dict_result=pd.DataFrame({"":title})

    for i,j in enumerate(soup.findAll("div", class_="LUCKY")):
        print(j.text.split()[0])
        temp_list.append(j.text.split()[0])

    for i,j in enumerate(soup.select("div.TODAY_CONTENT > p")):    
        if (i)%2 == 0:
            print(j.text[4:-1])
            temp_list.append(j.text[4:-1])
        else:
            print(j.text)
            temp_list.append(j.text)
            print()
    return temp_list


if __name__ == "__main__":
    
    iAstro_name = {"0":"牡羊座","1":"金牛座","2":"雙子座","3":"巨蟹座",
                   "4":"獅子座","5":"處女座","6":"天秤座","7":"天蠍座",
                   "8":"射手座","9":"魔羯座","10":"水瓶座","11":"雙魚座"}

    title = ["幸運數字","今日吉時","幸運顏色","開運方位","幸運星座",
             "整體評分","整體說明","愛情評分","愛情說明","事業評分",
             "事業說明","財運評分","財運說明"]

    dict_result = {}

    date = "2020-02-18"
    #iAstro = "0"


    dict_result=pd.DataFrame({"":title})
    for i in range(0,12,1):
        temp_list = web_scrapy(date,str(i))
        dict_result[iAstro_name[str(i)]] =  temp_list    
            
    dict_result.to_csv("%s.csv"%(date),encoding="utf_8_sig",index=0)




