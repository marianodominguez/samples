var CURRENCIES= ["USD", "EUR", "JPY"];
var URL='http://localhost:3000';

$(document).ready(function() {
    
    var transferMoney = function() {
        navigateTo('transferPage');
    }
    
    var viewTransactions = function(start, end) {
    
        var currentLast = $("#transactionList").children().last();
        
        var start = 0;
        var end = 10 ;
        
        if (currentLast.attr('id')) {
            var offset = parseInt(currentLast.attr('id') , 10 );
            start +=offset+1;
            end += offset+1; 
        }
        
        navigateTo('transactionPage');
         
        $.ajax({
            url: URL+"/transactions",
            data:{
                start: start,
                end: end
            },
            dataType: "json",
            success: function(result){
                for(i in result) {
                    var transaction = result[i];
                    var newItem = $("<li>", {
                        id: transaction.id,
                        html: transaction.name + "," 
                            + transaction.amount + "" + transaction.currency
                    });
                    
                    $("#transactionList").append(newItem);
                }          
            }  
        });
        
    }

    var clear = function() {
	
    }
    
    var next = function() {
        $.ajax({
            url:URL+"/transfer",
            success: function(result){
                navigateTo('buttonPage');
            }  
        });
    }

    var back = function() {
        navigateTo('buttonPage');
    }

    function navigateTo(page) {
        $(".page").hide();
        $("#"+page).show();
    }
       
    function loadCurrency(curencyList) {
        $('#currency').empty();
        for(var i in curencyList) {
            $('#currency').append($("<option></option>")
				  .attr("value",curencyList[i])
				  .text(curencyList[i])); 
        }

    }

    navigateTo('buttonPage');
    loadCurrency(CURRENCIES);
    $("#transfer").click(transferMoney);
    $("#viewTransactions").click(viewTransactions);
    $("#clear").click(clear);
    $("#next").click(next);
    $("#back").click(back);
    $("#more").click(viewTransactions);
    
});

