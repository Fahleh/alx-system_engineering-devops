su betty: switches the current user to the user betty
whoami: Prints the effective username of the current user.
groups: Lists all groups a user is part of
sudo chown betty hello: Changes owner of file hello to betty
touch hello: Creates an empty file named hello in the current directory
chmod u+x hello:Adds execute permission to the owner of the file hello
chmod u+x,g+x,o+r hello: Adds permissions executable to file & group owner and readable to others
chmod ugo+x hello: Adds execution permission to the owner, the group owner and the other users, to the file
chmod 007 hello: Grants full permissons to others and none to both owner and group owner
chmod 753 hello: Grants permission -rwxr-x-wx to file hello
chmod --reference=olleh hello: Mirrors the mode of olleh into hello
chmod -R ugo+x .: Recursively grants full permissions to all subdirectories of the current directory
mkdir -m 751 my_dir: Creates a directory called my_dir with permissions 751 in the working directory.
