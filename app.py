from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("/index.html")

# 「続ける」を押すと次のHTMLファイルに移動する
@app.route("/question3")
def question3():
    # 移動先のHTMLファイルの名前を指定します
    return render_template("/question3_page.html")


@app.route("/first")
def first():
    # 移動先のHTMLファイルの名前を指定します
    return render_template("/first_page.html")

@app.route("/second")
def second():
    # 移動先のHTMLファイルの名前を指定します
    return render_template("/second_page.html")

@app.route("/third")
def third():
    # 移動先のHTMLファイルの名前を指定します
    return render_template("/third_page.html")

@app.route("/Q3_correct")
def correct3():
    # 移動先のHTMLファイルの名前を指定します
    return render_template("/question3_correct.html")

@app.route("/Q3_incorrect")
def incorrect3():
    # 移動先のHTMLファイルの名前を指定します
    return render_template("/question3_incorrect.html")
if __name__ == "__main__":
    app.run(debug=True)
