def main():
    project = input("Enter the filename you want to create: ")
    with open(project, 'w') as file:
        file.write(input(f"Enter the content for '{project}': "))
    print(f"Content successfully written to '{project}'")
    
    with open(project, 'r') as file:
        print(f"Content of '{project}':")
        print(file.read())
    
    with open(project, 'a') as file:
        file.write("\n" + input("Enter new content to append: "))
    print("Content successfully appended to the file.")
    
    confirmation = input(f"Are you sure you want to delete '{project}'? (yes/no): ").strip().lower()
    if confirmation == 'yes':
        import os
        os.remove(project)
        print(f"File '{project}' deleted successfully.")
    else:
        print(f"Deletion of '{project}' canceled.")

if __name__ == "__main__":
    main()
