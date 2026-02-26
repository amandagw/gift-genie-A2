# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, render_template
from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://amgwonghk_db_user:HEeEzZJDn52oNkWp@gift-db.5wi8vex.mongodb.net/?appName=gift-db"

client = MongoClient(MONGODB_URI)

db = client["gift-genie"]
collection = db["gifts"]

app = Flask(__name__)
# data = [
#     {
#         "item": "Owala waterbottle",
#         "price": 29.99,
#         "image_url": "https://target.scene7.com/is/image/Target/GUEST_45286c52-213f-4b2a-989e-b9bb7bcc40c2?wid=300&hei=300&fmt=pjpeg"
#     },
#     {
#         "item": "Smiski blindbox",
#         "price": 12.25,
#         "image_url": "https://blinkbox.co.nz/cdn/shop/files/smiski_bed-series_collection-light.webp?v=1720931209&width=1214"
#     },
#     {
#         "item": "Lego Set",
#         "price": 49.99,
#         "image_url": "https://m.media-amazon.com/images/I/81g3YSvD00L._AC_UF894,1000_QL80_.jpg"
#     },
#     {
#         "item": "Weighted stuffed animal",
#         "price": 25,
#         "image_url": "https://target.scene7.com/is/image/Target/GUEST_6fa57cf3-807b-40aa-84da-2cc01c33ce32"
#     },
# ]

@app.route("/")
def start_index():
    return render_template("index.html")

@app.route("/search/<budget>") #mapping
def search_gifts(budget):
    budget = float(budget)
    result = []
    for gift in collection.find():
        if gift["price"] <= budget:
            gift["_id"] = str(gift["_id"])
            result.append(gift)
    return result

app.run(host = '0.0.0.0', port = 5000)


# Press the green button in the gutter to run the script.
##if __name__ == '__main__':
  #  print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
