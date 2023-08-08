alias ls="rm *": Creates an alias with name ls and value rm *.
echo 'Hello $USER': Prints hello user, where user is the current Linux user.
PATH=$PATH:/action: Adds /action to the PATH. /action should be the last directory the shell looks into when looking for a program.
echo $PATH | tr ':' '\n' | wc -l: Counts the number of directories in the PATH.
env: Lists environment variables.
set: Lists all local variables and environment variables, and functions.
BEST="School": Creates a new local variable named BEST with value School.
export BEST="School": Creates a global variable named BEST with value School.
echo $((128 + $TRUEKNOWLEDGE)): Prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line.
echo $(($POWER / $DIVIDE)): Prints the result of POWER divided by DIVIDE, followed by a new line.
echo $(($BREATH**$LOVE)): Displays the result of BREATH to the power LOVE.
