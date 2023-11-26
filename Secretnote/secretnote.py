import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64


def passwordtokey(password): #ne olduğunu bilmediğim derin işler
    salt ="tuz".encode()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=32
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key


def writecontent():
    fernet = Fernet(passwordtokey(masterkey_entry.get()))
    encryptedText = fernet.encrypt(secret_textbox.get("1.0", tkinter.END).encode())

    try:
        with open("Notes.txt", "x") as d:
            d.write(f"title: {title_entry.get()}\n{encryptedText.decode()}")
    except FileExistsError:
        with open("Notes.txt", "a") as d:
            d.write(f"\ntitle: {title_entry.get()}\n{encryptedText.decode()}")
    finally:
        title_entry.delete(0, tkinter.END)
        secret_textbox.delete(1.0, tkinter.END)


def decryption():
    try:
        fernet = Fernet(passwordtokey(masterkey_entry.get()))
        decryptedtext = fernet.decrypt(secret_textbox.get("1.0", tkinter.END).encode())
        secret_textbox.delete(1.0, tkinter.END)
        secret_textbox.insert("1.0", decryptedtext.decode())
    except:
        messagebox.showerror("Invalid Token", "key - token eşleşmesi yapılamadı")


window = tkinter.Tk()
window.minsize(400, 650)
window.title("Secret Note")


frame = tkinter.Frame(window, pady=30)
frame.pack()
# windows business
my_image = Image.open("Encrypting.jpg")
my_image = my_image.resize((200, 200))
test = ImageTk.PhotoImage(my_image)# photoimage nesnesi olusturuldu (heralde jpeg desteklemesi icin)
my_image_label = tkinter.Label(frame, image=test)
my_image_label.pack()


# Input
# title
title_label = tkinter.Label(text="Enter your title ",)
title_label.pack()
title_entry = tkinter.Entry()
title_entry.pack()
# content
secret_label = tkinter.Label(text="Enter your secret")
secret_label.pack()
secret_textbox = tkinter.Text(width=30, height=12,)
secret_textbox.pack()

# Password
masterkey_label = tkinter.Label(text="Enter your password")
masterkey_label.pack()
masterkey_entry = tkinter.Entry()
masterkey_entry.pack()

# buttons
frame_button = tkinter.Frame(window, pady=10)
frame_button.pack()

encrypt_button = tkinter.Button(frame_button, text="save&encrypt", command=writecontent)
decrypt_button = tkinter.Button(text="decrypt", command=decryption)
encrypt_button.pack()
decrypt_button.pack()


tkinter.mainloop()



