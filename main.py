class Observer():
    def update(self, message):
        pass

class WhatsAppObserver(Observer):
    def update(self, message, name) -> None:
        print("Notifying "+ name +" by Whatsapp\nMessage Received: " + message)

class SMSObserver(Observer):
    def update(self, message, name) -> None:
        print("Notifying "+ name +" by SMS\nMessage Received: " + message)

class EmailObserver(Observer):
    def update(self, message, name) -> None:
        print("Notifying "+ name +" by EMAIL\nMessage Received: " + message)

class User():
    def __init__(self, name, observer: Observer) -> None:
        self.name = name
        self.observer = observer
    
    def update(self,observer):
        self.observer=observer

class EventManager():
    def __init__(self): 
        self.users = []

    def notify(self, message) -> None:
        for user in self.users:
            user.observer.update(self,message, user.name)

    def attach(self, user : User) -> None:
        self.users.append(user)

    def detach(self, user : User) -> None:
        self.users.remove(user)

class MessageBoard():
    def __init__(self,status="public",password="password"): 
        self.event_manager = EventManager()
        self.status=status
        self.password=password
    def add_message(self, message):
        self.event_manager.notify(message)

    def add_subscriber(self, user : User,given_password="") -> None:
        if self.status == "private" and self.password==given_password:
            self.event_manager.attach(user)
        elif self.status == "public":
            self.event_manager.attach(user)
        else:
            return "Wrong Password"
    
    def remove_subscriber(self, user : User) -> None:
        self.event_manager.detach(user)
        
if __name__ == "__main__":
    board = MessageBoard()
    board = MessageBoard(status="private", password="test")
    user1 = User('Matthew',WhatsAppObserver)
    user2= User('Mark',SMSObserver)
    user3 = User('John',EmailObserver)
    
    board.add_subscriber(user1, "test")
    board.add_subscriber(user2, "test")
    board.add_subscriber(user3, "test")
    board.add_message("Hello World")
    user1.update(SMSObserver)