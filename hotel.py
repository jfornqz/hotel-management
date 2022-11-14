from user import User
class Hotel:

    def __init__(self, floor, roomPerFloor) :
        self.floor = int(floor)
        self.roomPerFloor =  int(roomPerFloor)
        # have hotel [] -> [[], []]
        self.rooms = [] # [101, 102, 103, 201, 202, 203]
        self.keyCard = [] # [1, 2, 3, 4, 5, 6]
        self.users = []
        self.hotel = []
        



        

        keyNumber = 1
        # create room with floor and roomPerFloor
        for floorAmt in range(1, self.floor+1, 1):
            floor = []
            room = []

            for roomAmt in range(1, self.roomPerFloor+1, 1):
                self.rooms.append(Room(f"{floorAmt}{'%02d' %(roomAmt)}"))
                room.append(Room(f"{floorAmt}{'%02d' %(roomAmt)}"))
                self.keyCard.append(keyNumber)
                keyNumber += 1
            floor.append(room)
            self.hotel.append(*floor)

    def getUser(self, keyCardNumber):
        for x in self.users:
            if keyCardNumber in x.userKey:
                return x.name

        
    def getUserByRoom(self, room):
        for guest in self.rooms:
            if room in guest.roomNumber:
                return guest.user
    
    def listGuestByAge(self, operator, age):
        guest = []
        for i in range(len(self.users)):
            if operator == "<":
                if self.users[i].age < age:
                    guest.append(self.users[i].name)
            elif operator == "=":
                if self.users[i].age == age:
                    guest.append(self.users[i].name)
            elif operator == ">":
                if self.users[i].age > age:
                    guest.append(self.users[i].name)
        return guest
    
    def listGuestByFloor(self, floor):
        users = []
        for i in self.rooms:
            if i.roomNumber[0] == floor and i.keycard != 0:
                users.append(i.user.name)
        return users

    def booking(self, index, name, age, clear):
        # Thor -> String
        # Thor -> User().userKey
        keyCard = self.keyCard[0]
        isGuest = False
        for i in self.users:
            if name == i.name:
                isGuest = True
                
        if isGuest:
            indexOfGuest = next(i for (i, d) in enumerate(self.users) if d.name == name)
            # print(indexOfGuest)
            self.keyCard.remove(keyCard) #remove from hotel -----> user
            self.rooms[index].setKeyCard(keyCard) #set keycard to room
            self.rooms[index].setUser(self.users[indexOfGuest]) #set user
            self.users[indexOfGuest].userKey.append(keyCard)
        else:
            self.keyCard.remove(keyCard) #remove from hotel -----> user
            user = User(name, age, [keyCard])
            self.users.append(user)
            self.rooms[index].setKeyCard(keyCard) #set keycard to room
            self.rooms[index].setUser(user) #set user
        # print(self.rooms[index].get_user())

        if clear == 'all':
            return self.rooms[index].roomNumber


        
    def bookByFloor(self, floor, name, age):
        rooms = []
        count = 0
        txt = ''
        for i in self.rooms:
            if i.roomNumber[0] == floor and i.keycard == 0:
                room = self.booking(count, name, age, 'all')
                rooms.append({"name": room, "key": i.keycard})
            count += 1
        
        return rooms

    def checkout_by_floor(self, floor):
        rooms = []
        for i in self.rooms:
            if i.roomNumber[0] == floor and i.keycard != 0:
                room = self.checkOut(i.keycard, i.get_user().get_name(), 'all')
                rooms.append(room)
        return rooms


    def checkOut(self, keycard, name, clear):
        indexOfGuest = next(index for (index, d) in enumerate(self.users) if d.name == name)
        indexOfRoom = next(index for (index, d) in enumerate(self.rooms) if d.keycard == int(keycard))
        if int(keycard) in self.users[indexOfGuest].userKey:

            self.rooms[indexOfRoom].clearUser()
            self.rooms[indexOfRoom].clearKeyCard()
            self.keyCard.append(int(keycard))
            self.keyCard.sort()
            # ลบ KeyCard ออกจาก User
            self.users[indexOfGuest].userKey.remove(int(keycard))
            
            # สร้าง Condition เช็คจำนวน KeyCard ถ้า User ไม่มี KeyCard แล้วลบออกจาก Hotel
            if len(self.users[indexOfGuest].userKey) == 0:
                self.users.pop(indexOfGuest)

            if clear == 'all':
                return self.rooms[indexOfRoom].roomNumber
            else:
                print("Room", self.rooms[indexOfRoom].roomNumber, "is checkout.")
                
        else:
            print("Only", self.getUser(int(keycard)) ,"can checkout with keycard number", keycard)

        
    def __str__(self):
        return f'{self.users}'

class Room:

    def __init__(self, roomNumber, user=User(name='', age='', key=[])):
        self.roomNumber = roomNumber
        self.keycard = 0
        self.user = user
    
    def setKeyCard(self, keycard):
        self.keycard = keycard
    
    def get_user(self):
        return self.user
    
    def setUser(self, user):
        self.user = user
        
    def clearUser(self):
        self.user = User(name='', age='', key=[])
        
    def clearKeyCard(self):
        self.keycard = 0
        
    def __str__(self):
        return f'{self.roomNumber}'
    
