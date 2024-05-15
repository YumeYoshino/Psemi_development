
// extra.js
function handleIdx2(ctx, canvas, color) {
    ctx.fillStyle = color.black;
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.font = "70px 'MPLUS'";
    ctx.fillStyle = color.white;
    ctx.fillText("つづける", 30, 100);
}

// グローバルに公開するために、windowオブジェクトに追加します
window.handleIdx1 = handleIdx1;
