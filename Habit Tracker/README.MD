📊 Coding Tracker using Pixela API
This Python script automates tracking daily coding hours using the Pixela API. It allows users to:
✅ Create a Pixela user account (if not already created)
✅ Set up a graph to track coding hours
✅ Log daily coding hours as pixels on the graph

🔧 Requirements
Python 3.x
requests library (install using pip install requests)
A Pixela account (automatically created by the script)
📌 Setup & Usage
1️⃣ Set Up Environment Variables
Before running the script, set your Pixela token as an environment variable:

Windows (Command Prompt):
set token=your_secret_token

Mac/Linux (Terminal):
export token=your_secret_token
Alternatively, you can directly replace os.getenv("token") with your token in the script, but storing sensitive data in code is not recommended.

2️⃣ Run the Script
python script.py
If running for the first time, it will create a Pixela user and set up a coding graph.
Enter how many hours you coded today when prompted.
🔗 API Endpoints Used
User Creation: https://pixe.la/v1/users
Graph Creation: https://pixe.la/v1/users/{USERNAME}/graphs
Pixel (Daily Log) Creation: https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}

