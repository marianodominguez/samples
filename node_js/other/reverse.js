function isVowel(c) {
  var result = "aeiouAEIOU".indexOf(c) >= 0
  //console.log(c + "," + result);
  return result;
}

function swap(s, i, j) {
  if (i<0 || i>=j || j>=s.length ) return s;
  return s.slice(0, i) + s[j] + s.slice(i+1,j) + s[i] + s.slice(j+1);
}

function rev(s) {
  if (!s || s.length < 1) {
    return s;
  }
  var b=0;
  var e=s.length-1;

  while(b<e && e>=0) {
      while ( !isVowel(s[e]) && e>=0 ) {
         e--;
      }
      while ( !isVowel(s[b]) && b<s.length ) {
        b++;
      }
      if( b!=e ) {
        s = swap(s,b,e);
      }
      e--;
      b++;
  }
  return s;
}

console.log(rev("united states"));
console.log(rev("mariano"));