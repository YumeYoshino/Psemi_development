from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("/index.html")

@app.route("/first")
def first():
    # 移動先のHTMLファイルの名前を指定します
    return render_template("/first_page.html")

@app.route("/first_first")
def first_first():
    # 移動先のHTMLファイルの名前を指定します
    return render_template("/first_first_page.html")

@app.route("/first_seikai")
def first_seikai():
    # 移動先のHTMLファイルの名前を指定します
    return render_template("/first_seikai_page.html")

@app.route("/first_fuseikai")
def first_fuseikai():
    # 移動先のHTMLファイルの名前を指定します
    return render_template("/first_fuseikai_page.html")

@app.route("/first_kaisetu")
def first_kaisetu():
    # 移動先のHTMLファイルの名前を指定します
    return render_template("/first_kaisetu_page.html")

@app.route("/second")
def second():
    # 移動先のHTMLファイルの名前を指定します
    return render_template("/second_page.html")

@app.route("/second/page2")
def second_page2():
    # 移動先のHTMLファイルの名前を指定します
    return render_template("/second_page2.html")

@app.route("/second/page3")
def second_page3():
    # 移動先のHTMLファイルの名前を指定します
    return render_template("/second_page3.html")

@app.route("/second/true")
def second_page_true():
    # 移動先のHTMLファイルの名前を指定します
    return render_template("/second_page_true.html")

@app.route("/second/false")
def second_page_false():
    # 移動先のHTMLファイルの名前を指定します
    return render_template("/second_page_false.html")

# 「続ける」を押すと次のHTMLファイルに移動する
@app.route("/question3")
def question3():
    # 移動先のHTMLファイルの名前を指定します
    return render_template("/question3_page.html")

@app.route("/Q3_correct")
def correct3():
    # 移動先のHTMLファイルの名前を指定します
    return render_template("/question3_correct.html")

@app.route("/Q3_incorrect")
def incorrect3():
    # 移動先のHTMLファイルの名前を指定します
    return render_template("/question3_incorrect.html")


@app.route("/end")
def end():
    return render_template("/end.html")

if __name__ == "__main__":
    app.run(debug=True)
