import random

# Lista de palabras para adivinar
words = ["parangaricutirimicuaro", "hexakosioihexekontahexafobia", "hipopotomonstrosesquipedaliofobia",  "electroencefalografista"]

def select_word():
    # Selecciona una palabra al azar de la lista
    return random.choice(words)

def show_board(word, guessed_letters):
    # Muestra el estado actual de la palabra oculta
    board = ""
    for letter in word:
        if letter in guessed_letters:
            board += letter
        else:
            board += "_"
    return board

def show_used_letters(guessed_letters):
    # Muestra las letras que ya se han utilizado
    used_letters = ', '.join(guessed_letters)
    return f"Letras utilizadas: {used_letters}"

def play():
    secret_word = select_word()
    guessed_letters = []
    remaining_attempts = 6

    print("¡Bienvenido al juego del ahorcado!")
    print("Tienes 6 intentos para adivinar la palabra secreta.")
    
    while remaining_attempts > 0:
        board = show_board(secret_word, guessed_letters)
        print("\nPalabra secreta: " + board)
        print(show_used_letters(guessed_letters))
        letter = input("Ingresa una letra: ").lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Ingresa una sola letra válida.")
            continue

        if letter in guessed_letters:
            print("Ya adivinaste esa letra.")
            continue

        guessed_letters.append(letter)

        if letter in secret_word:
            print("Adivinaste una letra correctamente.")
        else:
            remaining_attempts -= 1
            print(f"Letra incorrecta, te quedan {remaining_attempts} intentos.")

        if "_" not in show_board(secret_word, guessed_letters):
            print("\n¡Felicidades! Adivinaste la palabra secreta: " + secret_word)
            break

    if remaining_attempts == 0:
        print("\n¡Has agotado tus intentos! La palabra secreta era: " + secret_word)

play()

