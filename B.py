from functools import cmp_to_key
# 8
# 50 7 25 3632 A
# 14 23 52 212372 S
# 15 0 5 3632 C
# 14 21 30 212372 A
# 50 7 26 3632 C
# 14 21 30 3632 A
# 14 21 40 212372 B
# 14 23 52 3632 B

class event():

    def __init__(self, day, hour, minute, id_ , status):
        self.day = int(day)
        self.hour = int(hour)
        self.minute = int(minute)
        self.id = int(id_)
        self.status = status
        self.time = int(day) * 24 * 60 + int(hour) * 60 + int(minute)


def main():
    global event
    list_of_events = [] # array of events
    number_of_events = int(input()) # int входных строк
    for i in range(number_of_events):
        ev = input().split()
        # print(ev)
        ev = event(*ev) # string to event
        list_of_events.append(ev) # event append into array of events
    # print(list_of_events[0].status)
    list_of_events.sort(key = cmp_to_key(compare)) # сортируем массив событий по id => time
    # for event in list_of_events:
    #    print(event.id, event.day, event.hour, event.minute, event.status)

    previous_id = list_of_events[0].id
    previous_time = list_of_events[0].time
    previous_status = list_of_events[0].status
    list_times = []
    flying_time = 0
    for event in list_of_events[1:]:
        if event.id != previous_id:
            previous_id = event.id
            list_times.append(flying_time)
            flying_time = 0

        if event.status == 'S' or event.status == 'C':
            flying_time += (event.time - previous_time)

        if event.status == 'A' and event.id == previous_id:
            previous_time = event.time

        if event == list_of_events[-1]:
            list_times.append(flying_time)

    print(*list_times)

def calculus_time():
    pass

def compare(event1, event2): # compare by id => time
    if event1.id < event2.id:
        return -1
    elif event1.id > event2.id:
        return 1
    else:
        return event1.time - event2.time


if __name__ == '__main__':
    main()