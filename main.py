
from readfile import File
from hotel import Hotel, Room
from user import User

if __name__ == '__main__':
    reader = File()
    datasource = reader.get_data()

    all_detail = []
    for i in datasource:
        splitRow = i.split('\n')

        for j in splitRow:
            splitSpace =j.split(" ")
            all_detail.append(splitSpace)

    # loop select data in each row
    for i in range(0, len(all_detail), 1):
        for j in range(0, len(all_detail[i]),1):
            all_detail[i][j]
            
        match (all_detail[i][0]): # all detail[i][0] = the first input of each line (Command)
            
            case "create_hotel":
                floor = all_detail[0][1]
                roomPerFloor = all_detail[0][2]
                #create new hotel 
                hotel = Hotel(floor, roomPerFloor)
                print("Hotel creatd with", hotel.floor, "floor(s), ", hotel.roomPerFloor, "room(s) per floor.")
            
            case "book":
                roomNumber = all_detail[i][1]
                userName = all_detail[i][2]
                age = all_detail[i][3]
                # roomIndex is index of room in array
                # Example Room 203 have index number = 5

                roomIndex = [x.roomNumber for x in hotel.rooms].index(roomNumber) 
                keyInUse = hotel.rooms[roomIndex].keycard

                if hotel.rooms[roomIndex].keycard == 0:
                    hotel.booking(roomIndex, userName, age, 'one')
                    print("Room", hotel.rooms[roomIndex].roomNumber , "is booked by", hotel.users[-1], "with keycard number ", str(hotel.rooms[roomIndex].keycard) +".")


                else:
                    print("Cannot book room", hotel.rooms[roomIndex].roomNumber,"for", userName, "The room is currently booked by", hotel.rooms[roomIndex].user)


            case "list_available_rooms":
                # check Available room 
                for i in hotel.rooms:
                    if i.keycard == 0:
                        print(i.roomNumber)

            case "checkout":
                key = all_detail[i][1]
                name = all_detail[i][2]

                hotel.checkOut(key, name, "one")
                
            case "list_guest":
                users = []
                for user in hotel.users:
                    users.append(user.name)
                result = ', '.join(user for user in users)
                print(result)
            
            case "get_guest_in_room":
                room = all_detail[i][1]
                guestInRoom = hotel.getUserByRoom(room)
                print(guestInRoom)
            
            case "list_guest_by_age":
                operator = all_detail[i][1]
                age = all_detail[i][2]
                guestsByAge = hotel.listGuestByAge(operator, age)
                result = ', '.join(user for user in guestsByAge)
                print(result)
            
            case "list_guest_by_floor":
                floor = all_detail[i][1]
                guestsByFloor = hotel.listGuestByFloor(floor)
                result = ', '.join(user for user in guestsByFloor)
                print(result)

            case "checkout_guest_by_floor":
                floor = all_detail[i][1]
                checkoutRooms = hotel.checkout_by_floor(floor)
                result = ', '.join(room for room in checkoutRooms)
                print("Room", result, "are checkout.")

            case "book_by_floor":
                floor = all_detail[i][1]
                name = all_detail[i][2]
                age = all_detail[i][3]
                 
                bookedRooms = hotel.bookByFloor(floor, name, age)
                counter = 0
                resultRoom = ', '.join(str(room['name']) for room in bookedRooms)
                resultKey = ', '.join(str(room['key']) for room in bookedRooms)
                for room in bookedRooms:
                    counter += 1

                if counter == hotel.roomPerFloor:
                    print("Room", resultRoom, "are booked with keycard number", resultKey)
                else:
                    print(f'Cannot book floor {floor} for TonyStark')
                    

            
            
                
                
                

                
        
        
    