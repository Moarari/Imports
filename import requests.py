import requests

url = "https://boozeapi.com/api/v1/cocktails"
response = requests.get(url)
data = response.json()

ingrediencie=[]
drinks = data
meno_drinku = ''
vodka_count = 0
gin_count = 0
rum_count = 0

print('Drinky a ich obsah:')

for drink in drinks:

    veci = drinks.get("data", [])

    for vec in veci:

        meno_drinku = vec.get("name")
        # print(vec['name'] + vec['type'])
        ingredients = vec.get("ingredients", {})

        for ingredient in ingredients:

            ingrediencie.append(ingredient['type'])
            if "Vodka" in ingredient['type']:
                vodka_count += 1
            if "Gin" in ingredient['type']:
                gin_count += 1
            if "Rum" in ingredient['type']:
                rum_count += 1

        print(f'{meno_drinku} obsahuje: {', '.join(map(str,ingrediencie))}')
        ingrediencie=[]

print('')
print('Pocty alkoholu v drinkoch:')
print("Počet drinkov s vodkou:", vodka_count)
print("Počet drinkov s ginom:", gin_count)
print("Počet drinkov s rumom:", rum_count)
