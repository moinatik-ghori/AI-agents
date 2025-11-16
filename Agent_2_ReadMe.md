# Agent 2 - Personal AI Assistant Chatbot

## Overview

Agent 2 is an intelligent chatbot application that creates a **personal AI assistant** capable of answering questions about a professional's background, experience, skills, and projects. The chatbot uses a LinkedIn profile (in PDF format) and a comprehensive summary to provide accurate, professional responses about the person it represents.

This program demonstrates how to build an interactive AI agent that can act as a digital representative, making it perfect for networking, interviews, client interactions, and professional presentations.

## How It Works

The program:
- Reads a LinkedIn profile from a PDF file
- Loads a comprehensive summary about the person
- Creates a system prompt that instructs the AI to act as the person's professional representative
- Launches an interactive web-based chatbot interface
- Answers questions using only the provided information (LinkedIn PDF + summary)

## Setup Instructions

> **Note**: Before running this agent, make sure you've completed the Prerequisites section in the main [README.md](README.md) file, including installing UV, dependencies, and setting up your OpenAI API key.

### Step 1: Prepare Your Files

#### Getting a PDF Version of Your LinkedIn Profile

**Method 1: Using LinkedIn's Export Feature**
1. Log in to your LinkedIn account
2. Go to **Settings & Privacy** → **Data Privacy** → **Get a copy of your data**
3. Select "Want something in particular? Select the data files you're most interested in"
4. Choose "Posts" or "Connections" (this will include your profile)
5. Click "Request archive"
6. Wait for the email with your data (may take a few minutes to hours)
7. Download and extract the archive
8. Find your profile information and convert it to PDF if needed

**Method 2: Print to PDF (Easier Method)**
1. Go to your LinkedIn profile page
2. Press `Ctrl+P` (Windows) or `Cmd+P` (Mac) to open print dialog
3. Select "Save as PDF" or "Microsoft Print to PDF" as the printer
4. Save the file with a descriptive name (e.g., `YourName_LinkedIn.pdf`)
5. Place this file in the `files/` folder

**Method 3: Using Browser Extensions**
- Use browser extensions like "Print Friendly & PDF" or "Save as PDF"
- Navigate to your LinkedIn profile
- Use the extension to save the page as PDF

#### Creating a Summary File

1. Create a text file named `summary.txt` in the `files/` folder
2. Write a comprehensive summary about the person, including:
   - Professional background and experience
   - Key skills and expertise
   - Notable projects and achievements
   - Education and certifications
   - Career highlights
   - Any other relevant professional information

**Example summary.txt content:**
```
John Doe is a Senior Software Engineer with 8 years of experience in full-stack development. 
He specializes in Python, JavaScript, and cloud technologies. John has led multiple successful 
projects including a microservices architecture migration that improved system performance by 40%. 
He holds a Master's degree in Computer Science from MIT and is AWS certified. His expertise 
includes machine learning, API design, and DevOps practices.
```

### Step 2: Update the Code (Optional)

If you want to customize the person's name, edit `Agent_2.py` and change line 43:
```python
name = "Your Name Here"
```

Also, make sure the file paths match your setup:
- PDF file path: `files/YourName_LinkedIn.pdf.pdf` (line 29)
- Summary file path: `files/summary.txt` (line 38)

### Step 3: Run the Program

**Using UV (Recommended):**
```bash
uv run python Agent_2.py
```

**Using Standard Python:**
```bash
python Agent_2.py
```

The program will:
1. Check for the OpenAI API key
2. Load and extract text from the LinkedIn PDF
3. Load the summary file
4. Create the system prompt
5. Launch a Gradio web interface

You'll see output like:
```
OpenAI API key is set
Running on local URL:  http://127.0.0.1:7860
```

Open the URL in your browser to start chatting!

## Use Cases and Leveraging the Tool

This AI assistant can be leveraged in multiple powerful ways:

### 1. **Job Interview Preparation**
- **Practice answering questions**: Ask the chatbot common interview questions about your background
- **Review your experience**: Get reminded of your key projects and achievements
- **Prepare talking points**: Ask "What should I mention when asked about my Python experience?"
- **Example questions to ask**:
  - "Tell me about my most significant project"
  - "What are my key strengths in software development?"
  - "How should I explain my career transition?"

### 2. **Client Presentations and Pitches**
- **Quick reference**: During client calls, quickly ask about your relevant experience
- **Consistency**: Ensure you present the same information consistently
- **Example questions**:
  - "What projects have I completed in the healthcare industry?"
  - "What are my credentials in cloud architecture?"
  - "Summarize my experience with enterprise clients"

### 3. **Networking Events**
- **Elevator pitch**: Ask "Give me a 30-second introduction about myself"
- **Relevant experience**: "What should I mention when networking with data scientists?"
- **Example questions**:
  - "Create a brief introduction highlighting my AI/ML experience"
  - "What are my most impressive achievements to mention?"

### 4. **Recruiter Interactions**
- **Automated responses**: Share the chatbot link with recruiters for initial screening
- **Consistent information**: Ensure recruiters get accurate details
- **Example questions**:
  - "What is my current role and responsibilities?"
  - "What technologies am I proficient in?"
  - "What is my educational background?"

### 5. **Project Discussions**
- **Project details**: Get specific information about past projects
- **Technical stack**: Remember what technologies you used
- **Example questions**:
  - "Tell me about my e-commerce platform project"
  - "What technologies did I use in my machine learning project?"
  - "What were the key challenges I solved in Project X?"

### 6. **Self-Assessment and Career Planning**
- **Skill inventory**: "What are all my technical skills?"
- **Career progression**: "How has my career evolved over the years?"
- **Gap analysis**: "What areas should I focus on for career growth?"

### 7. **Resume and Cover Letter Writing**
- **Content generation**: "Give me bullet points for my resume about my Python experience"
- **Tailored responses**: "How should I describe my experience for a DevOps role?"
- **Example questions**:
  - "Create a professional summary for my resume"
  - "What achievements should I highlight for a senior developer position?"

### 8. **Team Introductions**
- **Onboarding**: New team members can learn about you quickly
- **Collaboration**: Help colleagues understand your expertise
- **Example questions**:
  - "Give me a brief professional introduction"
  - "What should my team know about my background?"

## Program Structure

```
AI-agents/
├── .env                          # Your OpenAI API key (not in git)
├── pyproject.toml                # Project dependencies
├── uv.lock                       # Locked dependency versions
├── Agent_2.py                    # Main program
├── Agent_2_ReadMe.md             # This file
└── files/
    ├── YourName_LinkedIn.pdf.pdf  # LinkedIn profile PDF
    └── summary.txt                # Professional summary
```

## Key Concepts Explained

> **Note**: For common concepts like Environment Variables, OpenAI Client, Message Format, API Response Structure, Error Handling, Model Selection, and String Formatting, see the [Important Concepts Explained](README.md#important-concepts-explained) section in the main README.md file.

### 1. **System Prompts**

**What is a system prompt?**
A system prompt is a special message that sets the context and behavior for the AI. It tells the AI "who" it should be and "how" it should respond.

**In this program:**
The system prompt:
- Defines the AI's role (professional representative)
- Sets the tone (professional, articulate)
- Provides the knowledge base (LinkedIn PDF + summary)
- Sets constraints (only use provided information)

**Why it matters:**
Without a good system prompt, the AI might:
- Make up information
- Respond in the wrong tone
- Not understand its purpose

### 2. **PDF Text Extraction**

**What is PDF extraction?**
PDFs contain text, but it's encoded in a special format. We need to extract the readable text from the PDF file.

**How it works:**
```python
reader = PdfReader("file.pdf")  # Open PDF
for page in reader.pages:        # Loop through pages
    text += page.extract_text()  # Extract text from each page
```

**Why it's needed:**
- PDFs are not plain text files
- The AI needs text to understand the content
- We convert the PDF into a string the AI can process

### 3. **Conversation History**

**What is conversation history?**
The `history` parameter in the `chat()` function contains previous messages, allowing the AI to maintain context across the conversation. This enables multi-turn conversations where the AI remembers what was discussed earlier.

**How it works:**
```python
def chat(message, history):
    messages = [{"role": "system", "content": system_prompt}] + history + [{"role": "user", "content": message}]
    # history contains previous user/assistant message pairs
```

**Why it's important:**
- Maintains context across multiple interactions
- Enables natural conversation flow
- Allows follow-up questions and clarifications

### 4. **Gradio Interface**

**What is Gradio?**
Gradio is a Python library that quickly creates web interfaces for machine learning models and AI applications.

**How it works:**
```python
gr.ChatInterface(chat, title="AI Assistant").launch()
```

**What it does:**
- Creates a web-based chat interface
- Handles user input and displays responses
- Manages conversation history automatically
- Provides a shareable URL

**Benefits:**
- No HTML/CSS/JavaScript needed
- Quick prototyping
- Easy to share and test
- Professional-looking interface

### 5. **Function Design: The `chat()` Function**

**What does it do?**
The `chat()` function is called every time the user sends a message. It:
1. Combines the system prompt, history, and new message
2. Sends the request to OpenAI
3. Returns the AI's response

**Why this design?**
- **Separation of concerns**: Chat logic is separate from UI
- **Reusability**: The function can be used in different interfaces
- **Testability**: Easy to test the chat logic independently

### 6. **File I/O (Input/Output)**

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

### Error: "openai is not defined" or "ModuleNotFoundError"
- **Solution**: See the Prerequisites section in the main [README.md](README.md) file for installing dependencies.

### Error: "OpenAI API key is not set"
- **Solution**: See the Prerequisites section in the main [README.md](README.md) file for setting up your API key.

### Error: "FileNotFoundError" for PDF or summary
- **Solution**: 
  1. Check that files exist in `files/` folder
  2. Verify file names match exactly (case-sensitive)
  3. Update file paths in `Agent_2.py` if needed


### Gradio interface not opening
- **Solution**: 
  1. Check the terminal for the local URL
  2. Make sure no firewall is blocking the port (usually 7860)
  3. Try accessing `http://127.0.0.1:7860` directly

### API Rate Limits or Authentication Errors
- **Solution**:
  1. Verify your API key is correct
  2. Check your OpenAI account has credits
  3. Ensure you haven't exceeded rate limits
  4. Wait a few minutes and try again

## Advanced Customization

### Changing the AI Model
Edit line 15 in `Agent_2.py`:
```python
model="gpt-4o"  # More capable but more expensive
# or
model="gpt-3.5-turbo"  # Faster and cheaper
```

### Customizing the System Prompt
Modify the `system_prompt` variable (lines 45-58) to change:
- The AI's personality
- Response style
- Information constraints
- Additional instructions

### Adding More Context
You can add more files to the knowledge base:
```python
# Load additional files
with open("files/projects.txt", "r") as f:
    projects = f.read()

system_prompt += f"\n\n## Projects:\n{projects}\n"
```

## Best Practices

1. **Keep your `.env` file secure**: Never commit it to version control
2. **Update summaries regularly**: Keep the summary file current with your latest achievements
3. **Test with various questions**: Ensure the chatbot handles edge cases
4. **Monitor API usage**: Keep track of costs, especially with high traffic
5. **Customize the prompt**: Tailor the system prompt to your specific needs

## Next Steps

After mastering this agent, you can:
- Add more data sources (resume, portfolio, blog posts)
- Implement conversation memory across sessions
- Add multi-language support
- Create specialized versions for different contexts (technical, business, etc.)
- Integrate with other APIs (LinkedIn API, GitHub API)
- Deploy to a cloud service for public access

## Additional Resources

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Gradio Documentation](https://www.gradio.app/docs/)
- [PyPDF Documentation](https://pypdf.readthedocs.io/)
- [UV Package Manager](https://github.com/astral-sh/uv)
- [Python-dotenv Documentation](https://pypi.org/project/python-dotenv/)

## License

This is an educational example. Make sure to follow OpenAI's usage policies and respect privacy when building applications with personal data.

