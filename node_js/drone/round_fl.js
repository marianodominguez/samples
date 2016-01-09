'use strict';

var RollingSpider = require('rolling-spider');
var temporal = require('temporal');

var drone = new RollingSpider();

drone.connect(function () {
 
  drone.setup(function () {
    drone.flatTrim();
    drone.startPing();
    drone.flatTrim();
  
     temporal.queue([
      {
        delay: 5000,
        task: function () {
          drone.takeOff();
          drone.flatTrim();
        }
      },
      {
        delay: 1000,
        task: function () {
          drone.up(
            {steps:50});
        }
      },
      {
        delay: 3000,
        task: function () {
          drone.clockwise({steps:90});
        }
      },
      {
        delay: 5000,
        task: function () {
          drone.backFlip();
        }
      },
      {
        delay: 5000,
        task: function () {
          drone.land();
        }
      },
      {
        delay: 5000,
        task: function () {
          temporal.clear();
          process.exit(0);
        }
      }
    ]);

  });
});

