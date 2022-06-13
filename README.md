# CLI-Password-Generator
Advanced Password Generator to generate passwords in Terminal that stores the passwords in a file.

# Why should I prefer this than already others available ?
This Password Generator generates passwords and stores them with the time of generation in case you get confused.

# Where are the passwords stored ?
The passwords are stored in `generated_password.txt` in the current working directory. 
(The same place where the script is located.)

The format is `password : dd/mm/yyyy hh:mm:ss` where `dd/mm/yyyy` = date and `hh:mm:ss` = time of generation.

# Where are the hashed passwords stored ? (Optional Feature)
The hashes are store in `hashed_password.txt` incase you wanted to see the hashes again.

# Are there any password generation limitations ?

There are no password generation limitations. You can generate password as long as your Computer can handle.

# Is this a good way to store passwords

No, storing passwords in a unencrypted file is not a good way to store passwords.

You can copy the contents of the file and paste it in a file that is password encrypted.
