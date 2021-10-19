"""
Name: Jake Tanner
vigenere.py

Problem: this program encodes text using the vigenere cipher

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *


# opens window
win = GraphWin('Vigenere Cipher', 600, 400)

# creates and draws text prompts in window
message_prompt = Text(Point(150, 100), 'Message to encode:')
key_prompt = Text(Point(189, 150), 'Keyword:')
message_prompt.draw(win)
key_prompt.draw(win)

# creates and draws entry boxes in window
message_entry = Entry(Point(390, 100), 30)
key_entry = Entry(Point(300, 150), 10)
message_entry.draw(win)
key_entry.draw(win)

# creates and draws button for encoding
button_text = Text(Point(300, 280), 'Encode')
button_outline = Rectangle(Point(260, 260), Point(340, 300))
button_text.draw(win)
button_outline.draw(win)

# un-draws button after click
win.getMouse()
button_text.undraw()
button_outline.undraw()

# # stores the message entered
message_text = message_entry.getText()
keyword_text = key_entry.getText()


# encodes plaintext
def code(message, keyword):
    message = message.upper()
    message = message.split(' ')
    acc_m = ''
    for x in message:
        acc_m += x
    message = acc_m

    keyword = keyword.upper()
    keyword = keyword.split(' ')
    acc_k = ''
    for y in keyword:
        acc_k += y
    keyword = acc_k

    ciphered = ''
    for i in range(len(message)):
        character = message[i]
        key = keyword[i % len(keyword)]
        character = ord(character) - 65
        k = ord(key) - 65
        i = character
        i = (i + k) % 26
        c = chr(i + 65)
        ciphered += c
    return ciphered


# draws resulting encoded text
resulting_prompt = Text(Point(300, 280), 'Resulting Message:')
encoded_message = Text(Point(300, 300), code(message_text, keyword_text))
resulting_prompt.draw(win)
encoded_message.draw(win)
close_prompt = Text(Point(300, 370), 'Click anywhere to close')
close_prompt.draw(win)
win.getMouse()
win.close()


def main():
    code(message_text, keyword_text)


if __name__ == '__main__':
    main()
