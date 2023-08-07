echo 'Hello, World': Script to print “Hello, World”, followed by a new line to the standard output.
echo '\"(Ôo)'": Script that displays a confused smiley.
cat /etc/passwd: Displays the content of the /etc/passwd file.
cat /etc/passwd /etc/hosts: Display the content of /etc/passwd and /etc/hosts.
tail -n 10 /etc/passwd: Displays the last 10 lines of /etc/passwd.
head -n 10 /etc/passwd: Displays the first 10 lines of /etc/passwd.
awk 'FNR==3 {print}' iacta: Displays the third line of the file iacta.
echo 'Best School' > \\\*\\\\"'\"Best School\"\\'"\\\\\*\$\\\?\\\*\\\*\\\*\\\*\\\*\:\): Creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line.
ls -la > ls_cwd_content: Writes into the file ls_cwd_content the result of the command ls -la
tail -n 1 iacta >> iacta: Duplicates the last line of the file iacta.
find . -type f -name '*.js' -delete: Deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.
find . -mindepth 1 -type d | wc -l: Counts the number of directories and sub-directories in the current directory.
ls -t1 | head -n 10: Displays the 10 newest files in the current directory.
sort | uniq -u: Takes a list of words as input and prints only words that appear exactly once.
grep -i "root" /etc/passwd: Displays lines containing the pattern “root” from the file /etc/passwd.
grep -c -i 'bin' /etc/passwd: Displays the number of lines that contain the pattern “bin” in the file /etc/passwd.
grep -i 'root' -A 3 /etc/passwd: Displays lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.
grep -i -v 'bin' /etc/passwd: Displays all the lines in the file /etc/passwd that do not contain the pattern “bin”
grep -i '^[a-z]' /etc/ssh/sshd_config: Displays all lines of the file /etc/ssh/sshd_config starting with a letter.
sed 's/A/Z/g; s/c/e/g': Replaces all characters A and c from input to Z and e respectively.
tr -d "cC": Removes all letters c and C from input
