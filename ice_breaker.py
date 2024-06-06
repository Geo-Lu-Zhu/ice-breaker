import os
from dotenv import dotenv_values, load_dotenv

load_dotenv()
if __name__ == "__main__":
    print("welcome")
    print(os.getenv('OPENAI_API_KEY'))