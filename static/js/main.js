
//読み込み時に実行される関数
(function () {
  drawBGImage("../static/images/download.jpg");
  drawCharaImage("../static/images/download.jpg");
})();

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


//テキストを読み込み
function initRevealTextMessage(text) {
    const chars = text.split("");
    const textMessageP = document.querySelector(".text_message_p");
    const startButton = document.getElementById("start-button");
    
    let timeout;
    
    startButton.addEventListener("click", () => {
      startRevealTextMessage();
      startButton.disabled = true;
    });
}
    
  
  //一文字ずつ表示
  function revealTextMessage(list) {
    let timeout;
    const next = list.splice(0, 1)[0];
    next.span.classList.add("revealed");
  
    if (list.length > 0) {
      timeout = setTimeout(() => {
        revealTextMessage(list);
      }, next.delayAfter);
    } else {
      clearTimeout(timeout);
    }
  }
  

//読み込み時に実行される関数
(function () {
    drawBGImage("/static/images/demo2.jpg");
    drawCharaImage("/static/images/demo.jpg.png");
    initRevealTextMessage("あいうえおかきくけこさしすせそたちつてと"); //ここで呼び出し
  })();
  
