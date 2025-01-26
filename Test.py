from dotenv import load_dotenv
import os
import json
import shutil

from openai import OpenAI


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client with the API key
client = OpenAI(api_key=api_key)



def extract_app_info(input_text):


    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages = [
            {"role" : "system" , "content" : "You are a DevOps assistant that automates the process of deploying applications.You must do so "
            "by extracting info from the natural language input into 2 pices of info: The application type AND the platform. Do so by having"
            "JSON keys with names: app_type and dep_plat"
            "If none is detected, write N/A"
            "Correct any mistakes if there is any please, and make them lowercased, with the first letter caps"
            "Now, the input will also include a github repository link, add a key called git_repo. Make sure no spaces before or after"},

            {"role" :"user", "content" : input_text}
        
        ]
    ) 
    dict_data = json.loads(response.choices[0].message.content.strip())
    app_type = dict_data["app_type"]
    dep_plat = dict_data["dep_plat"]
    git_repo = dict_data["git_repo"]
    return app_type,dep_plat,git_repo




if __name__ == "__main__":
    input = input("Info about your app: ")
    type,dep,link = extract_app_info(input)
    print("AI extracted specs:", type, dep , link)
    
    current_dir = os.getcwd()
    clone_dir = os.path.join(current_dir, "clone_repo")
    os.system(f'git clone "{link}" "{clone_dir}"')
    
    

