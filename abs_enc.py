class Database:
    def __init(self):
        
        self.__storage = {} #private

    def write(self, key, value):
        self.__storage[key] = value

    def read(self,key):
        if key in self.__storage:
            print (self.__storage[key])
        else:
            print("DB item not available")
        
db = Database ()
db.write("subscribers","100k")
db.read("subscribers")
db.write("name","EID")

db.read("name")