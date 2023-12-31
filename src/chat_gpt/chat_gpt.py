import openai
import json
import os
import yaml


openai.api_key = os.environ.get('CHATGPT_API_TOKEN')

class API_Manager(openai.ChatCompletion):
    def __init__(self):
        super().__init__()
        self.model = "gpt-3.5-turbo"
        self.temperature = 0
        self.max_tokens = 256

    def send_request(self, prompt):
        response = self.create(
            model = self.model,
            messages = prompt,
            temperature = self.temperature,
            max_tokens = self.max_tokens 
        )
        return response

    def get_interaction(self, res):
        json_res = json.dumps(res)
        data = json.loads(json_res)
        convo = [{"role": choice["message"]["role"], "content": choice["message"]["content"]} for choice in data["choices"]]
        return convo

    def prompt(self, prompt):
        response = self.send_request(prompt)
        return self.get_interaction(response)



class Message_Maker():
    def __init__(self, sys, user):
        self.sys = sys
        self.user = user

    def make_message(self, sys_message, user_message):
        return [{
            "role" : self.sys, 
            "content": sys_message,
            "role" : self.user,
            "content": user_message
        }]
    def make_user_message(self, user_message):
        return [{
            "role" : self.user,
            "content" : user_message
        }]
    




def main():

    message_maker = Message_Maker("system", "user")
    manager = API_Manager()
    # prompt = message_maker.make_message(
    #     sys_message="You will be provided with statements, and your task is to convert them to standard English.",
    #     user_message="She no went to the market."
    # )
    prompt = message_maker.make_user_message(
        "give me step by step instructions for making a very tasty cheesecake"
    )
    
    convo = prompt
    convo += manager.prompt(prompt)

    prompt = message_maker.make_user_message(
    "draw in asci a picture of an elephant"
    )
    convo += prompt
    convo += manager.prompt(prompt)
    # for i in range(5):
    #     user_input = input("ask chat_gpt something: ")
    #     userinput_obj = message_maker.make_user_message(user_input) 
    #     convo += manager.prompt(userinput_obj)

    with open("README.md", "w") as outfile:
        for item in convo:
            outfile.write(f"### Role: {item['role']}\n")
            outfile.write("#### Content:\n")
            outfile.write(item['content'])
            outfile.write("\n\n")  # Adds extra newlines between items for clarity


if __name__ == "__main__":
    main()