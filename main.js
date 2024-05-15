const { JSDOM } = require('jsdom');

// HTML の文字列を渡して JSDOM インスタンスを作成
const dom = new JSDOM('<div id="game-container"><canvas id="background-layer" width="1920" height="1080"></canvas><canvas id="character-layer" width="1920" height="1080"></canvas><div class="message_box"><p class="text_message_p"></p></div></div>');
const window = dom.window;
const document = window.document;

  
  //背景の描画
  function drawBGImage(src) {
    const canvas = document.querySelector("#background-layer");
    const ctx = canvas.getContext("2d");
    const img = new Image();
    img.src = src;
  
    img.addEventListener("load", (event) => {
      ctx.drawImage(img, 0, 0);
    });
  }
  
  //キャラクターの描画
  function drawCharaImage(src) {
    const canvas = document.querySelector("#character-layer");
    const bgcanvas = document.querySelector("#background-layer");
    const ctx = canvas.getContext("2d");
    const img = new Image();
    img.src = src;
  
    img.addEventListener("load", (event) => {
      const posX = (bgcanvas.width - img.width) / 2;
      ctx.drawImage(img, posX, 100);
    });
  }

  //読み込み時に実行される関数
(function () {
    //画像のファイルディレクトリは変化する恐れあり
    drawBGImage("C:\Users\InoueAkito\Psemi_development\img\_high_rise_building_1.jpg");
    drawCharaImage("C:\Users\InoueAkito\Psemi_development\img\_high_rise_building_1.jpg");
  })();

  