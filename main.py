import os
from dotenv import load_dotenv
from google import genai
import sys
import argparse

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
client_model = "gemini-2.0-flash-001"

def main():
    parser = argparse.ArgumentParser(description="AI Agent using Gemini API")
    parser.add_argument("prompt", help="The prompt to send to the AI")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    
    args = parser.parse_args()
    
    client_prompt = args.prompt
    verbose = args.verbose
    
    if not client_prompt:
        print("Error: No prompt provided")
        sys.exit(1)

    print("Hello from aiagent!")
    
    if verbose:
        print(f"User prompt: {client_prompt}")
    else:
        print(f"Your question was:", client_prompt)
    
    client_answer = client.models.generate_content(model=client_model, contents=client_prompt)
    print(f"Answer: {client_answer.text}")
    
    if verbose:
        print(f"Prompt tokens: {client_answer.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {client_answer.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
