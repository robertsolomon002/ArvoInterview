from dotenv import load_dotenv
import os
import json


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
            "Correct any mistakes if there is any please"},

            {"role" :"user", "content" : input_text}
        
        ]
    ) 
    dict_data = json.loads(response.choices[0].message.content.strip())
    app_type = dict_data["app_type"]
    dep_plat = dict_data["dep_plat"]
    return app_type,dep_plat


if __name__ == "__main__":
    input = input("Info about your app: ")
    type,dep = extract_app_info(input)
    print("AI extracted specs:", type, dep)