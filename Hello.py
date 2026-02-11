import requests
from flask import Flask

url = "https://boozeapi.com/api/v1/cocktails"
response = requests.get(url)
data = response.json()

ingrediencie = []
drinks = data
meno_drinku = ''
vodka_count = 0
gin_count = 0
rum_count = 0
vodka = False
rum = False
gin = False
adresa = ''
adresy = []
mena = []
print('Drinky a ich obsah:')

for drink in drinks:
    veci = drinks.get("data", [])
    for vec in veci:
        vodka = False
        rum = False
        gin = False
        meno_drinku = vec.get("name")
        ingredients = vec.get("ingredients", {})
        adresa = vec.get('image', {})
        adresy.append(adresa)
        mena.append(meno_drinku)

        for ingredient in ingredients:
            ingrediencie.append(ingredient['type'])
            if "Vodka" in ingredient['type'] and vodka == False:
                vodka = True
                vodka_count += 1
            if "Gin" in ingredient['type'] and gin == False:
                gin = True
                gin_count += 1
            if "Rum" in ingredient['type'] and rum == False:
                rum = True
                rum_count += 1

        print(f'{meno_drinku} obsahuje: {", ".join(map(str, ingrediencie))}')
        ingrediencie = []
        print(adresa)

app = Flask(__name__)


@app.route("/")
def hello_world():
    global drinks, ingredients, drink, veci, vec, meno_drinku, adresa, ingredient
    html = "<h1>Drinky z API</h1>"
    drinks = data
    meno_drinku = ''
    adresa = ''
    for drink in drinks:
        veci = drinks.get("data", [])
        for vec in veci:
            meno_drinku = vec.get("name")
            ingredients = vec.get("ingredients", {})
            adresa = vec.get('image', {})
        html += f"<h2>{meno_drinku}</h2>"
        html += f'<img src="{adresa}" width="250"><br>'

        html += "<b>Ingrediencie:</b><ul>"
        for ingredient in ingredients:
            html += f"<li>{ingredient.get('type')}</li>"
        html += "</ul><hr>"

    return html
if __name__ == "__main__":
    app.run(debug=True)

print('')
print('Pocty alkoholu v drinkoch:')
print("Počet drinkov s vodkou:", vodka_count)
print("Počet drinkov s ginom:", gin_count)
print("Počet drinkov s rumom:", rum_count)
