import main 

def test_join_board():
    board = main.MessageBoard()
    board = main.MessageBoard(status="public")
    user = main.User('Me',main.WhatsAppObserver)
    board.add_subscriber(user)
    assert(user in board.event_manager.users)

def test_join_private_board():
    board = main.MessageBoard()
    board = main.MessageBoard(status="private", password="test")
    user = main.User('Me',main.WhatsAppObserver)
    board.add_subscriber(user, 'test')
    assert(user in board.event_manager.users)

def test_fail_join_private_board():
    board = main.MessageBoard()
    board = main.MessageBoard(status="private", password="test12345")
    user = main.User('Me',main.WhatsAppObserver)
    assert(board.add_subscriber(user, "test")=="Wrong Password")

def test_leave_board():
    board = main.MessageBoard()
    board = main.MessageBoard(status="public")
    user = main.User('Me',main.WhatsAppObserver)
    board.add_subscriber(user)
    assert(user in board.event_manager.users)
    board.remove_subscriber(user)
    assert(user not in board.event_manager.users)

def test_update():
    user = main.User('Me',main.WhatsAppObserver)
    assert(user.observer==main.WhatsAppObserver)
    user.update(main.EmailObserver)
    assert(user.observer==main.EmailObserver)

def test_message_received():
    board = main.MessageBoard()
    board = main.MessageBoard(status="public")
    user = main.User('Me',main.WhatsAppObserver)
    board.add_subscriber(user)
    board.add_message("Hello World")




