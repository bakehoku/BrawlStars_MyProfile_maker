from flask import Flask,request,render_template,jsonify, url_for
import profile_create

#Flaskの設定
app = Flask(__name__, static_folder='./templates/Upload')

@app.route("/")
def check():
    # htmlファイルをレンダリング
    return render_template('index.html')

@app.route("/result", methods=['GET'])
def result():
    # htmlファイルをレンダリング
    return render_template('result.html', img_url="./Upload/res.jpg")

@app.route('/output', methods=['POST'])
def output():
    #json形式でURLを受け取る
    tag = request.json['url1']
    profile_create.maker(tag)
    """df = scr(url)
    print(df)
    out_of_stock_rate = df.stock_flg.sum()/len(df)
    print(out_of_stock_rate)
    return_data = {"result":round(out_of_stock_rate*100,1)}"""
    return_data = {"result":"成功"}
    #return render_template('index.html', img_url="./../Upload/res.jpg")
    return jsonify(ResultSet=return_data)

if __name__ == "__main__":
    app.run()