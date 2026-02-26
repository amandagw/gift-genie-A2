from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://amgwonghk_db_user:HEeEzZJDn52oNkWp@gift-db.5wi8vex.mongodb.net/?appName=gift-db"

client = MongoClient(MONGODB_URI)

db = client["gift-genie"]
collection = db["gifts"]

# Write
collection.insert_one({"item": "Owala waterbottle","price": 29.99,"image_url": "https://target.scene7.com/is/image/Target/GUEST_45286c52-213f-4b2a-989e-b9bb7bcc40c2?wid=300&hei=300&fmt=pjpeg"})
collection.insert_one({"item": "Smiski blindbox","price": 12.25,"image_url": "https://blinkbox.co.nz/cdn/shop/files/smiski_bed-series_collection-light.webp?v=1720931209&width=1214"})
collection.insert_one({"item": "Lego Set","price": 49.99,"image_url": "https://m.media-amazon.com/images/I/81g3YSvD00L._AC_UF894,1000_QL80_.jpg"})
collection.insert_one({"item": "Weighted stuffed animal","price": 25,"image_url": "https://target.scene7.com/is/image/Target/GUEST_6fa57cf3-807b-40aa-84da-2cc01c33ce32"})


#Read
#doc = collection.find_one()
