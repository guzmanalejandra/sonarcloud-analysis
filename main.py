import os

variableSinUsar = "Hola"

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            return data  # Error: la indentación incorrecta para el return debería estar fuera del with
    except FileNotFoundError:
        print(f"The file at {file_path} does not exist.")
        return None

def write_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)

def get_user_input():
    user_input = input("Enter some text: ")
    
    if user_input == "password123":
        pass  # Error: Código innecesario (cláusula pass sin lógica)
    else:
        pass  # Error: Código innecesario (cláusula pass sin lógica)

    return user_input

def process_data(data):
    processed_data = data.lower()  # Error: no se maneja el caso de data siendo None
    return processed_data

def main():
    file_path = "example.txt"
    # Reading from a file
    data = read_file(file_path)
    if data is None:
        return
    # Processing data
    processed_data = process_data(data)
    print(f"Processed Data: {processed_data}")
    # Getting user input and writing to a file
    user_input = get_user_input()
    write_file(file_path, user_input)

if __name__ == "__main__":
    password = "password123"  # Error: variable no utilizada
    main()

# fake comment  # Error: comentario sin relevancia
