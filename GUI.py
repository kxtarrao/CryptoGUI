from tkinter import *
import hashlib
from encrpytor import Encryptor


# *****************************************************************
# Functions
# *****************************************************************

def cryptoFunction(file_name, key):
    # Instantiate encryption object and translate key to bytes
    encryptor = Encryptor()

    # Set key
    hashed_byte_key = hashlib.sha1(str.encode(key)).hexdigest()[:32].encode()
    encryptor.set_key(hashed_byte_key)

    try:
        # Decrypt if enc_ header exists
        if (file_name[:4] == "enc_"):
            encryptor.decrypt_file(file_name)
            outputLabel["fg"] = "dark green"
            outputLabel["text"] = "File Successfully Decrypted"
        # Otherwise Encrypt
        else:
            encryptor.encrypt_file(file_name)
            outputLabel["fg"] = "dark green"
            outputLabel["text"] = "File Successfully Encrypted"
    except FileNotFoundError:
        outputLabel["fg"] = "dark red"
        outputLabel["text"] = "File Not Found"
    except ValueError:
        outputLabel["fg"] = "dark red"
        outputLabel["text"] = "Password Incorrect"


# *****************************************************************
# GUI Initialization
# *****************************************************************

# Instantiate Window and set size (canvas) and set frame
Root = Tk()
Canvas = Canvas(Root, height=700, width=800)
Canvas.pack()
Frame = Frame(Root, bg="gray")
Frame.place(anchor="nw", relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

# Set Title
Root.title("AES Symmetric Encryptor")

# *****************************************************************
# GUI Get Key
# *****************************************************************

keyLabel = Label(Frame,
                 bg="dark grey",
                 fg="black",
                 text="Enter Encryption Password"
                 )
keyLabel.place(anchor="n", relx=0.5, rely=0.1, relwidth=0.6, relheight=0.05)

keyText = Entry(Frame,
                bg="white",
                fg="black"
                )
keyText.place(anchor="n", relx=0.5, rely=0.15, relwidth=0.6, relheight=0.05)

# *****************************************************************
# GUI Get Message
# *****************************************************************

messageLabel = Label(Frame,
                     bg="dark grey",
                     fg="black",
                     text="Enter file to Encrypt/Decrypt"
                     )
messageLabel.place(anchor="n", relx=0.5, rely=0.3, relwidth=0.6, relheight=0.05)

messageText = Entry(Frame,
                    bg="white",
                    fg="black"
                    )
messageText.place(anchor="nw", relx=0.2, rely=0.35, relwidth=0.5, relheight=0.05)

messageButton = Button(Frame,
                       text="Enter",
                       fg="black",
                       command=lambda: cryptoFunction(messageText.get(), keyText.get())
                       )
messageButton.place(anchor="nw", relx=0.7, rely=0.35, relwidth=0.1, relheight=0.05)

# *****************************************************************
# GUI Output Window and InfoBox
# *****************************************************************

outputLabel = Label(Frame,
                    bg="dark grey",
                    fg="white",
                    )
outputLabel.place(anchor="n", relx=0.5, rely=0.5, relwidth=0.6, relheight=0.2)

infoBox = Label(Frame,
                    bg="dark grey",
                    fg="black",
                    text="Encrypted Files Must Begin With Header: enc_\n" +
                         "Unencrypted Example File Name: message.txt\n" +
                         "Encrypted Example File Name: message.txt"
                    )
infoBox.place(anchor="n", relx=0.5, rely=0.8, relwidth=0.6, relheight=0.1)

Root.mainloop()
