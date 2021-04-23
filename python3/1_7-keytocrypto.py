cipher = input()
key = input()
A_ASCII = ord('A')
message = ""

for index, cipher_char in enumerate(cipher):
  diff = ord(key[index]) - A_ASCII
  message_char = chr((ord(cipher_char) - diff - A_ASCII) % 26 + A_ASCII)

  key += message_char
  message += message_char

print(message)
