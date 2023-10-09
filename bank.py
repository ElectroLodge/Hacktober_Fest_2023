from cryptography.fernet import Fernet

master_password = "root"

mstr_password = input("Enter the master password: ")

if mstr_password == master_password:
    def load_key():
        file = open("key.key", "rb")
        key = file.read()
        file.close()
        return key

    key = load_key()
    fer = Fernet(key)

    def view():
        with open('pwd.txt', 'r') as f:
            for line in f:
                data = line.rstrip()
                user, encrypted_password = data.split("|")
                password = fer.decrypt(encrypted_password.encode()).decode()
                print("Username:", user, "| Password:", password)

    def add_pwd():
        ac = input("Enter your username: ")
        pwd = input("Enter your password: ")
        encrypted_pwd = fer.encrypt(pwd.encode()).decode()
        with open('pwd.txt', 'a') as f:
            f.write(ac + "\t|" + encrypted_pwd + "\n")

    while True:
        mode = input("Would you like to enter your email and password? Type 'Add' to add, 'View' to view existing passwords, and 'q' to quit: ").lower()

        if mode == 'q':
            break
        if mode == 'add':
            add_pwd()
        elif mode == 'view':
            view()
else:
    print("Enter the fkkkinn damm rigght pwd goat .")

#Ok gud , I am heppy doing this w
#Interperter dont print this heheheh
