var palette = (function(){
    var public = {};

    var canvas = null;
    var ctx = null;
    var currentImage = null;
    var dropZone = null;
    var newImage = null;

    public.init = function () {
        //load images into palette

        var icons = ['arrow.png', 'money_exchange.png', 'exit.png'];
        var container = document.getElementById('images');
        container.style.backgroundColor="#f3f3f3";
        for(i in icons) {
            var image = new Image();
            image.src = 'icons/' + icons[i];
            image.addEventListener('dragstart', function() {
              newImage = this;
            });
            container.appendChild(image);
        }
      dropZone = document.getElementById('dropZone');
    }

    public.drawGrid = function () {
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

    public.activateEvents = function () {
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
        if (newImage != null) {
          var x = event.clientX;
          var y = event.clientY;

          console.log("Copied image:" + x +"," + y);
          var copyImage = new Image();
          copyImage.src= newImage.src;
          dropZone.appendChild(copyImage);
          copyImage.style.position = 'absolute';
          copyImage.style.left = x + 'px';
          copyImage.style.top = y + 'px';
          copyImage.addEventListener('dragstart', moveStart);
          copyImage.addEventListener('dragend', moveEnd);
        }
    }

    function moveStart() {
      currentImage = this;
      newImage = null;
    }

    function moveEnd(event){
        if (currentImage != null) {
          var x = event.clientX;
          var y = event.clientY;
          console.log("Moved image " + x +"," + y);
          currentImage.style.position = 'absolute';
          currentImage.style.left = x + 'px';
          currentImage.style.top = y + 'px';
        }
        cancel(event);
    }

    return public;
})();

console.log("init");

onload = function() {
    palette.init();
    palette.drawGrid();
    palette.activateEvents();
};
