# -*- coding: utf-8 -*-
# Auther : jianlong
from mysql.connector import connect
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import hashlib
import binascii


def mysql_aes_encrypt(key, data):
    # MySQL AES uses a 16-byte key derived from the input key using MD5
    key_hash = hashlib.md5(key.encode('utf-8')).digest()

    # Generate a 16-byte IV of zeros (MySQL uses a zeroed IV for AES)
    iv = b'\x00' * 16

    # Create a Cipher object using AES in CBC mode
    cipher = Cipher(algorithms.AES(key_hash), modes.CBC(iv), backend=default_backend())

    # Pad the data to ensure it's a multiple of the block size (16 bytes)
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data.encode('utf-8')) + padder.finalize()

    # Encrypt the data
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Convert the ciphertext to a hexadecimal string
    return binascii.hexlify(ciphertext).decode('utf-8')


def mysql_aes_decrypt(key, hex_ciphertext):
    # MySQL AES uses a 16-byte key derived from the input key using MD5
    key_hash = hashlib.md5(key.encode('utf-8')).digest()

    # Generate a 16-byte IV of zeros (MySQL uses a zeroed IV for AES)
    iv = b'\x00' * 16

    # Convert the hex ciphertext back to binary
    ciphertext = binascii.unhexlify(hex_ciphertext)

    # Create a Cipher object using AES in CBC mode
    cipher = Cipher(algorithms.AES(key_hash), modes.CBC(iv), backend=default_backend())

    # Decrypt the data
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()

    # Unpad the decrypted data
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()

    # Convert the data back to a string and return it
    return data.decode('utf-8')


if __name__ == '__main__':
    try:
        con = connect(
            host='localhost',
            port=3306,
            user='root',
            password='Jianlong123.',
            database='vega'
        )
        con.start_transaction()
        sql = 'insert into t_user(username,password,email,role_id)' \
              ' values(%s,%s,%s,%s)'
        password = mysql_aes_encrypt('jianlong', '328852')
        cursor = con.cursor()
        # cursor.execute(sql, ('小郭', password, '328852120@qq.com', 2))

        con.commit()
    except Exception as e:
        if 'con' in dir():
            con.rollback()
        print(e)

    finally:
        if 'con' in dir():
            con.close()
