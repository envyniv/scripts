from pathlib import Path

from keepassxc_browser import Connection, Identity, ProtocolError

def password_eval():
    client_id = 'python-keepassxc-browser'

    state_file = Path('.assoc')
    if state_file.exists():
        with state_file.open('r') as f:
            data = f.read()
        id = Identity.unserialize(client_id, data)
    else:
        id = Identity(client_id)

    c = Connection()
    c.connect()
    c.change_public_keys(id)
    if not c.test_associate(id):
        print('Not associated yet, associating now...')
        assert c.associate(id)
        data = id.serialize()
        with state_file.open('w') as f:
            f.write(data)
        del data
    try:
        logins = c.get_logins(id, url='https://chat.foss.wtf')
        assert len(logins) == 1, logins
        for i in logins:
          if logins[i]["login"] == "envylogpuppet":
            password = logins[i]["password"]
    except ProtocolError:
        print('Entry not found')
        exit()
    c.disconnect()
    return password

accounts=[{ "server":"https://matrix.foss.wtf",
              "username":"envylogpuppet",
              "passeval":password_eval }] 

# the password_eval function can be named any thing as long as 
# it matches the function definition 

# ignore_rooms = ["room_id", "another_room_id"]
# note: room_id not room_alias (run matrixcli rooms to get the room_id)
