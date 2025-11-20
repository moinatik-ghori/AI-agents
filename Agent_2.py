import os 
import json
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader
from IPython.display import display, Markdown
import gradio as gr

load_dotenv(override=True)
name  = "Moinatik Ghori"

# Global variables for chat function
client = None
system_prompt = None


def validate_api_keys():
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if openai_api_key:
        print("OpenAI API key is set")
        openai_client = OpenAI(api_key=openai_api_key)
    else:
        print("OpenAI API key is not set")
        return None
    
    return openai_client

def read_pdf_summary():
    reader = PdfReader("files/Moinatik_Ghori_LinkedIn.pdf.pdf")
    pdf_text = ""

    for page in reader.pages:
        if page.extract_text():
            pdf_text += page.extract_text()

    # print(pdf_text)

    with open("files/summary.txt", "r") as f:
        summary = f.read()
    
    return pdf_text, summary


def chat(message, history):
    messages = [{"role" :"system", "content" : system_prompt}] + history + [{"role" :"user", "content" : message}]
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    return response.choices[0].message.content



def prepare_system_prompt(pdf_text, summary):
    system_prompt = f"""
    You are the digital professional representative for **{name}**. Your primary role is to act as a **personal AI assistant** on {name} engaging with individuals interested in their profile, such as potential clients, recruiters, and future employers.

    Your core responsibility is to **answer inquiries** regarding {name}'s career, professional background, skills, and experience.

    **Persona Guidelines:**
    * **Tone:** Maintain a highly professional, articulate, and engaging demeanor, mirroring a direct conversation with a valuable professional contact.
    * **Source Data:** Use the provided comprehensive summary of {name}'s background and LinkedIn profile as your sole knowledge base for all responses.
    * **Goal:** Faithfully and accurately represent {name}'s qualifications to promote professional opportunities.
    * **Constraint:** If the necessary information to answer a question is not explicitly contained within the provided summary, you **must explicitly state that the information is unavailable.**

    """
    system_prompt += f"\n\n## Summary:\n{summary}\n\n## LinkedIn Profile:\n{pdf_text}\n\n"
    system_prompt += f"With this context, please chat with the user, always staying in character as {name}."

    return system_prompt

def launch_app():
    gr.ChatInterface(chat, title=f"{name}'s AI Assistant", type="messages").launch()


if __name__ == "__main__":
    openai_client = validate_api_keys()
    if openai_client:
        client = openai_client  # Set global client variable
        pdf_text, summary = read_pdf_summary()
        system_prompt = prepare_system_prompt(pdf_text, summary)
        launch_app()``
    else:
        print("Cannot launch app: OpenAI API key is not set")


