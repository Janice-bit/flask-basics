from flask import Flask, render_template

app = Flask(__name__)

house_colours = {"artemis": "green",
                 "helio": "red",
                 "athena": "purple",
                 "poseidon": "blue"}

house_pts = {"artemis": 0,
             "helio": 67,
              "athena": -3120347160,
              "poseidon": 20}
visited_houses = []
analysed_text = []
             
@app.route("/")
def home():
    return "<h1> hellow world </h1>"

@app.route("/<text>")
def info(text):
    if text in house_colours.keys():
        house = text
        house_colour = house_colours[text]
        house_pt = house_pts[text]
        if house not in visited_houses:
            visited_houses.append(house)
        return render_template("index.html", house=house, house_colour= house_colour, house_pt= house.pt)

    else:
        length = len(text)
        num_digits = len([item for item in text if item.isdigit()])
        num_vowels = len([item for item in text if item.lower() in ["a","e","i","o","u"]])
        num_consonants = len([item for item in text if item.isalpha() and item.lower() not in "aeiou"])
        char_dict = {}
        if text != "favicon.ico":
            analysed_text.append(text)

        for item in text:
            if item not in char_dict:
                char[item] = 1
            else:
                char[item] += 1
if __name__ == "__main__":
     app.run(port=5678)
