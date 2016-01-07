var RollingSpider = require("rolling-spider");
 
var yourDrone = new RollingSpider();
 
yourDrone.connect(function () {
    console.log("connected ...")
	yourDrone.trim();
	yourDrone.takeOff();
	setTimeout(function () {
		yourDrone.forward(50);
		setTimeout(function () {
			yourDrone.land();
		}, 500);
	}, 3000);
});

