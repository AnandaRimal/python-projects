# Pixela Coding Tracker

## Introduction
This Python script uses the Pixela API to track daily coding hours. It automates the creation of a user account, a coding graph, and daily progress updates.

## Features
- **User Creation**: Registers a new Pixela user.
- **Graph Setup**: Creates a graph to track coding hours.
- **Daily Logging**: Records coding hours daily using Pixela's API.

## Requirements
- Python 3
- An active internet connection
- A Pixela account (created automatically by the script if not already registered)
- Environment variable `token` set up with your secret API token

## Installation and Setup
1. Install required packages (if not already installed):
   ```sh
   pip install requests
   ```
2. Set up an environment variable for `token`:
   ```sh
   export token="your_secret_token"
   ```
   (For Windows PowerShell, use `$env:token="your_secret_token"`)
3. Save the script as `coding_tracker.py`.

## Running the Script
Execute the script using:
```sh
python coding_tracker.py
```
It will prompt you to enter the hours you coded today and log them in your Pixela graph.

## API Endpoints Used
- **User Creation**: `https://pixe.la/v1/users`
- **Graph Creation**: `https://pixe.la/v1/users/{USERNAME}/graphs`
- **Daily Logging**: `https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}`

## Future Improvements
- Add error handling for API responses.
- Implement authentication checks before user creation.
- Automate updates without manual input.

Happy coding! 🚀

