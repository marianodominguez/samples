var MAX_ROWS = 1000;
var BUFFER_SIZE = 10;
var CURRENCY= ["JPY", "USD", "EUR"];

var testData = loadTransactions();

module.exports = {
    postTransfer: postTransfer,
    getTransactions: getTransactions
};
    
    
function postTransfer(source, destination) {
    return {
        result: "success",
        transactionId : 1000
    };
}

function loadTransactions() {
    var result = [];
    for(var i=0; i< MAX_ROWS; i++) {
        var t = {
            id: i,
            name : "Transaction #" + i,
            amount : (i * 453.13).toFixed(2),
            currency : CURRENCY[i % CURRENCY.length]
            };
        result.push(t);
    }
    
    return result;
}

function getTransactions(start, end) {
    var chunk = [];
    chunk = testData.slice(start, end);
    //console.log(chunk);
    return chunk;
}


