#!/bin/bash

#@Author DD7600
#Date 27/09/2021
#FINISH AT 15/10/2021

##COLOR
GRENN="\033[0;32m"
BLUE="\033[0;34m"
NORMAL="\033[0;00m"
RED="\033[0;31m"
PURPLE="\033[0;35m"


##VARIABLES

#INTEGER
answer=0
number=0
compteur=0
end=0
niveau=0
next=10
numberTry=3
try=1

##STRING

#essai="$RED $numberTry Tries YOU LOST $NORMAL "
quit="$GRENN YOU QUIT, BYE!\n $NORMAL"
win="YOU, WIN "
guest="$GRENN Try again:$NORMAL"
petit="$PURPLE **YOUR NUMBER IS TOO LOW** $NORMAL  "
grand="$PURPLE **YOUR NUMBER IS TOO HIGH** $NORMAL "



##Function game
game () {



 


while [  $answer -ne -1  ];do


#choose random number
number=$((RANDOM % next))
echo -e $GRENN
figlet -c LEVEL ${niveau}
echo -e $NORMAL

echo -e "$GRENN hey!i'm the computer can you guess my number?between: 0 and $next (number  of try : $numberTry )$NORMAL"

#INPUT

read -p "?->" answer

while [ $answer -ne $number ] && [ $end -ne -1 ];do



#LOST
if [ $try -eq $numberTry ];then

		echo -e "$RED $numberTry Tries YOU LOST $NORMAL "

		echo -e "$GRENNMy number was $number$NORMAL"
		try=1
		compteur=0
		break
fi
##TO QUIT
if [ $answer -eq -1 ];then
		echo -e $quit
		echo -e "$GRENNMy number was $number$NORMAL"
end=-1

else
##NUMBER TO LOW
if [ $answer -lt $number ];then

		echo -e $petit
		
		let "compteur++"
		let  "try++"
##NUMBER TO HIGH
elif [ $answer -gt $number ];then
		echo -e $grand
		let "compteur++"
		let  "try++"
		
fi
##TRY AGAIN
echo -e "$RED try again,you have $((numberTry - compteur)) tries left"
echo -e $guest
read -p "?->" answer
fi
done

##WIN
if [ $answer -eq $number ];then
		echo -e $BLEU
		echo -e $win | cowsay
		echo -e $NORMAL
		let "niveau++"
		let "numberTry++"
		next=$((next + 10))
		try=1
		compteur=0


fi
done

}

##FIN

##WELCOME MESSAGE
echo -e "$GRENN ******************************************************************************" 
figlet -c GUESS NUMBER GAME
echo "*********************************************************************************"
echo -e "$NORMAL " 

goal="$GRENN//////////////////////////////////////////////////////////////////////////////////////////\nthis game is guess the number , the computer chooses a Positive number and you have to find it you have 3 tries  and at each level the number of  try increase by 1 \n
Press: -1 to quit \n//////////////\
///////////////////////////////////////////////////////////////\n"




#START PROCESS
echo -e $goal

#function call
game


