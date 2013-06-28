var canvas = null;
var ctx = null;
var currentImage = null;

function init() {
	//load images into palette

	var icons = ['arrow.png', 'money_exchange.png', 'exit.png'];
	var container = document.getElementById('images');
	container.style.backgroundColor="#f3f3f3";
	for(i in icons) {
		var image = new Image();
		image.src = 'icons/' + icons[i];
        image.addEventListener('dragstart', function() {
            currentImage = this;
            console.log("DragStart " + this);
        });
        container.appendChild(image);
	}
}

function drawGrid() {
	canvas= document.getElementById("drawpad");
    
    if(canvas.getContext) {
      ctx = canvas.getContext("2d");
      ctx.strokeStyle = '#DDDDDD';
      ctx.lineWidth = 1;
    }
    else {
      alert("canvas unsupported in this browser");
      return;
    }

    for (var y = 0; y < canvas.height ; y+= 10) {
    	ctx.beginPath();

        ctx.moveTo(0, y);
      	ctx.lineTo(canvas.width - 1 , y);
      	ctx.closePath();
      	ctx.stroke();
    }
}

function activateEvents() {
	canvas.addEventListener('dragover', cancel);
	canvas.addEventListener( 'dragenter', cancel);

    canvas.addEventListener('drop', function (event) {
        // stops the browser from redirecting off to the text.
        if (event.preventDefault) {
            event.preventDefault(); 
        }
        console.log("dropped");
        //Draw the image in the grid
        drawImage(event);
    });
}

function cancel(event) {
  if (event.preventDefault) {
    event.preventDefault();
  }
  return false;
}

function drawImage(event) {
    var x = event.clientX - canvas.offsetLeft - currentImage.clientWidth /2;
    var y = event.clientY - canvas.offsetTop - currentImage.clientHeight /2 ;

    if (currentImage != null) {
        ctx.drawImage(currentImage,x,y);
    }
}

console.log("init");

onload = function() {
    init();
    drawGrid();
    activateEvents();
};