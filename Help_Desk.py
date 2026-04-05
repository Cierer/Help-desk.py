import json
import os
from datetime import datetime

# Represents a single help desk ticket
class Ticket:
def __init__(self, ticket_id, user, issue, priority):
self.ticket_id = ticket_id # Unique ID for the ticket
self.user = user # Name of the user who created the ticket
self.issue = issue # Description of the issue
self.priority = priority # Priority level (Low, Medium, High)
self.status = "Open" # Default status when ticket is created
self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Timestamp

# Convert ticket object into dictionary format for JSON storage
def to_dict(self):
return self.__dict__

# Handles all ticket operations (CRUD)
class HelpDesk:
FILE_NAME = "tickets.json" # File where tickets are stored

def __init__(self):
# Load existing tickets when the system starts
self.tickets = self.load_tickets()

# Load tickets from JSON file
def load_tickets(self):
# If file does not exist, return empty list
if not os.path.exists(self.FILE_NAME):
return []

# Read ticket data from file
with open(self.FILE_NAME, "r") as file:
return json.load(file)

# Save tickets to JSON file
def save_tickets(self):
with open(self.FILE_NAME, "w") as file:
json.dump(self.tickets, file, indent=4)

# Generate a simple incremental ticket ID
def generate_ticket_id(self):
return len(self.tickets) + 1

# Create a new ticket
def create_ticket(self):
user = input("Enter user name: ").strip()
issue = input("Describe the issue: ").strip()
priority = input("Priority (Low / Medium / High): ").capitalize()

# Validate priority input
if priority not in ["Low", "Medium", "High"]:
print("❌ Invalid priority.")
return

# Create a new Ticket object
ticket = Ticket(
self.generate_ticket_id(),
user,
issue,
priority
)

# Add ticket to list and save
self.tickets.append(ticket.to_dict())
self.save_tickets()

print(f"✅ Ticket #{ticket.ticket_id} created successfully.")

# Display all tickets
def view_tickets(self):
# Check if there are no tickets
if not self.tickets:
print("📭 No tickets available.")
return

# Loop through and display each ticket
for ticket in self.tickets:
print("-" * 40)
for key, value in ticket.items():
print(f"{key}: {value}")

# Update ticket status
def update_status(self):
try:
ticket_id = int(input("Enter ticket ID: "))
except ValueError:
print("❌ Invalid ticket ID.")
return

# Search for the ticket by ID
for ticket in self.tickets:
if ticket["ticket_id"] == ticket_id:
print(f"Current status: {ticket['status']}")

new_status = input("New status (Open / In Progress / Closed): ").title()

# Validate status input
if new_status not in ["Open", "In Progress", "Closed"]:
print("❌ Invalid status.")
return

# Update status and save changes
ticket["status"] = new_status
self.save_tickets()

print("✅ Status updated.")
return

# If ticket is not found
print("❌ Ticket not found.")

# Main menu system
def menu(self):
while True:
print("\n=== IT HELP DESK SYSTEM ===")
print("1. Create Ticket")
print("2. View Tickets")
print("3. Update Ticket Status")
print("4. Exit")

choice = input("Choose an option: ")

if choice == "1":
self.create_ticket()
elif choice == "2":
self.view_tickets()
elif choice == "3":
self.update_status()
elif choice == "4":
print("👋 Exiting system.")
break
else:
print("❌ Invalid choice.")
# This ensures the program runs only when executed directly
if __name__ == "__main__":
app = HelpDesk()
app.menu()

