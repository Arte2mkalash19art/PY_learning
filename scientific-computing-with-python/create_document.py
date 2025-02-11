message = input('Введіть текст (якщо хочете зашифрувати) або шифр (якщо хочете розшифрувати): ') 
custom_key = input('Введіть ключ до шифру: ')
mode = input('Введіть "e" для шифрування або "d" для розшифрування: ').lower()

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet_eng = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_ua = 'абвгґдежзийклмнопрстуфхцчшщьюя'
    final_message = ''

    for char in message.lower():
        if char in alphabet_eng:
            alphabet = alphabet_eng
        elif char in alphabet_ua:
            alphabet = alphabet_ua
        else:
            final_message += char
            continue

        key_char = key[key_index % len(key)]
        key_index += 1

        if key_char in alphabet_eng:
            key_alphabet = alphabet_eng
        elif key_char in alphabet_ua:
            key_alphabet = alphabet_ua
        else:
            continue
        offset = key_alphabet.index(key_char)
        index = alphabet.find(char)
        new_index = (index + offset * direction) % len(alphabet)
        final_message += alphabet[new_index]

    return final_message

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)

if mode == "e":
    encrypted_text = encrypt(message, custom_key)
    print(f'Зашифрований текст: {encrypted_text}')
elif mode == "d":
    decrypted_text = decrypt(message, custom_key)
    print(f'Розшифрований текст: {decrypted_text}')
else:
    print('Невірний режим, введіть "e" або "d".')
