/** assuming all parameters are validated as numbers */

function breakdown(n) {
    //use division by powers of ten
    var divisor = 1;
    // get number of digits
    var sn = n + "";
    var ndigits = sn.length;
    // current digit of 10 to validate
    var i = ndigits;
    var breakdownList = [];
    while (i > 0) {
	// convert to Number
	digit = parseInt(sn[i - 1], 10);
	// validate all numbers that have more than one-zero
	if (digit != 0) {
	    breakdownList.push(digit * Math.pow(10, ndigits - i));
	}
	i--;
    }
    return breakdownList;
}

function showBreakdown(n) {
    var l = breakdown(n);
    console.log(n + " = ");
    for (factor in l) {
	console.log(l[factor] + " + ");
    }
}

showBreakdown(344506);
showBreakdown(3006);
