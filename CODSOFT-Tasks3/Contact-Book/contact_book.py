import json
import tkinter as tk
from tkinter import messagebox, simpledialog


CONTACTS_FILE = "contacts.json"


def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)


def cli_menu(contacts):
    while True:
        print("\nContact Book CLI Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_contact_cli(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact_cli(contacts)
        elif choice == "4":
            update_contact_cli(contacts)
        elif choice == "5":
            delete_contact_cli(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def add_contact_cli(contacts):
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    address = input("Enter address: ").strip()
    if name in contacts:
        print("Contact already exists. Try updating it instead.")
    else:
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print("Contact added successfully!")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")


def search_contact_cli(contacts):
    search = input("Enter name or phone number to search: ").strip()
    results = [f"{name}: {details}" for name, details in contacts.items() if search in name or search in details['phone']]
    if results:
        print("\nSearch Results:")
        for result in results:
            print(result)
    else:
        print("No contact found.")


def update_contact_cli(contacts):
    name = input("Enter the name of the contact to update: ").strip()
    if name in contacts:
        print("Leave a field empty to keep it unchanged.")
        phone = input("Enter new phone number: ").strip()
        email = input("Enter new email address: ").strip()
        address = input("Enter new address: ").strip()
        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email
        if address:
            contacts[name]["address"] = address
        print("Contact updated successfully!")
    else:
        print("Contact not found.")


def delete_contact_cli(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


def add_contact_gui():
    name = simpledialog.askstring("Add Contact", "Enter contact name:")
    if name:
        phone = simpledialog.askstring("Add Contact", "Enter phone number:")
        email = simpledialog.askstring("Add Contact", "Enter email:")
        address = simpledialog.askstring("Add Contact", "Enter address:")
        if name in contacts:
            messagebox.showerror("Error", "Contact already exists.")
        else:
            contacts[name] = {"phone": phone, "email": email, "address": address}
            save_contacts(contacts)
            messagebox.showinfo("Success", "Contact added successfully!")

def view_contacts_gui():
    if not contacts:
        messagebox.showinfo("Contact List", "No contacts found.")
    else:
        contact_list = "\n".join([f"{name}: {details['phone']}" for name, details in contacts.items()])
        messagebox.showinfo("Contact List", contact_list)

def search_contact_gui():
    search = simpledialog.askstring("Search Contact", "Enter name or phone number:")
    if search:
        results = [f"{name}: {details}" for name, details in contacts.items() if search in name or search in details['phone']]
        if results:
            result_text = "\n".join(results)
            messagebox.showinfo("Search Results", result_text)
        else:
            messagebox.showinfo("Search Results", "No contact found.")

def delete_contact_gui():
    name = simpledialog.askstring("Delete Contact", "Enter the name of the contact to delete:")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        messagebox.showinfo("Success", "Contact deleted successfully!")
    else:
        messagebox.showerror("Error", "Contact not found.")


def gui_menu():
    root = tk.Tk()
    root.title("Contact Book")

    tk.Button(root, text="Add Contact", command=add_contact_gui, width=20).pack(pady=5)
    tk.Button(root, text="View Contacts", command=view_contacts_gui, width=20).pack(pady=5)
    tk.Button(root, text="Search Contact", command=search_contact_gui, width=20).pack(pady=5)
    tk.Button(root, text="Delete Contact", command=delete_contact_gui, width=20).pack(pady=5)
    tk.Button(root, text="Exit", command=root.quit, width=20).pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    contacts = load_contacts()
    print("1. Run CLI\n2. Run GUI")
    choice = input("Choose an option: ").strip()
    if choice == "1":
        cli_menu(contacts)
    elif choice == "2":
        gui_menu()
    else:
        print("Invalid option. Exiting.")