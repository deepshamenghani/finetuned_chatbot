import json

# Replace 'input.json' with the path to your JSON file
input_file_path = './teststructure/data/FAQ_with_unknownanswers.json'
output_file_path = './teststructure/data/FAQ_with_unknownanswers_converted.jsonl'

def convert_json_to_chat(input_file, output_file):
    # Load the questions and answers from the input JSON file
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Open the output file in write mode
    with open(output_file, 'w') as file:
        # Iterate over each question-answer pair and write the chat format to the output file
        for qa in data["questions"]:
            chat_format = {
                "messages": [
                    {"role": "user", "content": qa["question"]},
                    {"role": "assistant", "content": qa["answer"]}
                ]
            }
            # Write the chat conversation as a JSON line in the output file
            file.write(json.dumps(chat_format) + '\n')

# Call the function to perform the conversion
convert_json_to_chat(input_file_path, output_file_path)
