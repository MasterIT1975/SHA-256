import hashlib

def encrypt(message, key):
    # Хэшируем ключ с использованием SHA-256
    hashed_key = hashlib.sha256(key.encode()).hexdigest()

    # Преобразуем ключ в байты
    key_bytes = bytes.fromhex(hashed_key)

    # Преобразуем сообщение в байты
    message_bytes = message.encode()

    # XOR операция между байтами сообщения и ключа
    encrypted_bytes = bytes(x ^ y for x, y in zip(message_bytes, key_bytes))

    # Возвращаем зашифрованное сообщение в виде шестнадцатеричной строки
    return encrypted_bytes.hex()

def decrypt(encrypted_message, key):
    # Хэшируем ключ с использованием SHA-256
    hashed_key = hashlib.sha256(key.encode()).hexdigest()

    # Преобразуем ключ в байты
    key_bytes = bytes.fromhex(hashed_key)

    # Преобразуем зашифрованное сообщение из шестнадцатеричной строки в байты
    encrypted_bytes = bytes.fromhex(encrypted_message)

    # XOR операция между байтами зашифрованного сообщения и ключа
    decrypted_bytes = bytes(x ^ y for x, y in zip(encrypted_bytes, key_bytes))

    # Возвращаем дешифрованное сообщение в виде строки
    return decrypted_bytes.decode()

# Ввод текста и ключа для шифрования
message = input("Введите текст для шифрования: ")
encryption_key = input("Введите ключ для шифрования: ")

# Шифруем сообщение
encrypted_message = encrypt(message, encryption_key)
print(f"Зашифрованное сообщение: {encrypted_message}")

# Ввод ключа для дешифрования
decryption_key = input("Введите ключ для дешифрования: ")

# Дешифруем сообщение
decrypted_message = decrypt(encrypted_message, decryption_key)
print(f"Дешифрованное сообщение: {decrypted_message}")
