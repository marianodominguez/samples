var mdmDraw = (function() {
    var public = {};

    var w = 800;
    var h = 600;
    var ctx;
    var currentShape=1;

    var init = function() {
        var canvas = document.getElementById("drawCanvas");

        if (canvas.getContext) {
        ctx = canvas.getContext("2d");
        ctx.strokeStyle = 'red';
        ctx.lineWidth = 1;
        } else {
        alert("canvas unsupported in this browser");
        return;
        }
    }

    var connect = function() {
        var button = document.getElementById("drawButton");
        button.addEventListener("click", drawShape);
    }

    var drawShape = function() {
        ctx.moveTo(w / 2, h / 2)
        ctx.clearRect(0,0,w,h);
        switch(currentShape) {
        case 1:
        diamond(25);
        break;
        case 2:
        web();
        break;
        case 3:
        stitchOne();
        break;
        case 4:
        stitchTwo();
        break;
        case 5:
        weird(25);
        break;
        default:
        currentShape=0;
        }
        currentShape++;
    }

    function stitchOne() {
        ctx.strokeStyle = 'red';
        for (th = 0.0; th < 2 * Math.PI; th += Math.PI / 100) {
        x1 = 150 * Math.sin(th);
        y1 = 150 * Math.cos(th);
        x2 = 300 * Math.cos(th);
        y2 = 300 * Math.cos(th);
        ctx.beginPath()
        ctx.moveTo(x1 + w / 2, h / 2 - y1);
        ctx.lineTo(x2 + w / 2, h / 2 - y2);
        ctx.closePath();
        ctx.stroke();
        }
    }

    function stitchTwo() {
        ctx.strokeStyle = 'blue';
        for (th = 0.0; th < 2 * Math.PI; th += Math.PI / 100) {
        x1 = 200 * Math.sin(th);
        y1 = 200 * Math.cos(th);
        x2 = 300 * Math.cos(th);
        y2 = 300 * Math.sin(th);
        ctx.beginPath()
        ctx.moveTo(x1 + w / 2, h / 2 - y1);
        ctx.lineTo(x2 + w / 2, h / 2 - y2);
        ctx.closePath();
        ctx.stroke();
        }
    }

    function web() {
        ctx.strokeStyle = 'blue';
        for (var x = 0; x < w; x += 10) {
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(0, h - x);
        ctx.closePath();
        ctx.stroke();
        }
    }

    function diamond(sides) {
        ctx.strokeStyle = 'black';
        var th = 2 * Math.PI / sides;
        for (var i = 0; i < sides; i++) {
        x = 250 * Math.sin(th * i);
        y = 250 * Math.cos(th * i);

        for (var j = 0; j < sides; j++) {
            x1 = 250 * Math.sin(th * j);
            y1 = 250 * Math.cos(th * j);
            ctx.beginPath();
            ctx.moveTo(x + w / 2, h / 2 - y);
            ctx.lineTo(x1 + w / 2, h / 2 - y1);
            ctx.closePath();
            ctx.stroke();
        }
        }
    }

    function weird(sides) {
        ctx.strokeStyle = 'blue';
        var th = 2 * Math.PI / sides;
        for (var i = 0; i < sides; i++) {
        x = 200 * Math.sin(th * i);
        y = 200 * Math.cos(th * i);

        for (var j = 0; j < sides; j++) {
            x1 = 250 * Math.cos(th * j);
            y1 = 250 * Math.cos(th * j);
            ctx.beginPath();
            ctx.moveTo(x + w / 2, h / 2 - y);
            ctx.lineTo(x1 + w / 2, h / 2 - y1);
            ctx.closePath();
            ctx.stroke();
        }
        }
    }

    public = {
        init: init,
        connect: connect
    };
    return public;
    })();

window.onload = function (){
    mdmDraw.init();
    mdmDraw.connect();
}
