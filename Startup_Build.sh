#!/bin/bash

#keep it clean
clear 

#checking to see if the virtual environment named /ProjectEnv exists
if  [ -d  "./ProjectEnv" ];then 
	printf "\n\n\n\n"
	printf "	Project Environment Already Exist..."
	printf "\n"
	sleep 2
	clear
else

#if /ProjectEnv does not exist we will make sure we have Virtualenv installed... 
	printf "\n\n\n\n"
	printf "	Building Project Environment..."
	printf "\n"
	sleep 2
	clear
	pip install Virtualenv
	clear

#then we will be running Virtualenv to create /ProjectEnv 
	printf "\n\n\n\n"
	printf "	Please Wait..."
	printf "\n"
	sleep 2
	clear
	Virtualenv ProjectEnv
	clear
fi

#activating our virtual environment /ProjectEnv
printf "\n\n\n\n"
printf "	Activating Virtual Environment..."
printf "\n"
sleep 2
clear

source ProjectEnv/bin/activate
clear
printf "\n\n\n\n"
printf "	Virtual Environment Activated!"
printf "\n"
sleep 2
clear

#naming the dependencies for user consent 
printf "		The Following Dependenies are ~__MB. \n"
printf "	-selenium\n"
printf "	-smtplib\n"
read -r -p  "		Are You Sure? [Y/n] " input

#user consent
case $input in
    [yY][eE][sS]|[yY])
printf "		Downloading Dependenes" 
sleep 1 
printf "." 
sleep 1 
printf "." 
sleep 1 
printf "." 
sleep 1
clear 

python get-pip.py

#checking and installing python packages
package_exist(){
    package=$1
    if pip freeze | grep $package=;then
        echo "$package Installed"
    else
        pip install $package
    fi
}

sleep 1
package_exist selenium
package_exist smtplib
sleep 1
clear
printf "\n\n\n\n	All Dependencies Have Been Installed!\n"
sleep 3
clear
;;
    [nN][oO]|[nN])
 clear
 echo "		Build file will now close!"
 sleep 2
 clear
 exit 1
;;
 *)
 clear
 echo "Invalid input..."
 exit 1
 ;;
esac

#	now that we made sure that the proper depedencies have 
#been installed in our VE.
#	we can choose which python script we would like to run
#withen the current directory.
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
deactivate ProjectEnv/bin/activate
exit 1