from uuid import uuid4
from nicegui import ui

messages = []

@ui.refreshable
def chat_messages(own_id):
    for user_id, avatar, username, text in messages:
        ui.chat_message(avatar=avatar, text=f"{username}: {text}", sent=user_id==own_id)

@ui.page('/')
def index():
    username_input = ui.input(placeholder='Enter your username')  # Input field for username
    
    def send():
        username = username_input.value
        messages.append((user, avatar, username, text.value))
        chat_messages.refresh()
        text.value = ''
        
    user = str(uuid4())
    avatar = f'https://robohash.org/{user}?bgset=bg1'
    
    with ui.column().classes('w-full items-stretch'):
        username_input  # Display the username input field
        chat_messages(user)

    with ui.footer().classes('bg-white'):
        with ui.row().classes('w-full items-center'):
            with ui.avatar():
                ui.image(avatar)
            text = ui.input(placeholder='message') \
                .props('rounded outlined').classes('flex-grow') \
                .on('keydown.enter', send)

ui.run()
