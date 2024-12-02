import os

def read_and_modify_file(input_filename, output_filename):
    # Check if the input file exists before proceeding
    if not os.path.exists(input_filename):
        print(f"Error: The file '{input_filename}' does not exist.")
        return

    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()  # Modify as needed

        # Write the modified content to a new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to {output_filename}")

    except IOError:
        print("Error: There was a problem reading or writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def handle_file_error():
    while True:
        filename = input("Please enter the filename: ")

        # Check if the file exists before trying to open it
        if not os.path.exists(filename):
            print(f"Error: The file '{filename}' does not exist. Please try again.")
        else:
            try:
                # Try opening the file
                with open(filename, 'r') as file:
                    content = file.read()
                    print("File contents:\n")
                    print(content)
                break  # Exit the loop if the file is successfully read
            except IOError:
                print(f"Error: The file '{filename}' could not be read.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                break

# Example usage
input_filename = "example.txt"  # Input file name
output_filename = "modified_example.txt"  # Output file name
read_and_modify_file(input_filename, output_filename)
handle_file_error()


#Error Handling Lab
import os

def handle_file_error():
    while True:
        filename = input("Please enter the filename: ")

        # Check if the file exists before trying to open it
        if not os.path.exists(filename):
            print(f"Error: The file '{filename}' does not exist. Please try again.")
        else:
            try:
                # Try opening the file
                with open(filename, 'r') as file:
                    content = file.read()
                    print("File contents:\n")
                    print(content)
                break  # Exit the loop if the file is successfully read
            except IOError:
                print(f"Error: The file '{filename}' could not be read.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                break

# Call the function to test
handle_file_error()
