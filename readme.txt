
1) Give correct filepath(North/South/IQ).
2) While running using cmd use the following command
	python filename.py arg1 arg2
	arg1----port number(depending on the file from North/South/IQ)  default-2775 for North/
	arg2----month default month is set to 3(March)   
3) If arg1= , 
	case 1:If both the arguemnts are not passed then,the default port number is 2775 and month=3.
	case 2: if only arg1 is passed arg2=3 (march) default value
	case 3 : if both arg1 and arg2 is passed then graph is plotted for specific port number and month 
4)the .png file of graph is stored in file path mentioned.