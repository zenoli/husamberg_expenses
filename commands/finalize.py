from constants import ADMIN
import bills
import db

def finalize_command(number, arg_str):
    if number == ADMIN:
        success = bills.finalize()
        if success:
            return (
                f"Finalization of {db.current_db} complete.\n"
                f"'How much' commands can be issued"
            )
        else:
            f"DB {db.current_db} not found. Finalization failed..."
