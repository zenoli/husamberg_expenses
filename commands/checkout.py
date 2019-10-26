from db import checkout_db
from constants import ADMIN

def checkout_command(number, arg_str):
    if number != ADMIN:
        return "You don't have permission to do this..."
    else:
        db_name = arg_str.strip()
        if checkout_db(db_name):
            return f"Switched to DB {db_name}."
        else:
            return f"New DB {db_name} created."
        
    
