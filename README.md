# AI Agent

This project implements an AI agent that can interact with various tools (such as listing files, reading file contents, running Python files, and writing to files) and iteratively improve its responses based on feedback from previous iterations. The agent uses OpenAI’s Gemini API (or another similar LLM API) to generate responses and interact with the tools.

## Features
- **Iterative Functionality**: The agent can call functions like `get_files_info`, `get_file_content`, `run_python_file`, and `write_file` based on its analysis.
- **Feedback Loop**: The agent maintains a conversation where each response is based on the previous outputs, making it capable of continuously iterating on its work.
- **Verbose Mode**: The agent can provide detailed output for debugging and tracking the actions it takes.

## Installation

### Prerequisites

- Python 3.12 or higher
- `pip` (Python package manager)

### Steps

1. Clone the repository:
<pre> 
   ```bash
   git clone <repository-url>
   cd <repository-folder>
</pre>
2. Create a virtual environment (optional but recommended):
<pre>
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
</pre>
3. Install the required dependencies:
<pre>
pip install -r requirements.txt
</pre>
4. Set up environment variables:
<pre>
Copy the .env.example file and rename it to .env.
Add your API key and any other required configuration.
</pre> 
Example .env file:
<pre>
GEMINI_API_KEY=<Your_Gemini_API_Key>
WORK_DIR = "./calculator"
MAX_CHARS = 10000
MAX_ITERATIONS = 20
</pre>
### Basic Command
To start the AI agent, run the following command in the terminal:
<pre>python3 main.py "Your prompt here"</pre>
### Verbose Mode
If you want to see detailed outputs about the agent's actions (e.g., function calls, token counts), use the --verbose flag:
<pre> python3 main.py "How do I fix the bug in the calculator?" --verbose</pre>
Exit Criteria
The agent will iterate up to MAX_ITERATIONS (configured in config.py). If no progress is made (i.e., no new function calls or content added), the agent will terminate early. You can modify MAX_ITERATIONS in the config.py file to change the number of iterations.

How It Works
Initial Prompt: The user provides a prompt to the agent (e.g., "How do I fix the bug in the calculator?").

Function Calls: The agent will iterate on the conversation, calling available functions such as:

get_files_info: List files in the working directory.

get_file_content: Read content from a file.

run_python_file: Execute Python files.

write_file: Write to a file.

Iterative Feedback: After each function call, the results are appended to the conversation, and the model continues reasoning based on this new information.

Stop Conditions: The loop stops after MAX_ITERATIONS or when the conversation is marked as complete.

### File Structure:
<pre>
your-project-folder/
├── .env.example            # Example environment variables file
├── .env                    # Actual environment variables file 
├── main.py                 # Main program file
├── requirements.txt        # Dependencies file
├── functions/
│   └── call_function.py    # function definition
│   └── get_file_content.py # function definition
│   └── get_files_info.py   # function definitions
│   └── run_python_file.py  # function definitions
│   └── write_file          # function definitions

├── config.py               # Configuration file relevant variables
└── prompt.py               # System prompt 
</pre>