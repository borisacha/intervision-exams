import React from 'react';
import './App.css';
import ConnectChat from './components/ConnectChat';  // Component for Amazon Connect Chat

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Amazon Services Demo</h1>
        <ConnectChat />  {/* This initializes and handles the chatbot */}
      </header>
    </div>
  );
}

export default App;
