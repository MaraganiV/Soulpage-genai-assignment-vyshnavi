**TASK1**
This project presents a Multi-Agent AI system developed using LangGraph and LangChain to perform movie data analysis. The system demonstrates how independent AI agents can collaborate through an orchestrated workflow to collect information, analyze it, and generate meaningful insights.

The project highlights practical implementation of agent-based architecture and automated decision support.

**Agent Design**
**Data Collector Agent**
Gathers movie-related information such as ratings, audience feedback, and box office performance.

Formats the data for analysis.

**Analyst Agent**
Evaluates the collected data.

Produces a concise summary with key observations about the movie’s performance.

**Workflow Architecture**

User Query → Data Collector → Analyst → Final Insight

This workflow illustrates coordinated communication between agents to complete a multi-step analytical task.

**Technology Stack**
Language: Python

Libraries: LangChain, LangGraph

Concepts: Multi-Agent Systems, Workflow Orchestration, Automated Insights

**Setup Instructions**
**Clone the Repository**
git clone https://github.com/MaraganiV/Soulpage-genai-assignment-vyshnavi.git

**Navigate to the Project Directory**
cd Soulpage-genai-assignment-yourfriendname

**Install Required Packages**
pip install -r requirements.txt

**Run the Project**
Open the notebook file and execute the cells to observe how the agents interact and generate the analysis.

**Example Output**
Movie: Leo  
Rating: 7.5/10  
Box Office: ₹600 Cr  
Insight: The film performed strongly at the box office while receiving mixed critical reviews.

**TASK2**
**Intelligent Knowledge Assistant Bot**
**Project Description**
The Intelligent Knowledge Assistant Bot is a command line based conversational application designed to deliver quick and reliable information to users. The bot retrieves data from Wikipedia and generates concise summaries, enabling users to understand topics without searching manually.

This project highlights the implementation of conversational AI with memory awareness, allowing the bot to reference previous interactions for improved response relevance.

**Objective**

The purpose of this project is to build a smart assistant capable of:

Understanding user queries

Fetching factual information

Maintaining basic conversation context

Delivering summarized responses

It demonstrates practical skills in Python development and information retrieval systems.

**Core Functionalities**
**Real Time Query Handling**

Users can ask questions directly in the terminal, and the bot instantly returns summarized knowledge.

**Context Retention**

The system stores recent conversation inputs to enhance follow up responses.

**Automated Summarization**

Instead of displaying lengthy articles, the bot extracts key points and presents them clearly.

**Fault Tolerance**

If the requested information is unavailable, the bot gracefully informs the user rather than crashing.

**Technology Stack**
Python

Wikipedia Library

Command Line Interface

**Installation Guide**
**Clone the Repository**
git clone https://github.com/MaraganiV/Soulpage-genai-assignment-vyshnavi.git


**Move to Project Directory**
cd Task2_Context_Aware_Knowledge_Bot

**Install Required Packages**
pip install -r requirements.txt

**Running the Application**

Execute the following command:

python knowledgeBot.py


Once started, the assistant will prompt you to enter a question.

**Example queries:**

What is Artificial Intelligence?
Who invented the telephone?
Explain cloud computing.


To terminate the program, type:

exit


