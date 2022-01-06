import cv2 as cv
import numpy as np
from PIL import Image, ImageFont, ImageDraw, Image
import player_data_API
import datetime

class CvPutJaText:
    def __init__(self):
        pass

    @classmethod
    def puttext(cls, cv_image, text, point, font_path, font_size, color=(0,0,0)):
        font = ImageFont.truetype(font_path, font_size)

        cv_rgb_image = cv.cvtColor(cv_image, cv.COLOR_BGR2RGB)
        pil_image = Image.fromarray(cv_rgb_image)

        draw = ImageDraw.Draw(pil_image)
        draw.text(point, text, fill=color, font=font)

        cv_rgb_result_image = np.asarray(pil_image)
        cv_bgr_result_image = cv.cvtColor(cv_rgb_result_image, cv.COLOR_RGB2BGR)

        return cv_bgr_result_image

class CvOverlayImage(object):
    """
    [summary]
      OpenCV形式の画像に指定画像を重ねる
    """

    def __init__(self):
        pass

    @classmethod
    def overlay(
            cls,
            cv_background_image,
            cv_overlay_image,
            point,
    ):
        overlay_height, overlay_width = cv_overlay_image.shape[:2]

        # OpenCV形式の画像をPIL形式に変換(α値含む)
        # 背景画像
        cv_rgb_bg_image = cv.cvtColor(cv_background_image, cv.COLOR_BGR2RGB)
        pil_rgb_bg_image = Image.fromarray(cv_rgb_bg_image)
        pil_rgba_bg_image = pil_rgb_bg_image.convert('RGBA')
        # オーバーレイ画像
        cv_rgb_ol_image = cv.cvtColor(cv_overlay_image, cv.COLOR_BGRA2RGBA)
        pil_rgb_ol_image = Image.fromarray(cv_rgb_ol_image)
        pil_rgba_ol_image = pil_rgb_ol_image.convert('RGBA')

        # composite()は同サイズ画像同士が必須のため、合成用画像を用意
        pil_rgba_bg_temp = Image.new('RGBA', pil_rgba_bg_image.size,
                                     (255, 255, 255, 0))
        # 座標を指定し重ね合わせる
        pil_rgba_bg_temp.paste(pil_rgba_ol_image, point, pil_rgba_ol_image)
        result_image = \
            Image.alpha_composite(pil_rgba_bg_image, pil_rgba_bg_temp)

        # OpenCV形式画像へ変換
        cv_bgr_result_image = cv.cvtColor(
            np.asarray(result_image), cv.COLOR_RGBA2BGRA)

        return cv_bgr_result_image

def img_read(path,size):
    img = cv.imread(path, cv.IMREAD_UNCHANGED)
    img = cv.resize(img, dsize=None, fx=size, fy=size)
    return img

def img_read_black(path,size):
    img = cv.imread(path)
    img = cv.resize(img, dsize=None, fx=size, fy=size)
    return img

def Upper_put(player_data):
    icon_data = ["xp1","xp2","xp3","shelly","colt","block","jessie","nita","dynamike","primo","bull","rico","barley","poco","mortis","bo","spike","crow","piper","xp4","xp5","xp6","xp7","xp8","tro1","tro2","tro3","tro4","pam","None","tro5","tro6","tro7","tro8","darryl","penny","frank","leon","gene","carl","rosa","bibi","tick","8-bit","sandy","emz","bea","max","mrp","jacky","sprout","gale","nani","surge","colette","amber","lou","byron","edgar","ruffs","pls1","plg1","stu","pls2","plg2","belle","squeak","buzz","griff","pls3","plg3","ash","pls4","plg4","meg","lola","pls5","plg5","None","None","grom"]
    
    b = icon_data[int(player_data[1])%100]

    dt = datetime.datetime.today()
    Create_day = "{:02d}/{:02d}/{:02d}".format(dt.year%100,dt.month,dt.day)

    cv_background_image = cv.imread("./Images/back.png")
    cv_background_image = cv.resize(cv_background_image, dsize=None, fx=0.9, fy=0.9)
    S = 0.192
    if (b[0:2] == "xp") or (b[0:3] == "tro"):
        S = 0.35
    elif b == "neko":
        S = 0.235
    elif (b[0:3] == "pls") or (b[0:3] == "plg"):
        S = 0.56
    
    club_icon = img_read("./Images/Club_default.png", 0.44)
    XP_img = img_read("./Images/XP.png", 0.36)
    Tro_img = img_read("./Images/Tro.png", 1.2)
    Besttro_img = img_read("./Images/Best_tro.png", 0.384)
    Vic3_img = img_read("./Images/3v3.png", 0.276)
    Vic2_img = img_read("./Images/Duo.png", 0.768)
    Vic1_img = img_read("./Images/Solo.png", 0.36)
    waku = img_read("./Images/waku.png", 0.384)

    if (b[0:3] == "pls") or (b[0:3] == "plg"):
        portrait = img_read("./Brawler Portraits/Portrait_square/"+b+".png", S)
        image = CvOverlayImage.overlay(cv_background_image, portrait, (48, 42))
    else:
        portrait = img_read("./Brawler Portraits/Portrait_square/"+b+".png", S)#192 235
        image = CvOverlayImage.overlay(cv_background_image, portrait, (48, 42))
        cv.rectangle(image, (48, 42), (125, 120), (0, 0, 0), 3)

    image = CvOverlayImage.overlay(image, club_icon, (50, 144)) #255
    image = CvOverlayImage.overlay(image, XP_img, (42, 218))
    image = CvOverlayImage.overlay(image, waku, (198, 235))
    image = CvOverlayImage.overlay(image, waku, (504, 235))
    image = CvOverlayImage.overlay(image, waku, (810, 235))
    image = CvOverlayImage.overlay(image, waku, (1116, 235))
    image = CvOverlayImage.overlay(image, waku, (1422, 235))
    image = CvOverlayImage.overlay(image, Tro_img, (164, 240))
    image = CvOverlayImage.overlay(image, Besttro_img, (474, 222))
    image = CvOverlayImage.overlay(image, Vic3_img, (780, 237))
    image = CvOverlayImage.overlay(image, Vic1_img, (1086, 240))
    image = CvOverlayImage.overlay(image, Vic2_img, (1392, 240))
    
    font_path_jp = './Fonts/NotoSansJP-Black.otf'
    font_path_en = './Fonts/LilitaOne-Regular.ttf'

    image = CvPutJaText.puttext(image, player_data[0], (168, 30), font_path_jp, 63, (0, 0, 0))
    image = CvPutJaText.puttext(image, "Created by bakehoku\n       (@bakehokuX)", (1220, 20), font_path_jp, 40, (0, 0, 0))
    image =  CvPutJaText.puttext(image, "Create : "+Create_day, (1260, 140), font_path_jp, 40, (0, 0, 0))
    image = CvPutJaText.puttext(image, player_data[8], (144, 132), font_path_jp, 48, (0, 0, 0))
    if player_data[2] >= 100:
        image = CvPutJaText.puttext(image, str(player_data[2]), (54, 246), font_path_en, 43, (255, 255, 255))
    elif player_data[2] >= 10:
        image = CvPutJaText.puttext(image, str(player_data[2]), (65, 246), font_path_en, 43, (255, 255, 255))
    else:
        image = CvPutJaText.puttext(image, str(player_data[2]), (75, 246), font_path_en, 43, (255, 255, 255))

    image = CvPutJaText.puttext(image, str(player_data[3]), (264, 242), font_path_en, 54, (0, 0, 0))
    image = CvPutJaText.puttext(image, str(player_data[4]), (570, 242), font_path_en, 54, (0, 0, 0))
    image = CvPutJaText.puttext(image, str(player_data[5]), (876, 242), font_path_en, 54, (0, 0, 0))
    image = CvPutJaText.puttext(image, str(player_data[6]), (1182, 242), font_path_en, 54, (0, 0, 0))
    image = CvPutJaText.puttext(image, str(player_data[7]), (1488, 242), font_path_en, 54, (0, 0, 0))
    return image

def Rank_put(image, brawler_data, brawlers):
    font_path_en = './Fonts/LilitaOne-Regular.ttf'
    rank_col = [0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,6,6,6,6,6,7]
    colors = [(60,110,190), (185,165,165), (30,200,255), (255,190,30), (255,80,180), (60,175,60), (80,20,200), (255,70,120)]
    base_x = 42
    base_y = 348
    waku_x = 144
    waku_y = 84
    ma = 18
    k = 0

    while True:
        for i in range(10):
            b = brawler_data[i+k*10][0]
            r = brawler_data[i+k*10][1]
            c = rank_col[r-1]
            cv.rectangle(image, (base_x+i*(waku_x+ma), base_y+k*(waku_y+ma)), (base_x+i*(waku_x+ma)+waku_x, base_y+k*(waku_y+ma)+waku_y), colors[c], -1)
            portrait = img_read("./Brawler Portraits/"+b+".png", 0.212)
            image = CvOverlayImage.overlay(image, portrait, (base_x+i*(waku_x+ma), base_y+k*(waku_y+ma)))
            rank_icon = img_read("./Ranks/rank_"+str(c)+".png", 0.66)
            image = CvOverlayImage.overlay(image, rank_icon, (base_x+i*(waku_x+ma)+int(waku_x*0.5), base_y+k*(waku_y+ma)+int(waku_y*0.12)))
            ones = 0
            if r % 10 == 1:
                ones += 1
            if int(r / 10) == 1:
                ones += 1
            if r >= 10:
                image = CvPutJaText.puttext(image, str(r), (base_x+i*(waku_x+ma)+int(waku_x*0.61*(1+ones*0.02)), base_y+k*(waku_y+ma)+int(waku_y*0.41)), font_path_en, 33, (0, 0, 0))
                image = CvPutJaText.puttext(image, str(r), (base_x+i*(waku_x+ma)+int(waku_x*0.63*(1+ones*0.02)), base_y+k*(waku_y+ma)+int(waku_y*0.45)), font_path_en, 28, (255, 255, 255))
            else:
                image = CvPutJaText.puttext(image, str(r), (base_x+i*(waku_x+ma)+int(waku_x*0.66*(1+ones*0.01)), base_y+k*(waku_y+ma)+int(waku_y*0.41)), font_path_en, 33, (0, 0, 0))
                image = CvPutJaText.puttext(image, str(r), (base_x+i*(waku_x+ma)+int(waku_x*0.69*(1+ones*0.01)), base_y+k*(waku_y+ma)+int(waku_y*0.45)), font_path_en, 28, (255, 255, 255))
            cv.rectangle(image, (base_x+i*(waku_x+ma), base_y+k*(waku_y+ma)), (base_x+i*(waku_x+ma)+waku_x, base_y+k*(waku_y+ma)+waku_y), (0,0,0), 2)
            brawlers -= 1
            if brawlers <= 0:
                break
        k += 1
        if brawlers <= 0:
            break
    return image

def maker(tag):
    brawler_data, brawlers, player_data = player_data_API.GETrank(str(tag))#2LL9CJ9 R88CG22P
    image = Upper_put(player_data)
    image = Rank_put(image, brawler_data, brawlers)

    print("  作成完了", end = "")
    #cv.imshow("sample", image)
    path = "./templates/Upload/res.jpg"
    cv.imwrite(path, image)
    #cv.waitKey(0)
    
    #return path

"""if __name__ == '__main__':
    maker("2LL9CJ9")"""
"""    while True:
        tag = input("プレイヤータグ:#")
        #b = input("Icon(全て小文字):")
        brawler_data, brawlers, player_data = player_data_API.GETrank(str(tag))#2LL9CJ9 R88CG22P
        image,b = Upper_put(player_data)
        image = Rank_put(image, brawler_data, brawlers)

        print("  作成完了")
        #cv.imshow("sample", image)
        path = "./result/"+str(tag)+"_"+id+".jpg"
        cv.imwrite(path, image)
        #cv.waitKey(0)"""