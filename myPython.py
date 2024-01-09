import openai
import requests
from bs4 import BeautifulSoup

openai.api_key = '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'

# Website URL
website_url = "https://botpenguin.com/"

def fetch_website_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def extract_key_information(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    key_elements = soup.find_all('p', {'class': 'content'})
    extracted_data = "\n".join([element.get_text() for element in key_elements])
    return extracted_data

def generate_chatbot_response(user_input, website_content):
    prompt = f"User: {user_input}\nWebsiteContent: {website_content}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input},
        ]
    )

    return response['choices'][0]['message']['content'].strip()

if __name__ == "__main__":
    print("Welcome to the BotPenguin..! \n(Type 'exit' to end the conversation)")

    # Fetch website content
    html_content = fetch_website_content(website_url)

    if html_content:
        website_content = extract_key_information(html_content)

        while True:
            print("**********************************************************************************************************************")
            user_input = input("You: ")

            if user_input.lower() == 'exit':
                print("Chatbot session ended.\nThank's for your interest in BotPenguin..!")
                break

            chatbot_response = generate_chatbot_response(user_input, website_content)

            # Print the chatbot's response
            
            print("Chatbot:", chatbot_response,"\n")
    else:
        print("Failed to fetch website content.")

'''
Here are some example queries to get started..
-What are the key features of BotPenguin?
-Can you tell me more about the services offered by BotPenguin?
-How is BotPenguin used in different industries?
-What kind of chatbots can I create using BotPenguin?
-What is the pricing structure for BotPenguin?
'''
