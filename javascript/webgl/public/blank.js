main();

function initGL(canvas,gl) {
    try {

        gl.viewportWidth = canvas.width;
        gl.viewportHeigh = canvas.heigh;
    }
    catch(e) {
        if(!gl) {
            alert("No webGL !");
        }
    }
}



function main() {
    const canvas = document.getElementById("canvas");
    const gl=canvas.getContext("webgl");

    initGL(canvas,gl);
    //initShaders();
    //initBuffers();

    gl.clearColor(0.0, 0.0, 0.0, 1.0);
    gl.clear(gl.COLOR_BUFFER_BIT);

    drawScene(gl);
  }

function drawScene(gl) {


}