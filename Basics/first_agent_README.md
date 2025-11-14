# First AI Agent - OpenAI Chat Completion

## Overview

This program demonstrates how to interact with OpenAI's API using Python. It performs three main tasks:
1. **Simple Q&A**: Asks a basic factual question and gets an answer
2. **Question Generation**: Asks the AI to create a challenging IQ test question
3. **Question Answering**: Asks the AI to answer the question it just generated

This is a beginner-friendly introduction to building AI agents that can have conversations with OpenAI's language models.

## What This Program Teaches

- How to securely manage API keys using environment variables
- How to set up and use the OpenAI Python client
- How to format messages for the Chat Completions API
- How to make API calls and extract responses
- How to chain multiple AI interactions together

## Prerequisites

Before running this program, you need:

1. **Python 3.12 or higher** - Check your version with `python --version`
2. **OpenAI API Key** - Get one from [OpenAI's website](https://platform.openai.com/api-keys)
3. **Required Python packages**:
   - `python-dotenv` - For loading environment variables
   - `openai` - The official OpenAI Python library

## Setup Instructions

### Step 1: Install Dependencies

Install the required packages using pip:

```bash
pip install python-dotenv openai
```

Or if you're using the project's dependency management:

```bash
pip install -e .
```

### Step 2: Create a `.env` File

Create a file named `.env` in the root of your project (same directory as `pyproject.toml`). Add your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

**Important Security Notes:**
- Never commit your `.env` file to version control
- Replace `your_api_key_here` with your actual API key
- Keep your API key secret and don't share it

### Step 3: Verify Your Setup

Make sure your project structure looks like this:

```
AI-agents/
├── .env                    # Your API key (not in git)
├── pyproject.toml          # Project dependencies
└── Basics/
    ├── README.md          # This file
    └── first_agent.py     # The program
```

## How to Run

Navigate to the project root directory and run:

```bash
python Basics/first_agent.py
```

Or from the Basics directory:

```bash
cd Basics
python first_agent.py
```

## Program Flow

The program executes in the following sequence:

### Phase 1: Initialization
1. **Load Environment Variables**: Reads the `.env` file to get the API key
2. **Validate API Key**: Checks if the key exists, stops if missing
3. **Create OpenAI Client**: Establishes connection to OpenAI's API

### Phase 2: Simple Question
4. **Ask a Question**: Sends "What is the capital of France?" to the AI
5. **Display Answer**: Prints the AI's response

### Phase 3: Question Generation
6. **Request Question Creation**: Asks the AI to generate a challenging IQ test question
7. **Extract Generated Question**: Saves the AI's generated question
8. **Display Question**: Prints the generated question

### Phase 4: Question Answering
9. **Ask for Answer**: Sends the generated question back to the AI
10. **Extract Answer**: Gets the AI's solution/explanation
11. **Display Answer**: Prints how the AI solved its own question

## Key Concepts Explained

### Environment Variables
Environment variables are a secure way to store sensitive information like API keys. The `.env` file keeps your keys separate from your code, preventing accidental exposure.

### Message Format
OpenAI's Chat API expects messages in a specific format:
```python
[
    {"role": "user", "content": "Your question here"}
]
```
- `role`: Either "user" (your message) or "assistant" (AI's message)
- `content`: The actual text of the message

### API Response Structure
When you make an API call, you get back a response object:
```python
response.choices[0].message.content
```
- `choices[0]`: The first (usually only) response option
- `message.content`: The actual text content of the response

### Model Selection
The program uses `gpt-4o-mini`, which is:
- A smaller, faster version of GPT-4
- More cost-effective for simple tasks
- Still very capable for most use cases

## Example Output

When you run the program, you should see something like:

```
OPENAI_API_KEY is set
Paris
Question: If a train leaves Station A at 60 mph and another train leaves Station B at 80 mph, and they are 280 miles apart, how long until they meet if they're traveling toward each other?

Answer: To solve this problem, we need to find when the two trains meet. Since they're traveling toward each other, their speeds add up: 60 mph + 80 mph = 140 mph. The distance between them is 280 miles. Time = Distance / Speed, so Time = 280 miles / 140 mph = 2 hours. Therefore, the trains will meet in 2 hours.
```

## Understanding the Code Structure

### Import Section
```python
from dotenv import load_dotenv  # For loading .env file
from openai import OpenAI        # OpenAI API client
import os                        # For reading environment variables
```

### Configuration Section
- Loads and validates the API key
- Creates the OpenAI client instance

### Interaction Sections
Each interaction follows the same pattern:
1. Create a message in the correct format
2. Call the API with `chat.completions.create()`
3. Extract the response content
4. Display or use the result

## Troubleshooting

### Error: "OPENAI_API_KEY is not set"
- Make sure you created a `.env` file in the project root
- Verify the file contains: `OPENAI_API_KEY=your_actual_key`
- Check that the file is named exactly `.env` (with the dot)

### Error: "ModuleNotFoundError: No module named 'dotenv'"
- Install the package: `pip install python-dotenv`

### Error: "ModuleNotFoundError: No module named 'openai'"
- Install the package: `pip install openai`

### Error: API authentication failed
- Verify your API key is correct
- Check that your OpenAI account has credits/usage available
- Ensure you haven't exceeded rate limits

## Next Steps

After understanding this program, you can:
- Modify the questions to ask different things
- Add conversation history to maintain context
- Experiment with different models (gpt-4, gpt-3.5-turbo, etc.)
- Add error handling for network issues
- Create more complex agent workflows

## Additional Resources

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [OpenAI Python Library](https://github.com/openai/openai-python)
- [python-dotenv Documentation](https://pypi.org/project/python-dotenv/)

## License

This is an educational example. Make sure to follow OpenAI's usage policies when building applications.

