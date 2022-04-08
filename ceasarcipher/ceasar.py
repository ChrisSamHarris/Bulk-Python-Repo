#alphabet duplicated in order to ensure we can shift latter letters i.e. 'Zulu' 

import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
txt = input("Type your message:\n").lower()
shft = int(input("Type the shift number:\n"))

# The modulus will stop us exceeding any daft characters or patterns of shift 
shft = shft % 26
encoded_text = ""

end_encryption = False
def encrypt(text, shift):
      cipher_text = ""
      for char in text:
        if char in alphabet:
          position = alphabet.index(char)
          new_position = position + shift
          new_char = alphabet[new_position]
          cipher_text += new_char
        else:
          cipher_text += char
      print(f"The encoded text is {cipher_text}")
def decrypt(text, shift):
      cipher_text = ""
      for char in text:
        if char in alphabet:
          position = alphabet.index(char)
          new_position = position - shift
          new_char = alphabet[new_position]
          cipher_text += new_char
        else:
          cipher_text += char
      print(f"The decoded text is {cipher_text}")
      

while end_encryption == False:
  if shft >= 27:
    end_encryption = True
    print("You shifted too much!")
  elif shft <= 26 and direction == "encode":
    encrypt(txt, shft)
    end_encryption = True
  elif direction == "decode":
    decrypt(txt, shft)
    end_encryption = True
  #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

# ===== Redacted code: =====
# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#     shift_amount *= -1
#   for char in start_text:
#     if char in alphabet:
#       position = alphabet.index(char)
#       new_position = position + shift_amount
#       end_text += alphabet[new_position]
#     else:
#       end_text += char
#   print(f"Here's the {cipher_direction}d result: {end_text}")

# from art import logo
# print(logo)


# should_end = False
# while not should_end:

#   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#   text = input("Type your message:\n").lower()
#   shift = int(input("Type the shift number:\n"))

#   shift = shift % 26

#   caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

#   restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
#   if restart == "no":
#     should_end = True
#     print("Goodbye")