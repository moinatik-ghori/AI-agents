# AI Agents Project

A collection of AI agent implementations demonstrating various use cases and patterns for building intelligent applications with OpenAI's API. This project serves as both a learning resource and a practical toolkit for developing AI-powered applications.

## Project Overview

This repository contains multiple AI agents, each designed to showcase different aspects of AI agent development:

### Agent 1 - OpenAI Chat Completion Basics

**Purpose**: A beginner-friendly introduction to building AI agents that interact with OpenAI's API.

**Key Features**:
- Demonstrates fundamental API interaction patterns
- Shows how to make sequential AI calls
- Illustrates question generation and answering workflows
- Perfect starting point for learning AI agent development

**What it does**:
1. Asks a simple factual question and receives an answer
2. Requests the AI to generate a challenging IQ test question
3. Asks the AI to answer the question it just generated

**Best for**: Learning the basics of OpenAI API integration, understanding message formatting, and chaining AI interactions.

**Documentation**: See [Agent_1_ReadMe.md](Agent_1_ReadMe.md) for detailed information.

---

### Agent 2 - Personal AI Assistant Chatbot

**Purpose**: An intelligent chatbot that creates a personal AI assistant capable of answering questions about a professional's background.

**Key Features**:
- Reads LinkedIn profiles from PDF files
- Uses comprehensive summaries for context
- Interactive web-based chatbot interface (Gradio)
- Acts as a digital professional representative

**What it does**:
- Extracts text from LinkedIn profile PDFs
- Loads professional summaries
- Creates a system prompt for professional representation
- Launches an interactive chatbot interface
- Answers questions using only provided information

**Best for**: Networking, interview preparation, client presentations, recruiter interactions, and professional self-representation.

**Documentation**: See [Agent_2_ReadMe.md](Agent_2_ReadMe.md) for detailed information.

---

## Prerequisites

Before running any agent in this project, you need to complete the following setup steps:

### 1. Install UV Package Manager

**UV** is a fast Python package installer and resolver written in Rust. It's the recommended way to manage dependencies for this project.

#### Installation on Windows:

**Option A: Using PowerShell (Recommended)**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Option B: Using pip**
```bash
pip install uv
```

**Option C: Using pipx**
```bash
pipx install uv
```

#### Installation on macOS/Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Verify Installation:

After installation, verify UV is working:
```bash
uv --version
```

You may need to restart your terminal or add UV to your PATH. On Windows, UV is typically installed to `%USERPROFILE%\.cargo\bin\uv.exe`.

### 2. Install Project Dependencies Using UV

Once UV is installed, navigate to the project root directory (where `pyproject.toml` is located) and run:

```bash
uv sync
```

This command will:
- Read the `pyproject.toml` file
- Install all dependencies listed in the file
- Create a virtual environment automatically
- Lock the dependency versions

**Alternative: Install dependencies in an existing environment**
```bash
uv pip install -e .
```

### 3. Set Up OpenAI API Key

**Step 1: Get Your OpenAI API Key**
1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in to your account
3. Navigate to [API Keys](https://platform.openai.com/api-keys)
4. Click "Create new secret key"
5. Copy the key (you won't be able to see it again!)

**Step 2: Create `.env` File**
1. In the project root directory (same level as `pyproject.toml`), create a file named `.env`
2. Add the following line:
   ```
   OPENAI_API_KEY=your_actual_api_key_here
   ```
3. Replace `your_actual_api_key_here` with your actual API key

**Important Security Notes:**
- Never commit the `.env` file to version control (it should be in `.gitignore`)
- Keep your API key secret and don't share it publicly
- The programs will not run without a valid API key

## Project Structure

```
AI-agents/
├── .env                          # Your OpenAI API key (not in git)
├── pyproject.toml                # Project dependencies
├── uv.lock                       # Locked dependency versions
├── README.md                     # This file
├── Agent_1.py                    # Basic OpenAI chat completion
├── Agent_1_ReadMe.md             # Agent 1 documentation
├── Agent_2.py                    # Personal AI assistant chatbot
├── Agent_2_ReadMe.md             # Agent 2 documentation
└── files/                        # Data files for agents
    ├── YourName_LinkedIn.pdf.pdf # LinkedIn profile PDF (for Agent 2)
    └── summary.txt               # Professional summary (for Agent 2)
```

## Quick Start

1. **Complete Prerequisites**: Follow the Prerequisites section above to install UV, dependencies, and set up your API key.

2. **Choose an Agent**: 
   - For beginners: Start with **Agent 1** to learn the basics
   - For interactive applications: Try **Agent 2** for a chatbot experience

3. **Run an Agent**:
   ```bash
   # Using UV (Recommended)
   uv run python Agent_1.py
   # or
   uv run python Agent_2.py
   
   # Using Standard Python
   python Agent_1.py
   # or
   python Agent_2.py
   ```

4. **Read the Documentation**: Each agent has its own detailed README file with specific setup instructions, use cases, and examples.

## Important Concepts Explained

These concepts are fundamental to understanding how all agents in this project work:

### 1. **Environment Variables and `.env` Files**

**What are they?**
Environment variables are key-value pairs that store configuration settings outside your code. The `.env` file is a special file that stores these variables.

**Why use them?**
- **Security**: Keeps sensitive data (like API keys) out of your code
- **Flexibility**: Different environments (development, production) can use different keys
- **Best Practice**: Prevents accidentally committing secrets to version control

**How it works:**
```python
from dotenv import load_dotenv
load_dotenv(override=True)  # Loads variables from .env file
openai_api_key = os.getenv("OPENAI_API_KEY")  # Read the key
```

### 2. **OpenAI Client and API Calls**

**What is the OpenAI Client?**
The `OpenAI` class is a Python client that provides a convenient interface to interact with OpenAI's API. It handles authentication, request formatting, and response parsing.

**How it works:**
```python
client = OpenAI(api_key=openai_api_key)  # Create client with your key
response = client.chat.completions.create(  # Make API call
    model="gpt-4o-mini",
    messages=messages
)
```

**Key components:**
- **Model**: The AI model to use (`gpt-4o-mini` is cost-effective and capable)
- **Messages**: A list of conversation messages with roles (system, user, assistant)
- **Response**: Contains the AI's generated text

### 3. **Message Format**

**What is the message format?**
OpenAI's Chat API expects messages in a specific structure:
```python
[
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi! How can I help?"},
    {"role": "user", "content": "What's my experience?"}
]
```

**Roles:**
- **system**: Sets the AI's behavior (sent once, at the start)
- **user**: Messages from the human
- **assistant**: Previous responses from the AI

**Why this format?**
- Allows the API to understand conversation context
- Enables multi-turn conversations
- Provides structure for the AI to process requests

### 4. **API Response Structure**

**What is the response structure?**
When you make an API call, you get back a response object with a specific structure:
```python
response.choices[0].message.content
```

**Breaking it down:**
- `response`: The complete API response object
- `choices[0]`: An array of possible responses (usually just one)
- `message`: The message object containing role and content
- `content`: The actual text content of the response

**Why this structure?**
- Allows for multiple response options (though usually just one)
- Provides metadata about the response
- Enables future features like streaming responses

### 5. **System Prompts**

**What is a system prompt?**
A system prompt is a special message that sets the context and behavior for the AI. It tells the AI "who" it should be and "how" it should respond.

**Why it matters:**
- Defines the AI's role and personality
- Sets the tone and style of responses
- Provides constraints and guidelines
- Without a good system prompt, the AI might make up information or respond inappropriately

**Example:**
```python
system_prompt = "You are a helpful assistant that provides accurate information."
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "What is Python?"}
]
```

### 6. **Error Handling and Validation**

**Why it's important:**
- Prevents runtime errors from missing configuration
- Gives clear feedback to users
- Helps with debugging and troubleshooting

**Best practices:**
- Always validate required inputs before use
- Provide clear error messages
- Handle errors gracefully

**Example:**
```python
if openai_api_key is None:
    raise ValueError("OPENAI_API_KEY is not set")
else:
    print("OPENAI_API_KEY is set")
    client = OpenAI(api_key=openai_api_key)
```

### 7. **Model Selection**

**What is a model?**
A model is a specific AI system trained by OpenAI. Different models have different capabilities, speeds, and costs.

**Common models:**
- `gpt-4o-mini`: A smaller, faster version of GPT-4, cost-effective for simple tasks
- `gpt-4o`: More capable but more expensive
- `gpt-3.5-turbo`: Faster and cheaper, less capable
- `gpt-4`: Most capable, most expensive

**Choosing a model:**
- Consider your use case (simple Q&A vs. complex reasoning)
- Balance between cost and capability
- Test different models to find the best fit

### 8. **String Formatting with f-strings**

**What are f-strings?**
F-strings (formatted string literals) allow you to embed expressions inside strings.

**Example:**
```python
name = "John"
message = f"Hello, {name}!"
# Result: "Hello, John!"
```

**Why use them?**
- Cleaner syntax than string concatenation
- More readable than format() method
- Efficient execution

### 9. **File I/O (Input/Output)**

**Reading files:**
```python
with open("file.txt", "r") as f:
    content = f.read()
```

**Why `with` statement?**
- Automatically closes the file
- Handles errors gracefully
- Best practice in Python

**File modes:**
- `"r"`: Read mode (default for text files)
- `"w"`: Write mode (overwrites existing file)
- `"a"`: Append mode (adds to existing file)

## Troubleshooting

### Error: "OPENAI_API_KEY is not set"
- **Solution**: 
  1. Create a `.env` file in the project root
  2. Add: `OPENAI_API_KEY=your_key_here`
  3. Make sure the file is named exactly `.env` (with the dot)

### Error: "ModuleNotFoundError"
- **Solution**: Install dependencies:
  ```bash
  uv sync
  ```
  Or:
  ```bash
  pip install -e .
  ```

### Error: API authentication failed
- **Solution**:
  1. Verify your API key is correct
  2. Check that your OpenAI account has credits/usage available
  3. Ensure you haven't exceeded rate limits
  4. Wait a few minutes and try again

For agent-specific troubleshooting, refer to the individual agent README files.

## Additional Resources

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [OpenAI Python Library](https://github.com/openai/openai-python)
- [Python-dotenv Documentation](https://pypi.org/project/python-dotenv/)
- [UV Package Manager](https://github.com/astral-sh/uv)
- [Gradio Documentation](https://www.gradio.app/docs/)

## License

This is an educational project. Make sure to follow OpenAI's usage policies when building applications.
