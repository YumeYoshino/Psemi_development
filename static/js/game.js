document.addEventListener("DOMContentLoaded", function() {
    const canvas = document.getElementById("gameCanvas");
    const ctx = canvas.getContext("2d");

    const color = {
        white: "rgb(255, 255, 255)",
        black: "rgb(0, 0, 0)",
        blue: "rgb(0, 255, 255)"
    };

    let tmr = 0;
    let idx = 0;

    const buttonRects = [
        { x: 110, y: 360, width: 120, height: 40, text: "はじめる" },
        { x: 170, y: 410, width: 120, height: 40, text: "つづける" },
        { x: 240, y: 470, width: 120, height: 40, text: "おわる" }
    ];

    const bgImage = new Image();
    // bgImage.src = "../images/_high_rise_building_1.jpg";
    bgImage.src = "{{url_for('static',filename='/images/_high_rise_building_1.jpg')}}";


    function drawText(size, text, color, x, y) {
        ctx.font = `${size}px 'MPLUS'`;
        ctx.fillStyle = color;
        ctx.fillText(text, x, y);
    }

    function drawButton(button, rectColor, textColor) {
        ctx.fillStyle = rectColor;
        ctx.fillRect(button.x, button.y, button.width, button.height);
        ctx.strokeStyle = textColor;
        ctx.lineWidth = 2;
        ctx.strokeRect(button.x, button.y, button.width, button.height);
        
        drawText(24, button.text, textColor, button.x + 10, button.y + 28);
    }

    function gameLoop() {
        tmr++;

        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(bgImage, 0, 0, canvas.width, canvas.height);

        if (idx === 0) {
            drawText(70, "インシデント対応", color.black, 30, 100);
            drawText(75, "RPG", color.black, 30, 220);
            buttonRects.forEach(button => drawButton(button, color.white, color.blue));
        } else if (idx === 1) {
            ctx.fillStyle = color.black;
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            drawText(70, "始める", color.white, 30, 100);
        } else if (idx === 2) {
            ctx.fillStyle = color.black;
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            drawText(70, "つづける", color.white, 30, 100);
            if (tmr > 30) {
                idx = 0;
                tmr = 0;
            }
        } else if (idx === 3) {
            window.close();
        }

        requestAnimationFrame(gameLoop);
    }

    canvas.addEventListener("click", function(event) {
        const rect = canvas.getBoundingClientRect();
        const mouseX = event.clientX - rect.left;
        const mouseY = event.clientY - rect.top;

        if (idx === 0) {
            buttonRects.forEach((button, i) => {
                if (mouseX > button.x && mouseX < button.x + button.width &&
                    mouseY > button.y && mouseY < button.y + button.height) {
                    idx = i + 1;
                    tmr = 0;
                }
            });
        }
    });

    bgImage.onload = function() {
        gameLoop();
    };

});
