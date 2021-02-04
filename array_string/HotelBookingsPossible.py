def is_hotel_booking_possible(arrival, departure, total_room):

    event = [(a,0) for a in arrival] + [(d,1) for d in departure]
    event.sort()
    print(event)
    
    guest=0
    for i in range(0, len(event)):
        if guest > total_room: return False
        if event[i][1] == 0 :
            guest = guest + 1
        else:
            guest = guest - 1
    return True

arrival = [1, 3, 5]
departure = [2, 4, 8]
total_room = 1
possible = is_hotel_booking_possible(arrival, departure, total_room)
print(possible)
