import requests
import os
import json
 
TOKEN = "BrawlStarsAPIのトークン"

def get_proxies():
    proximo_url = os.environ.get('PROXIMO_URL')
    print(proximo_url)
    if proximo_url is None:
        return {}
    return {'http': proximo_url, 'https': proximo_url}

def GETrank(Tag):

    #本来は以下のコメントアウトされたコードよりプレイヤーデータを取得
    """URL_p = "https://api.brawlstars.com/v1/players/%23"
    headers = {
            "content-type": "application/json; charset=utf-8",
            "cache-control": "max-age=600",
            "authorization": "Bearer %s" % TOKEN
        }
    
    playertag = Tag
    endpoint = URL_p + playertag
    
    response = requests.get(endpoint, headers=headers, proxies=get_proxies())
    results = response.json()"""

    #APIが登録したIPアドレスからのみアクセス可能のため
    # 今回は事前に取得したデータを読み込み挙動を再現

    # 再現用コード
    with open('json_sample/'+ Tag +'.json', 'r') as f:
        results = json.load(f)
    # ここまで
        
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