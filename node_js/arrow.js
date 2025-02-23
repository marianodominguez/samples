const obj = {
    name: "Alice",
    // Arrow function uses parent (global/window) scope's `this`
    greet: () => console.log(this.name) // ❌ `this` is undefined/global
  };
  
  obj.greet(); // Logs `undefined` (or `window.name` in browsers)

  const obj2 = {
    name: "Alice",
    // Function keyword uses the object's `this`
    greet: function() {
      console.log(this.name); // ✅ "Alice"
    }
  };
  
  obj2.greet();