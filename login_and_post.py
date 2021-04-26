# From:  https://stackoverflow.com/questions/43438323/python-requests-form-filling


import requests

save = "https://anotepad.com/note/save"
txt = "Hello World"
login = "https://anotepad.com/create_account"

data = {"action": "login",
        "email": "aambrioso1@gmail.com",
        "password": "Thumper1",
        "submit": ""}

# construct the POST request
with requests.session() as s: # Use a Session object.
    s.post(login, data) # Login.

    form_data = {"number": "2yrwpi",
                 "notetype": "PlainText",
                 "noteaccess": "2",
                 "notequickedit": "false",
                 "notetitle": "whatever",
                 "notecontent": txt}

    r = s.post(save, data=form_data) # Save note.

print(f'{r.json()=}')

# s.post("https://anotepad.com/note/list").text

"""
r.json()

will give you {"message":"Saved"} on success. Also if you want to see what notes you have,
after logging in, run 

s.post("https://anotepad.com/note/list").text.

"""