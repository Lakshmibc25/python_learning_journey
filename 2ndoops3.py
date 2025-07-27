class Database:
    def _init(self):  # fixed __init_ method
        self.__storage = {}  # private attribute

    def write(self, key, value):
        self.__storage[key] = value

    def read(self, key):
        if key in self.__storage:
            print(self.__storage[key])
        else:
            print("DB item not available")

db = Database()
db.write("subscribers", "100k")
db.read("subscribers")
db.write("name", "EID")
db.read("name")