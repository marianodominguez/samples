var Diamond = {
  w: 800,
  h: 600,
  ctx: null,
  r: 300
};

Diamond.draw = function (sides) {
   var th = 2 * Math.PI / sides;
   for(var i=0; i< sides ; i++) {

      x = this.r * Math.sin(th * i);
      y = this.r * Math.cos(th * i);

      for(var j=0; j< sides ; j++) {

          x1 = this.r * Math.sin(th * j);
          y1 = this.r * Math.cos(th * j);
          this.ctx.beginPath();

          this.ctx.moveTo(x + this.w/2, this.h/2 - y );
          this.ctx.lineTo(x1 + this.w/2 , this.h/2 - y1);
          this.ctx.closePath();
          this.ctx.stroke();
      }
   }
};

Diamond.drawDiamond = function () {
    var canvas= document.getElementById("drawCanvas");
    console.log('launched' + this.w);
    if(canvas.getContext) {
      this.ctx = canvas.getContext("2d");
      this.ctx.strokeStyle = "blue";
      this.ctx.lineWidth = 1;
    }
    else {
      alert("canvas unsupported in this browser");
      return;
    }

   this.ctx.moveTo(this.w/2,this.h/2)
   this.draw(21);
};

console.log("init");

onload = function() {
    Diamond.drawDiamond();
};