# Customer Service Chatbot with OpenAI and Python

This repository houses the code for a project aimed at developing a customer service chatbot using OpenAI's GPT models and Python. It includes scripts for setting up a chatbot, handling conversations, and fine-tuning the model with custom datasets to improve interaction quality.

## Repository Contents

- `/data`: Contains the datasets for chatbot training and fine-tuning.
- `.gitignore`: Specifies intentionally untracked files to ignore.
- `README.md`: Describes the project and how to navigate the repository.
- `chatbot_conversation`: A script for initiating a chatbot that can handle continuous conversations.
- `chatbot_conversation_tuned`: An advanced version of the chatbot script post fine-tuning.
- `chatbot_singlequestion`: A script for a chatbot that responds to single queries.
- `tuning_model.py`: The fine-tuning script for optimizing the chatbot's performance.
- `uploading_dataset.py`: A utility to upload training datasets to the OpenAI API.

## Setup

To set up the chatbot, clone this repository and install the required dependencies. You will need to obtain an OpenAI API key and ensure Python is installed on your system.

## Usage

The scripts can be run individually, depending on your requirements:

- Use `chatbot_singlequestion` for a basic chatbot interaction.
- `chatbot_conversation` allows for more dynamic conversation handling.
- `uploading_dataset.py` and `tuning_model.py` are used in sequence for fine-tuning the chatbot model.
