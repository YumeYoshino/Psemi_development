from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# 「始める」を押すと次のHTMLファイルに移動する
@app.route("/start")
def start():
    # 移動先のHTMLファイルの名前を指定します
    return render_template("/start_page.html")

# 「続ける」を押すと次のHTMLファイルに移動する
@app.route("/continue")
def continue_game():
    # 移動先のHTMLファイルの名前を指定します
    return redirect("/continue_page.html")
if __name__ == "__main__":
    app.run(debug=True)

