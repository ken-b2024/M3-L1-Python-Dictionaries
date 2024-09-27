customer_service_tickets = {
    "INC1": {"User": "Christopher", "Issue": "Password Reset", "Status": "Open"}
    }
menu_items = [
            '1. Create a ticket',
            '2. View all tickets', 
            '3. Change Ticket Status',
            '4. Close a ticket', 
            '5. Quit'
]

def main_menu():
    print("Welcome to your Ticketing System!")
    print("\n")
    print('Menu:', *menu_items, sep='\n ')
def new_ticket(incident):
    existing_ids = [int(id[3:]) for id in customer_service_tickets]
    new_id_number = max(existing_ids) + 1 if existing_ids else 1
    new_id = f"INC{new_id_number}"
    user_name = input("Please add your first name: ")
    issue = input("What is your issue?: ")
    customer_service_tickets[new_id] = {"User": user_name, "Issue": issue, "Status": "Open"}
    print(f"\n{new_id}, has been successfully added to queue!")    
def view_tickets():
    if customer_service_tickets:
        print("\nAll Tickets:")
        for ticket_id, details in customer_service_tickets.items():
            print(f"{ticket_id} \nUser: {details['User']}, Issue: {details['Issue']}, Status: {details['Status']}")
    else:
        print("No tickets available.")
def change_ticket_status():
    ticket_id = input("Enter your ticket number: ")
    if ticket_id in customer_service_tickets:
       status = input("Enter the new status: ")
       customer_service_tickets[ticket_id]["Status"] = status
       print(f"\n{ticket_id} status has been changed to {status}")
    else:
        print("Ticket number is not valid. Try again...")
def close_ticket():
    ticket_id = input("Enter your ticket number: ")
    if ticket_id in customer_service_tickets:
        customer_service_tickets[ticket_id]["Status"] = "Closed"
        print(f"\n{ticket_id} has been closed")

while True:
    main_menu()
    try:
        user_action = int(input("Please select a menu item number: "))
        if user_action == 1:
            new_ticket("incident")
        if user_action == 2:
            view_tickets()
        if user_action == 3:
            change_ticket_status()
        if user_action == 4:
            close_ticket()
        if user_action == 5:
            print("\nThank you for using the Ticketing System. Goodbye!")
            break
    except ValueError:
        print("\nThat is not a valid selection. Try again...")
