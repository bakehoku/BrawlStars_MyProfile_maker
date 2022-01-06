import requests
 
TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImFiMGM0ZmQxLTBmMjctNDdmOC05YWY5LWFhNmZlYzllYjU5MyIsImlhdCI6MTYwOTQxNDgxNSwic3ViIjoiZGV2ZWxvcGVyLzcxYTRhZDAzLTAxZTYtZjJhOC0yZTM1LTEyODlhMmQ3OWM3NCIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTI1LjE5OC4xNzguMzUiXSwidHlwZSI6ImNsaWVudCJ9XX0.MOmHX6krZyeh197bOxhX1D2Abr0J_UPrf91zwo1Q6U4BQHVcAPbn1BpOQCrpMiAFIECYGHRToQ2anAvBYaI1ww"

def GETrank(Tag):
    URL_p = "https://api.brawlstars.com/v1/players/%23"
    headers = {
            "content-type": "application/json; charset=utf-8",
            "cache-control": "max-age=600",
            "authorization": "Bearer %s" % TOKEN
        }
    
    playertag = Tag
    endpoint = URL_p + playertag
    
    response = requests.get(endpoint, headers=headers)
    results = response.json()
        
    rank_data = []
    brawler_num = len(results["brawlers"])
    for i in range(brawler_num):
        tmp = []
        tmp.append(results["brawlers"][i]["name"])
        tmp.append(results["brawlers"][i]["rank"])
        tmp.append(results["brawlers"][i]["highestTrophies"])
        rank_data.append(tmp)
    rank_data_S = sorted(rank_data, reverse=True, key=lambda x: x[2])
    
    tmp = []
    tmp.append(results["name"])
    tmp.append(results["icon"]["id"])
    tmp.append(results["expLevel"])
    tmp.append(results["trophies"])
    tmp.append(results["highestTrophies"])
    tmp.append(results["3vs3Victories"])
    tmp.append(results["soloVictories"])
    tmp.append(results["duoVictories"])
    try:
        tmp.append(results["club"]["name"])
    except:
        tmp.append("クラブ未所属")
    Player_data = tmp
    """print(Player_data[1]%100)
    for i in range(brawler_num):
        if Player_data[1]%100 == results["brawlers"][i]["id"]:
            Player_data[1] = results["brawlers"][i]["name"]
            print(results["brawlers"][i]["name"])
            break"""

    return rank_data_S, brawler_num, Player_data

"""P = str(input("タグ：#"))
_,_,A = GETrank(P)
print(A)"""