def parse_input(user_input):
    parts = user_input.split()
    cmd = parts[0].strip().lower()
    args = parts[1:] 
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid number of arguments. Usage: add <name> <phone>"
    name, phone = args
    contacts[name] = phone
    return "Contact added"

def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid number of arguments. Usage: change <name> <phone>"
    
    name, phone = args
    if name not in contacts:
        return f"{name} doesn't exist."  # Return if contact doesn't exist
    
    contacts[name] = phone  # Update the contact
    return f"Contact {name} changed."
def phone_username(name, contacts):
    if name in contacts:
        return contacts[name]
    else:
        return f"{name} doesn't exist."
    
def all(contacts):
    return contacts
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)  
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            result = add_contact(args, contacts)
            print(result)
        elif command == "change":
            result = change_contact(args, contacts)
            print(result)
        elif command == "username":
            if len(args) == 1:
                print(phone_username(args[0], contacts))  
            else:
                print("Usage: phone_username <username>")
        elif command == "all":
            print(all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
