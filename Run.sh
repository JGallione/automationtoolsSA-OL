#!/bin/bash
clear
source ProjectEnv/bin/activate
clear

printf "Choose a Python Script\n"
unset options i
while IFS= read -r -d $'\0' f; do
	options[i++]="$f"
done < <(find ./ -maxdepth 1 -type f -name "*.py" -print0 )
select opt in "${options[@]}" "Exit"; do
  case $opt in
    *.py)
		clear
    	echo "Python file $opt selected..."
		sleep 2
		clear
		python $opt
		break
    	;;
    "Exit")
		clear
    	echo "	Now Exiting..."
    	break
    	;;
    *)
		clear

    	printf "Invalid Entry. Click 'Enter' For File Options\n"
    	
		;;
  esac
done

#each option above ends with a break into the main script
#once logically reaching here the script will clear the terminal and exit
sleep 2
clear
printf "Deactivating Virtual Environment"
deactivate ProjectEnv/bin/activate 
exit 1
