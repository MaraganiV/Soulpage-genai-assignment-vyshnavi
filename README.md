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
