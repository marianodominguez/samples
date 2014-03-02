
$(document).ready(function () {

    var Todo = Backbone.Model.extend({
        defaults: {
            title:'',
            completed: false
        }
    });

    var TodoListType = Backbone.Collection.extend({
        model: Todo,
        localStorage: new Store('todos-backbone')
    });

    var todoList = {};

    var TodoListView = Backbone.View.extend({
        initialize : function() {
            this.render();
        },
        render : function() {
            var model = {
                title : "TODO list",
                todo: todoList.models};
            var template = _.template( $("#todo_template").html(),
                model );
            this.$el.html(template);
        }
    });

    var start_disabled = function() {
        var firstTodo = new Todo();
        console.log("Default Title : " + firstTodo.get('title'));
        firstTodo.set('title', 'Enjoy reading the book');
        console.log('Title changed: ' + firstTodo.get('title'));
    }

    var createModel = function() {
        todoList = new TodoListType;
        todoList.fetch();

        if (todoList.length === 0) {
            console.log("storage empty, create");
            todoList.create({title: 'Try out code examples'});
            var firstTodo = new Todo({title: 'Read whole book'});
            todoList.create(firstTodo);
            var thirdTodo = new Todo({title: 'Make something cool'});
            todoList.create(thirdTodo);
        }
        console.log(todoList.models);
    }

    createModel();
    var view = new TodoListView( { el: $("#todo") } );
});