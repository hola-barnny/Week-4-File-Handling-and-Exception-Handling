import os
from datetime import datetime

def log_operation(message):
    """Logs operations to a file with a timestamp."""
    with open("operations.log", "a") as log_file:
        log_file.write(f"{datetime.now()} - {message}\n")

def process_file(input_filename, output_filename):
    """Reads a file, processes it, and writes the modified content to a new file."""
    try:
        # Check if the input file exists
        if not os.path.exists(input_filename):
            raise FileNotFoundError(f"The file '{input_filename}' does not exist.")
        
        # Read the file content
        with open(input_filename, "r") as file:
            content = file.read()

        # Perform modifications
        modified_content = content.upper()  # Capitalize all text
        word_count = len(content.split())
        unique_word_count = len(set(content.split()))
        
        # Append statistics to the modified content
        modified_content += f"\n\n--- STATISTICS ---\n"
        modified_content += f"Total Words: {word_count}\n"
        modified_content += f"Unique Words: {unique_word_count}\n"

        # Write the modified content to the output file
        with open(output_filename, "w") as file:
            file.write(modified_content)

        # Log success
        log_operation(f"Processed '{input_filename}' and saved to '{output_filename}'")
        print(f"File processed successfully! Modified content written to '{output_filename}'.")

    except FileNotFoundError as e:
        log_operation(f"Error: {str(e)}")
        print(str(e))
    except PermissionError:
        log_operation(f"Error: Permission denied for '{input_filename}'.")
        print(f"Permission denied for '{input_filename}'. Please check your file permissions.")
    except Exception as e:
        log_operation(f"Unexpected error: {str(e)}")
        print(f"An unexpected error occurred: {str(e)}")

def main():
    """Main function to handle user input and process files."""
    print("Welcome to the File Processor 📂")
    
    input_filename = input("Enter the name of the file to read: ").strip()
    output_filename = input("Enter the name of the file to save the modified content: ").strip()

    process_file(input_filename, output_filename)

if __name__ == "__main__":
    main()
