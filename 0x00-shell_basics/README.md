pwd - script to print out the absolute path of the current working directory
ls - script to display the contents list of your current directory.
cd - changes the working directory to the user’s home directory
ls -l - display current directory contents in a long format
ls -al - display current directory contents including hidden
ls -al -n - display current directory contents including group ids
mkdir /tmp/my_first_directory - creates a directory in the tmp directory 
mv /tmp/betty /tmp/my_first_directory - moves the betty file from one direcrtory to another 
rm /tmp/my_first_directory/betty - Delete the file betty
rm -r /tmp/my_first_directory - Delete the directory my_first_directory
cd - - Change working directory to previous one
ls -al . .. - List all files including the parent & boot directories
file /tmp/iamafile - Prints the file type of iamafile
ln -s /bin/ls __ls__ - Creates a symbolic link
cp -u *.html .. - copy html files to parent directory if not found or newer
mv [[:upper:]]* /tmp/u - Move all filers beginning with uppercase
rm *~ - Delete all files ending with ~
mkdir -p welcome/to/school - Creates a directory and its parent directories
ls -a -F -m - Lists the content of working directory separated by a comma
