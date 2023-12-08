from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()
# Load your API key from an environment variable
client = OpenAI(api_key=os.getenv('OPENAI_API'))

# Fine-tuning the model
client.fine_tuning.jobs.create(
  training_file=os.getenv('FAQ_CLEANED'), 
  model="gpt-3.5-turbo-1106",
)