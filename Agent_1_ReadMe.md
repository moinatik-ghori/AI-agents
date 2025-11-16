# Agent 1 - OpenAI Chat Completion Basics

## Overview

Agent 1 is a beginner-friendly introduction to building AI agents that interact with OpenAI's API. This program demonstrates fundamental concepts of AI agent development by performing three sequential tasks:

1. **Simple Q&A**: Asks a basic factual question and receives an answer
2. **Question Generation**: Requests the AI to create a challenging IQ test question
3. **Question Answering**: Asks the AI to answer the question it just generated

This program serves as an excellent starting point for understanding how to build AI agents that can have conversations with OpenAI's language models, making it perfect for learning the basics of AI agent development.

## How It Works

The program:
- Loads environment variables securely from a `.env` file
- Creates an OpenAI client instance for API communication
- Makes three sequential API calls to demonstrate different interaction patterns
- Shows how to format messages, extract responses, and chain AI interactions
- Demonstrates both simple queries and creative generation tasks

## Setup Instructions

> **Note**: Before running this agent, make sure you've completed the Prerequisites section in the main [README.md](README.md) file, including installing UV, dependencies, and setting up your OpenAI API key.

### Step 1: Verify Your Setup

Make sure your project structure looks like this:

```
AI-agents/
├── .env                    # Your API key (not in git)
├── pyproject.toml          # Project dependencies
├── uv.lock                 # Locked dependency versions
├── Agent_1_ReadMe.md       # This file
└── Agent_1.py              # The program
```

### Step 2: Run the Program

**Using UV (Recommended):**
```bash
uv run python Agent_1.py
```

**Using Standard Python:**
```bash
python Agent_1.py
```

The program will:
1. Load environment variables from the `.env` file
2. Validate the OpenAI API key
3. Create an OpenAI client instance
4. Execute three sequential AI interactions
5. Display the results in the terminal

You'll see output like:
```
OPENAI_API_KEY is set
Paris
Question: If a train leaves Station A at 60 mph and another train leaves Station B at 80 mph, and they are 280 miles apart, how long until they meet if they're traveling toward each other?

Answer: To solve this problem, we need to find when the two trains meet. Since they're traveling toward each other, their speeds add up: 60 mph + 80 mph = 140 mph. The distance between them is 280 miles. Time = Distance / Speed, so Time = 280 miles / 140 mph = 2 hours. Therefore, the trains will meet in 2 hours.
```

## Program Flow

The program executes in the following sequence:

### Phase 1: Initialization
1. **Load Environment Variables**: Reads the `.env` file to get the API key
2. **Validate API Key**: Checks if the key exists, raises an error if missing
3. **Create OpenAI Client**: Establishes connection to OpenAI's API

### Phase 2: Simple Question
4. **Ask a Question**: Sends "What is the capital of France?" to the AI
5. **Display Answer**: Prints the AI's response (e.g., "Paris")

### Phase 3: Question Generation
6. **Request Question Creation**: Asks the AI to generate a challenging IQ test question
7. **Extract Generated Question**: Saves the AI's generated question
8. **Display Question**: Prints the generated question

### Phase 4: Question Answering
9. **Ask for Answer**: Sends the generated question back to the AI
10. **Extract Answer**: Gets the AI's solution/explanation
11. **Display Answer**: Prints how the AI solved its own question

## Use Cases and Learning Applications

This program demonstrates fundamental concepts that can be applied in various ways:

### 1. **Learning AI Agent Basics**
- **Understanding API calls**: Learn how to structure requests to OpenAI's API
- **Message formatting**: Understand the role-based message structure
- **Response extraction**: Learn how to parse API responses
- **Example modifications**:
  - Change the initial question to test different query types
  - Modify the question generation prompt to create different types of questions
  - Experiment with different models

### 2. **Building Foundation for Complex Agents**
- **Sequential interactions**: Understand how to chain multiple AI calls
- **Variable management**: Learn how to store and reuse AI responses
- **Error handling**: See how to validate inputs before API calls
- **Example extensions**:
  - Add conversation history to maintain context
  - Implement retry logic for failed API calls
  - Add logging for debugging

### 3. **Educational Demonstrations**
- **Teaching AI concepts**: Use as a teaching tool for AI agent development
- **Code walkthrough**: Study the detailed comments to understand each step
- **Experimentation**: Modify the code to see how changes affect behavior
- **Example experiments**:
  - Try different models (gpt-4, gpt-3.5-turbo)
  - Change temperature settings for more creative responses
  - Add system prompts to guide AI behavior

### 4. **Prototyping and Testing**
- **Quick testing**: Use as a template for testing OpenAI API functionality
- **Model comparison**: Test different models with the same prompts
- **Cost estimation**: Understand API usage patterns
- **Example uses**:
  - Test new OpenAI features
  - Benchmark response times
  - Estimate API costs

### 5. **Building Custom Applications**
- **Template for chatbots**: Use as a starting point for custom chatbots
- **Question-answer systems**: Adapt for FAQ systems or knowledge bases
- **Content generation**: Modify for creative writing or content generation
- **Example adaptations**:
  - Create a trivia game generator
  - Build a study question generator
  - Develop a creative writing assistant

## Program Structure

```
AI-agents/
├── .env                    # Your API key (not in git)
├── pyproject.toml          # Project dependencies
├── uv.lock                 # Locked dependency versions
├── Agent_1_ReadMe.md       # This file
└── Agent_1.py              # The program
```

## Key Concepts Explained

> **Note**: For common concepts like Environment Variables, OpenAI Client, Message Format, API Response Structure, Error Handling, Model Selection, and String Formatting, see the [Important Concepts Explained](README.md#important-concepts-explained) section in the main README.md file.

### 1. **Chaining AI Interactions**

**What is chaining?**
Chaining means using the output of one AI call as input to the next call. In this program, we:
1. Ask the AI to generate a question
2. Use that generated question as input for the next call
3. Ask the AI to answer its own question

**How it works:**
```python
# First call: Generate question
response = openai_client.chat.completions.create(...)
question = response.choices[0].message.content

# Second call: Answer the question
message = [{"role": "user", "content": question}]
response = openai_client.chat.completions.create(...)
answer = response.choices[0].message.content
```

**Why it's useful:**
- Demonstrates how to build complex workflows
- Shows how AI can build upon its own outputs
- Enables multi-step problem solving

### 2. **Variable Reuse and Overwriting**

**What happens in this program?**
The program reuses the `question` variable:
1. First, it stores the prompt to generate a question
2. Then, it overwrites it with the AI-generated question

**Example:**
```python
question = "Please propose a hard question..."  # Original prompt
# ... API call ...
question = response.choices[0].message.content  # Overwritten with AI response
```

**Why this pattern?**
- Saves memory by reusing variables
- Keeps code simple and readable
- Demonstrates variable lifecycle

### 3. **Sequential Execution**

**What is sequential execution?**
The program runs steps one after another, waiting for each to complete before starting the next.

**Flow:**
1. Initialize → 2. Ask question → 3. Generate question → 4. Answer question

**Why this matters:**
- Each step depends on the previous one
- Demonstrates synchronous programming
- Shows how to build step-by-step workflows

## Troubleshooting

### Error: "OPENAI_API_KEY is not set" or "ValueError: OPENAI_API_KEY is not set"
- **Solution**: See the Prerequisites section in the main [README.md](README.md) file for setting up your API key.

### Error: "ModuleNotFoundError"
- **Solution**: See the Prerequisites section in the main [README.md](README.md) file for installing dependencies.

### Error: API authentication failed
- **Solution**:
  1. Verify your API key is correct
  2. Check that your OpenAI account has credits/usage available
  3. Ensure you haven't exceeded rate limits
  4. Wait a few minutes and try again

### Error: "ValueError: OPENAI_API_KEY is not set"
- **Solution**: 
  1. Make sure your `.env` file exists in the project root
  2. Verify the file contains: `OPENAI_API_KEY=your_actual_key`
  3. Check that the file is named exactly `.env` (with the dot, no extension)

### Program runs but produces no output
- **Solution**:
  1. Check your internet connection
  2. Verify your OpenAI account has available credits
  3. Check the terminal for any error messages
  4. Ensure you're running the program from the correct directory

## Advanced Customization

### Changing the AI Model

Edit the `model` parameter in `Agent_1.py`:
```python
# Line 56, 84, or 109
model="gpt-4o"  # More capable but more expensive
# or
model="gpt-3.5-turbo"  # Faster and cheaper
```

### Modifying the Initial Question

Change line 48 in `Agent_1.py`:
```python
message = [{"role": "user", "content": "Your custom question here"}]
```

### Customizing the Question Generation Prompt

Modify line 71 in `Agent_1.py`:
```python
question = "Your custom prompt for question generation"
```

### Adding System Prompts

You can add a system message to guide the AI's behavior:
```python
message = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"}
]
```

### Adding Temperature Control

Control the creativity/randomness of responses:
```python
response = openai_client.chat.completions.create(
    model="gpt-4o-mini",
    messages=message,
    temperature=0.7  # Range: 0.0 (deterministic) to 2.0 (creative)
)
```

### Adding Conversation History

Maintain context across multiple calls:
```python
conversation = [{"role": "user", "content": "Hello"}]
response = openai_client.chat.completions.create(...)
conversation.append({"role": "assistant", "content": response.choices[0].message.content})
conversation.append({"role": "user", "content": "Tell me more"})
```

## Best Practices

1. **Keep your `.env` file secure**: Never commit it to version control
2. **Validate inputs**: Always check for required values before use
3. **Handle errors gracefully**: Add try-except blocks for API calls
4. **Monitor API usage**: Keep track of costs, especially with high traffic
5. **Use appropriate models**: Choose models based on your needs (cost vs. capability)
6. **Add logging**: Log API calls for debugging and monitoring
7. **Test thoroughly**: Test with various inputs to ensure reliability
8. **Document your code**: Add comments explaining complex logic

## Next Steps

After understanding this program, you can:

- **Add error handling**: Wrap API calls in try-except blocks
- **Implement conversation history**: Maintain context across multiple interactions
- **Experiment with different models**: Compare capabilities and costs
- **Add system prompts**: Guide the AI's behavior and personality
- **Create interactive versions**: Build command-line or web interfaces
- **Add logging**: Track API usage and debug issues
- **Implement retry logic**: Handle temporary API failures
- **Build more complex agents**: Create multi-agent systems or specialized assistants
- **Add streaming responses**: Show responses as they're generated
- **Integrate with other services**: Connect to databases, APIs, or file systems

## Additional Resources

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [OpenAI Python Library](https://github.com/openai/openai-python)
- [Python-dotenv Documentation](https://pypi.org/project/python-dotenv/)
- [UV Package Manager](https://github.com/astral-sh/uv)
- [OpenAI Models Overview](https://platform.openai.com/docs/models)

## License

This is an educational example. Make sure to follow OpenAI's usage policies when building applications.
