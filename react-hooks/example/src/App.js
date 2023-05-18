import React, { useState } from 'react';

function App() {

  const [count, setCount] = useState(4);
  const [theme, setTheme] = useState('blue');

  function decrementCount() {
    setCount(prevCount => prevCount - 1);
  }

  function incrementCount() {
    setCount(prevCount => prevCount + 1);
  }

  function changeTheme() { 
    // choose a random color
    const colors = ['red', 'blue', 'green', 'orange', 'purple'];
    const randomColor = colors[Math.floor(Math.random() * colors.length)];
    setTheme(randomColor);

  }

  // alternative changeTheme function
  function changeTheme() {

    setTheme(prevTheme => {
      if (prevTheme === 'blue') {
        return 'red';
          
      } else {
        return 'blue';
      }
    });
  }

  return (
    <>
      <button onClick={decrementCount}>-</button>
      <span>{count}</span>
      <button onClick={incrementCount}>+</button>
      <br />
      <span onClick={}>{theme}</span>
    </>
  );
}

export default App;
