import openai
api = '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'
def chat_gpt(api_key, query):
    openai.api_key = api_key
    completions = openai.Completion.create(
        engine='text-davinci-002',
        prompt=query,
        temperature=0.5,
        top_p=1,
        max_tokens=2048,
        n =1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )
    return completions.choices[0].text
while True:
    query=input("\nYou: ")
    response = chat_gpt(api, query)
    print(response)
