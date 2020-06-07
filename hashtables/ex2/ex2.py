''' tickets = [
    Ticket{ source: "PIT", destination: "ORD" },
    Ticket{ source: "XNA", destination: "CID" },
    Ticket{ source: "SFO", destination: "BHM" },
    Ticket{ source: "FLG", destination: "XNA" },
    Ticket{ source: "NONE", destination: "LAX" },
    Ticket{ source: "LAX", destination: "SFO" },
    Ticket{ source: "CID", destination: "SLC" },
    Ticket{ source: "ORD", destination: "NONE" },
    Ticket{ source: "SLC", destination: "PIT" },
    Ticket{ source: "BHM", destination: "FLG" }
] '''
#each ticket has a source and destination
#the First ticket the source is none
#the Second ticket the destination is none



class Ticket:
    def __init__(self, source, destination):
        self.source = source  #it's the previous
        self.destination = destination  #it's the next


def reconstruct_trip(tickets, length):
    cache = {}
    route = []
    
    for i in range(length):
        if tickets[i] not in cache:
            cache[tickets[i].source] = tickets[i].destination
    #append first one
    route.append(cache["NONE"])
    
    for j in range(length):
        current = route[-1] #current is equal to the last in route, starts by being our first ticket - "LAX"
        #LAX is a key and the value of it is the next airport for the route
        route.append(cache[current]) #then append the value of that airport
        if route[-1] == "NONE":  #when our route's last value is NONE return it
            return route

ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5, ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

''' expected = ["LAX", "SFO", "BHM", "FLG", "XNA", "SAP",
            "SLC", "PIT", "ORD", "NONE"] '''

reconstruct_trip(tickets, 10)

        
