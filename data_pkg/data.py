import json, requests

# get the data from the API and write it to a JSON file
# not necessary, could be more simply stored in variable
# this was more of a thou   ght experiment to learn
# how to write, rewrite, and read a JSON file

def get_data():
    data_source = 'https://opentdb.com/api.php?amount=50&category=12&difficulty=easy&type=multiple'
    response = requests.get(data_source)
    data = response.json()

    #write results to JSON file, and set up use case for API error

    try:
        with open("data_pkg/source.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)
        # print("Data saved to JSON file")
    except Exception as e:
        print("Request failed. Please try again later.")

    

