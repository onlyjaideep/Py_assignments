#write and append data to a file
try:
    # Data to write to the file
    user_input = input("Enter data to write to output.txt (e.g., 25): ")
    
    with open('output.txt', 'w') as file:
        file.write(user_input + "\n")
    
    # 2. Appends additional data to the same file.
    additional_data = "Data successfully appended in step 2."
    
    # Open the file in 'append' mode ('a'). This adds content to the end.
    with open('output.txt', 'a') as file:
        file.write(additional_data + "\n")
        
    # 3. Reads and displays the final content of the file.
    print("\n--- Reading Final Content of output.txt ---")
    
    # Open the file in 'read' mode ('r') to display contents.
    with open('output.txt', 'r') as file:
        final_content = file.read()
        print(final_content)
    print("------------------------------------------")
except IOError:
    print("An error occurred while handling the file.")