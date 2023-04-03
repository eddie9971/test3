alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
     'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, the 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
     cipher_text = ''
     for letter in plain_text:
          position = alphabet.index(letter)
          new_position = position + shift_amount
          if new_position > 26:
               new_position -= 26
          new_letter = alphabet[new_position]
          cipher_text += new_letter

     print(f"The encoded text is {cipher_text}")
     return cipher_text


def decrypt(cipher_text, shift_amount):
     decipher_text = ''
     for letter in cipher_text:
          position = alphabet.index(letter)
          new_position = position - shift_amount
          if new_position < 0:
               new_position += 26
          new_letter = alphabet[new_position]
          decipher_text += new_letter

     print(f"The decoded text is {decipher_text}")
     return decipher_text


def caesar(start_text, shift_amount, cipher_direction):
     end_text = ''
     if cipher_direction == 'decode':
          shift_amount *= -1
     for char in start_text:
          if char in alphabet:
               position = alphabet.index(char)
               new_position = position + shift_amount
               end_text += alphabet[new_position]
          else:
               end_text += char
     print(f'The {cipher_direction} text is {end_text}')


if direction == 'encode':
     encrypt(text, shift)
elif direction =='decode':
     decrypt(text, shift)


