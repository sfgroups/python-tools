import openai
from dotenv import dotenv_values, find_dotenv
from openai import OpenAI
from requests.structures import CaseInsensitiveDict

def get_gpt_response(prompt=None):
    # Set up your OpenAI API key
    config = CaseInsensitiveDict(dotenv_values(find_dotenv()))
    openai.api_key = config.get('OPENAI_API_KEY')

    client = OpenAI(# This is the default and can be omitted
        api_key=openai.api_key)
    try:
        chat_completion = client.chat.completions.create(messages=[{"role": "user", "content": "Say this is a test", }],
            model="gpt-3.5-turbo", )

        print(chat_completion)
        return chat_completion.choices[0].text
    except openai.APIConnectionError as e:
        # Handle connection error here
        print(f"Failed to connect to OpenAI API: {e}")
        pass
    except openai.APIError as e:
        # Handle API error here, e.g. retry or log
        print(f"OpenAI API returned an API Error: {e}")
        pass
    except openai.RateLimitError as e:
        # Handle rate limit error (we recommend using exponential backoff)
        print(f"OpenAI API request exceeded rate limit: {e}")
        pass  #

# Example usage
if __name__ == "__main__":
    prompt = "Write a short story about a brave knight."
    response = get_gpt_response(prompt)
    print(response)
