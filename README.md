# Intervision Insurance AI Solution POC

## Business Value

Intervision Insurance aims to enhance customer satisfaction and operational efficiency by leveraging AI and automation technologies. This solution reduces the number of customers requiring agent assistance, thereby lowering operational costs and improving response times. By automating customer interactions and dynamically addressing common issues, the company can provide more personalized and efficient service, leading to higher customer retention and satisfaction.

## Business Problem

Intervision Insurance faces a high volume of customer inquiries related to policy details, premium increases, and other common issues. Many customers are routed to live agents, resulting in long wait times and increased operational costs. This inefficiency impacts customer satisfaction and the overall effectiveness of the support team.

## Issues Faced

1. **High Operational Costs:** 
   - A significant number of customer inquiries require agent intervention, leading to increased labor costs.
   
2. **Long Wait Times:**
   - Customers experience long wait times due to the high volume of calls, resulting in dissatisfaction and potential churn.
   
3. **Inefficient Problem Resolution:**
   - Agents spend a considerable amount of time handling repetitive inquiries, reducing their availability for more complex issues.
   
4. **Inconsistent Customer Experience:**
   - Manual handling of customer queries can lead to inconsistent responses and service quality.

## Solution Overview

To address these issues, Intervision Insurance has implemented an AI-powered chatbot using Amazon Lex, AWS Lambda, DynamoDB, Amazon Connect, and Amazon Bedrock. This solution automates customer interactions, dynamically verifies customer information, and provides AI-driven responses to common issues.

## Architecture Daigram
The AI-powered support system automates customer interactions using Amazon Lex for natural language understanding, AWS Lambda for serverless processing, DynamoDB for data storage, Amazon Connect for call center operations, and Amazon Bedrock for AI-driven knowledge base queries.

### Architecture Diagram
![Architecture Diagram](https://raw.githubusercontent.com/borisacha/intervision-exams/main/daigram.svg)

### Explanation
The architecture diagram illustrates the workflow of the AI-powered support system:

1. **Users**: Customers initiate the interaction through a chat interface.
2. **Amazon Connect Chat**: Manages the initial customer interaction.
3. **LexBot**: Handles customer inquiries and processes intents.
4. **DynamoDbQuery Lambda Function**: Verifies customer information by querying Amazon DynamoDB.
5. **Amazon DynamoDB**: Stores customer information such as policy ID, first name, and last name.
6. **QueryKnowledgeBaseFunction Lambda Function**: Queries the knowledge base in Amazon Bedrock to provide AI-driven responses.
7. **Amazon Bedrock**: Hosts the knowledge base and processes customer queries to find relevant information.
8. **Knowledge Base**: A repository of information used by Amazon Bedrock to resolve customer queries.

### Key Components and Workflow

1. **Amazon Lex Chatbot:**
   - The chatbot handles initial customer interactions, gathering information and addressing common issues through predefined intents.

2. **Dynamic Customer Verification:**
   - When a customer reports an issue, such as an increase in their insurance premium, the chatbot asks for their insurance ID or policy ID.
   - A Lambda function (`DynamoDbQuery`) is triggered, which queries DynamoDB to retrieve the customer’s information (e.g., first name, last name).
   - The chatbot uses this information to verify the customer dynamically.

3. **AI-Driven Problem Solving:**
   - For issues like premium increases, the chatbot leverages a knowledge base set up in Amazon Bedrock.
   - A foundational model like Claude analyzes the conversation and queries the knowledge base to find potential causes for the premium increase.
   - A Lambda function (`QueryKnowledgeBaseFunction`) manages this logic, returning the results to the customer.
   - The chatbot asks if the customer is satisfied with the response or wants to be connected to an agent.

4. **Agent Transfer via Amazon Connect:**
   - If the customer needs further assistance, they are transferred to an agent using Amazon Connect.
   - The flow includes logging interactions to CloudWatch Logs and setting custom error logging attributes.

### Chat Widget

A React application is created for testing and deploying the chat widget, allowing customers to interact with the chatbot seamlessly.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js:** The runtime environment required to run the application. [Download Node.js](https://nodejs.org/)
- **npm:** The package manager for JavaScript, installed with Node.js.

## Installation

Follow these steps to set up the project on your local machine:

### Clone the Repository


git clone https://github.com/borisacha/intervision-exams.git
cd intervision-exams

## Install Dependencies

Navigate to the widget-site directory amd install all the required dependencies:



npm install


## Running the Application

To start the application on your local development server:


npm start


This command will compile the application and automatically open it in your default web browser. The application typically runs on http://localhost:3000 unless the port is already in use.

### Additional Notes

- **Amazon Lex**: Configured with intents for handling customer interactions.
- **AWS Lambda Functions**:
  - **DynamoDbQuery**: Handles customer verification by querying DynamoDB.
  - **QueryKnowledgeBaseFunction**: Handles querying the knowledge base in Amazon Bedrock.
- **Amazon Connect**: Configured for transferring customers to agents and logging interactions.
- **Amazon Bedrock**: Used for the knowledge base and AI-driven problem-solving capabilities.
