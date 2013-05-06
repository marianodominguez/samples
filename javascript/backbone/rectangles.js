$(document).ready(function() {

	var Rectangle = Backbone.Model.extend({});

	var RectangleView = Backbone.View.extend({
		tagName: 'div',
		
		className: 'rectangle',
		
		render: function() {
			this.setDimensions();
			this.setPosition();
			return this;
		},

		events: {
			'click': 'move'
		},
		
		setDimensions: function() {
			this.$el.css({
				width: this.model.get('width') + 'px',
				height: this.model.get('height') + 'px',
			});
		},
		
		setPosition: function() {
			var position = this.model.get('position');
			this.$el.css({
				left: position.x,
				top: position.y
			});
		},
		move: function() {
			this.$el.css('left', this.$el.position().left + 10);			
		}
	
	});


	var myRectangle = new Rectangle({
		width: 100,
		height: 60,
		position: {
			x:300,
			y:50
		}
	});

	var myRectangleView = new RectangleView({model: myRectangle});
		
	$('div#canvas').append(myRectangleView.render().el);	
});
