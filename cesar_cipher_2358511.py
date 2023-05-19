def welcome():
    print("Welcome to ceaser cipher.")
    print("This program encrypts and decrypts text with the ceaser cipher.")
    enter_message()
def enter_message():
    e_or_d_val = input("Would you like to encrypt(e) or decrypt(d):")

    if e_or_d_val == 'e':
        encrypt()
    elif e_or_d_val == 'd':
        decrypt()
    else:
        print("Invalid mode")
        enter_message()

    more_ip = input("Would you like to encrypt or decrypt another message? (y/n):")
    if more_ip == 'y':
        enter_message()
    else:
        print("Thanks for using the program, goodbye!")
        exit()

def encrypt():
    enc_list = []
    console_file = input("would you like to read from a file(f) or the console(c)?")
    if console_file == 'c':
        encrypt_message = input("what message would you like to encrypt:")
        encrypt_message = str.upper(encrypt_message)
        shift_val = input("What is the shift number: ")
        for i in range(len(encrypt_message)):
            encrypted_ascii_value = ord(encrypt_message[i])
            if encrypted_ascii_value == 32:
                    encrypted_ascii_value = 32
            else:
                encrypted_ascii_value += int(shift_val)
                if encrypted_ascii_value > 90:
                    encrypted_ascii_value = ((encrypted_ascii_value) % 90 ) + 64 
            encrypted_character = chr(encrypted_ascii_value)
            enc_list.append(encrypted_character)
        
        enc_msg = ''.join(enc_list)
        print("your encrypted message is:", str.upper(enc_msg))
    elif console_file == 'f':
        print('test')
    else:
        enter_message()

def decrypt():
    dec_list = []
    console_file = input("would you like to read from a file(f) or the console(c)?")
    if console_file == 'c':    
        decrypt_message = input("what message would you like to decrypt:")
        shift_val = input("What is the shift number: ")
        for i in range(len(decrypt_message)):
            decrypted_ascii_value = ord(decrypt_message[i])
            if decrypted_ascii_value == 32:
                decrypted_ascii_value = 32
            else:
                decrypted_ascii_value -= int(shift_val)
                if decrypted_ascii_value < 65:
                    decrypted_ascii_value = 91 - ((decrypted_ascii_value) % 65)

            decrypted_character = chr(decrypted_ascii_value)
            dec_list.append(decrypted_character)
        
        dec_msg = ''.join(dec_list)
        print("your encrypted message is:", str.upper(dec_msg))
    elif console_file == 'f':
        print('test')
    else:
        enter_message()

welcome()