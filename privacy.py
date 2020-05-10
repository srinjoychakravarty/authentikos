import os
import gnupg

cwd = os.getcwd()
gpg = gnupg.GPG(gnupghome = cwd)
input_data = gpg.gen_key_input(name_email = 'powerhorse@protonmail.ch', passphrase = "i_love_unicorns")
key = gpg.gen_key(input_data)
print(key)
