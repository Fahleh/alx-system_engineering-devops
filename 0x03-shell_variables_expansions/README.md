alias ls="rm *": Creates an alias with name ls and value rm *.
echo 'Hello $USER': Prints hello user, where user is the current Linux user.
PATH=$PATH:/action: Adds /action to the PATH. /action should be the last directory the shell looks into when looking for a program.
echo $PATH | tr ':' '\n' | wc -l: Counts the number of directories in the PATH.
env: Lists environment variables.
