def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts text using Caesar Cipher.
    """
    # Normalize shift: positive for encrypt, negative for decrypt, modulo 26
    shift = shift % 26 if mode == 'encrypt' else -(shift % 26)
    
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result


def main():
    print("=== Caesar Cipher Program ===")
    print("This program can encrypt and decrypt messages using the Caesar Cipher.\n")
    
    while True:
        print("-" * 50)
        print("Choose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Quit")
        print("-" * 50)
        
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == '3':
            print("\nGoodbye!")
            break
        elif choice not in ['1', '2']:
            print("\nInvalid choice. Please enter 1, 2, or 3.\n")
            continue
        
        # Determine mode
        if choice == '1':
            mode = 'encrypt'
            action = "Encrypted"
        else:
            mode = 'decrypt'
            action = "Decrypted"
        
        # Get shift value
        while True:
            try:
                shift_input = int(input("\nEnter the shift value (any positive integer): "))
                if shift_input < 0:
                    print("Please enter a non-negative integer.")
                    continue
                break
            except ValueError:
                print("Please enter a valid integer for shift.")
        
        # Get message
        message = input("Enter your message: ")
        
        # Process
        result = caesar_cipher(message, shift_input, mode)
        
        print(f"\n{action} message:\n{result}")
        
        # Verification
        reverse_mode = 'decrypt' if mode == 'encrypt' else 'encrypt'
        reverse_result = caesar_cipher(result, shift_input, reverse_mode)
        print(f"\nVerification: reversing gives back:\n{reverse_result}")
        
        if reverse_result == message:
            print("✓ Verification successful!\n")
        else:
            print("✗ Verification failed!\n")
        
        # The loop will show the menu again automatically


if __name__ == "__main__":
    main()