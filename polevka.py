from bs4 import BeautifulSoup
import requests
import json


def main():

    ingredients = []


    response = requests.get("https://js-trebesin.github.io/bsoup-exam/")

    soup = BeautifulSoup(response.content, "html.parser") #<--- Úkol: popiš krátce, co tohle dělá : htmp.parser prelozi html tak, aby ho byla schopna soup zpracovat

    ingrs = soup.find_all("h2")

    for ingr in ingrs:
        ingredients.append(ingr.text)

    for i in range(4):
        print(ingredients[i])
            
    

    with open("recept.json", mode="w") as f:
        json.dump(ingredients, f, indent=4, ensure_ascii=False)



    


if __name__ == "__main__":
    main()