def input_error(func):
    
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command."
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name not in contacts:
        raise KeyError
    return f"{name}: {contacts[name]}"

@input_error
def show_all(args, contacts):
    if not contacts:
        return "Contacts list is empty."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    print("Available commands:")
    print("  hello                   - Get a greeting")
    print("  add [name] [phone]      - Add a new contact")
    print("  change [name] [phone]   - Change an existing contact's phone")
    print("  phone [name]            - Get a contact's phone number")
    print("  all                     - Show all contacts")
    print("  close / exit            - Exit the program")
    print("-" * 40)
    
    while True:
        user_input = input("Enter a command: ")
        
        if not user_input.strip():
            continue
            
        try:
            command, *args = parse_input(user_input)
        except ValueError:
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()