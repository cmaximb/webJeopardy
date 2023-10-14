import html2text
import requests

parser = html2text.HTML2Text()

def ask_question(jeopc):
    categories = []
    responses = requests.get("http://jservice.io/api/clues", params = {"category": jeopc})
    for m in range(5):
        try: 
            print(responses.json()[m]["question"])
            response = responses.json()[m]
            parser.handle(response["answer"])
            parser.handle(response["question"])
        except:
            response = []
        categories.append(response)

    return categories
