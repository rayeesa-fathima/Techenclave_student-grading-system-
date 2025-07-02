def create_note():
    note = input("Enter your note: ")
    with open("notes.txt", "w") as file:
        file.write(note)
    print("Note saved to notes.txt")

def view_notes():
    try:
        with open("notes.txt", "r") as file:
            content = file.read()
            print("\n--- Saved Notes ---")
            print(content)
    except FileNotFoundError:
        print("No notes found. Please create a note first.")

def append_note():
    new_note = input("Enter content to append: ")
    with open("notes.txt", "a") as file:
        file.write("\n" + new_note)
    print("Content appended to notes.txt")
while True:
    print("\n=== Notes App Menu ===")
    print("1. Create a new note (overwrite)")
    print("2. View saved notes")
    print("3. Append to note")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        create_note()
    elif choice == '2':
        view_notes()
    elif choice == '3':
        append_note()
    elif choice == '4':
        print("Exiting Notes App.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")