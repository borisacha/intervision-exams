import React from 'react';
import './App.css';
import ConnectChat from './components/ConnectChat';

function App() {
  console.log('Rendering App Component'); // Add this log
  return (
    <div className="App">
      <header className="App-header">
        <h1>Intervision Insurance AI Solution Demo</h1>
        <p className="intro-text">
          Welcome to the Intervision Insurance AI Solution Demo. This application showcases how we leverage
          Amazon Web Services (AWS) to enhance customer interactions and support. The solution integrates 
          Amazon Lex, AWS Lambda, DynamoDB, Amazon Connect, and Amazon Bedrock to provide an efficient and 
          automated customer service experience.
        </p>
        <h2>Project Overview</h2>
        <p className="project-overview">
          Our chatbot assists customers with common inquiries such as policy details and premium increases.
          The chatbot uses AI to dynamically verify customer information, solve problems, and seamlessly
          transfer to a live agent if necessary. Key components include:
        </p>
        <ul className="components-list">
          <li><strong>Amazon Lex:</strong> Handles initial customer interactions and gathers information.</li>
          <li><strong>AWS Lambda:</strong> Executes functions for customer verification and problem-solving.</li>
          <li><strong>DynamoDB:</strong> Stores and retrieves customer data.</li>
          <li><strong>Amazon Connect:</strong> Transfers customers to live agents and logs interactions.</li>
          <li><strong>Amazon Bedrock:</strong> Provides AI-driven responses by querying the knowledge base.</li>
        </ul>
        <h2>Chatbot Interaction</h2>
        <p className="chatbot-interaction">
          Initiate a conversation with our chatbot to see how it handles customer queries dynamically and 
          efficiently. The chatbot will verify your identity, provide assistance with your issue, and 
          offer to connect you to a live agent if needed.
        </p>
        <ConnectChat />
      </header>
    </div>
  );
}

export default App;
