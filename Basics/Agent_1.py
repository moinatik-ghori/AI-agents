# Import the load_dotenv function from the dotenv module
# This function helps us load environment variables from a .env file
# Think of it as a way to securely store sensitive information like API keys
from dotenv import load_dotenv

# Import the OpenAI class from the openai module
# This class is the main interface we'll use to communicate with OpenAI's API
# It's like getting a special tool that knows how to talk to OpenAI's servers
from openai import OpenAI

# Import the os module, which provides functions for interacting with the operating system
# We'll use it to read environment variables that we loaded from the .env file
import os


# Call load_dotenv() to load environment variables from a .env file in the current directory
# The override=True parameter means: if an environment variable already exists,
# replace it with the value from the .env file
# This is like opening a secret file and reading all the passwords/keys stored in it
load_dotenv(override=True)

# Use os.getenv() to retrieve the value of the OPENAI_API_KEY environment variable
# This reads the API key that was loaded from the .env file
# Think of this as looking up a specific key from our secret storage
openai_api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key was found (if it's None, that means it wasn't set)
# This is a safety check to make sure we have the key before trying to use it
if openai_api_key is None:
    # If the key is missing, raise an error to stop the program
    # This prevents the program from running without proper authentication
    # It's like checking if you have your house key before trying to unlock the door
    raise ValueError("OPENAI_API_KEY is not set")
else:
    # If the key exists, print a confirmation message
    # This lets us know that everything is set up correctly
    print("OPENAI_API_KEY is set")

# Create an instance of the OpenAI client using our API key
# This client object is what we'll use to make requests to OpenAI's API
# Think of it as establishing a connection to OpenAI's servers with our credentials
openai_client = OpenAI(api_key=openai_api_key)

# Create a message list containing a single message dictionary
# The "role": "user" tells OpenAI this is a message from the user (not the assistant)
# The "content" contains the actual question we want to ask
# This is the format OpenAI expects for chat conversations - a list of message dictionaries
message = [{"role": "user", "content": "What is the capital of France?"}]

# Make a request to OpenAI's API to generate a chat completion
# chat.completions.create() sends our message to OpenAI and asks for a response
# We specify the model "gpt-4o-mini" (a smaller, faster version of GPT-4)
# We pass our message list so OpenAI knows what conversation we're having
# This is like sending a letter to OpenAI and asking them to write back
response = openai_client.chat.completions.create(
    model="gpt-4o-mini",  # Which AI model to use for generating the response
    messages=message      # The conversation history (our question)
)

# Extract and print the actual text content from the AI's response
# response.choices[0] gets the first (and usually only) response option
# .message.content gets the text content of that message
# This is like opening the letter from OpenAI and reading what they wrote
print(response.choices[0].message.content)

# Create a string variable containing our request to the AI
# We're asking the AI to generate a challenging IQ test question
# The instruction "Respond only with the question" tells the AI to give us just the question,
# not any explanation or additional text
# This is like giving the AI a job: "Create a hard question for me"
question = "Please propose a hard, challenging question to assess someone's IQ. Respond only with the question."

# Create a new message list with our request
# We're formatting it the same way as before: a list with a dictionary containing "role" and "content"
# The "role": "user" means this message is coming from us (the user)
# We're putting our question string into the "content" field
message = [{"role": "user", "content": question}]

# Make our first API call to ask the AI to generate an IQ question
# We're using the same client and model as before
# This time, instead of asking a simple factual question, we're asking the AI to be creative
# and generate a challenging question for us
response = openai_client.chat.completions.create(
    model="gpt-4o-mini",  # Using the same efficient model
    messages=message      # Sending our request to generate a question
)

# Extract the AI's response and store it in the question variable
# Notice we're overwriting the question variable - now it contains the AI-generated question
# instead of our original request
# This is like: we asked for a question, and now we're saving the question the AI gave us
question = response.choices[0].message.content

# Print the AI-generated question with a label
# The f"..." is an f-string (formatted string) that lets us insert variables into text
# {question} gets replaced with the actual question text
# This shows us what challenging question the AI created
print(f"Question: {question}")

# Create a new message list, but this time we're using the AI-generated question
# We're asking the AI to answer the question it just created
# This is like taking the question the AI gave us and asking it back to the AI
message = [{"role": "user", "content": question}]

# Make a second API call, this time asking the AI to answer the question it generated
# This creates an interesting scenario: the AI is answering its own question
# It's like asking someone to create a puzzle, then immediately asking them to solve it
response = openai_client.chat.completions.create(
    model="gpt-4o-mini",  # Same model for consistency
    messages=message      # The AI-generated question we want answered
)

# Extract the AI's answer to the question
# Store it in a variable called "answer" so we can use it later
# This contains the solution or explanation to the challenging question
answer = response.choices[0].message.content

# Print the answer with a label
# Using an f-string again to format the output nicely
# This shows us how the AI solved or answered the question it created
print(f"Answer: {answer}")
