# elpscrk - Mr.Robot

Brute Force & Password Generating Program from Mr.Robot

**PC & iOS Useable!**

Elpscrk v4 is a mix of my 2 programs `elpscrkv3` and `RoBrutev8`!
This new edition includes automated brute force attacks; meaning
all you have to do is plug in the target and elpscrk will scan for
ssh, http, https, and http-alt and then proceed to brute force!
Scanning checks for key elements in the HTML of the target website
and proceeds to identify them inorder to figure out what post data
must be submitted!

***Usage:***

**root@elliot$** `elpscrk -list <file>.list-add <keyword>; <unlimited keywords>`

**root@elliot$** `elpscrk -ip <domain/ip> -usr <username> -psw <password file>`

***Outputs:***

**root@elliot$** `Scanning Complete`   <- This means the program has finished finding the attack vectors!

**root@elliot$** `<HTTP|HTTPS|SSH|HTTP-ALT> Vector`   <- This means the program has found a successful login!

**root@elliot$** `Password: <Successful Password>` 

***Errors:***

**root@elliot$** `Invalid`   <- This means you screwed up the commands horribly! :D

**root@elliot$** `Unable/No Login Services`   <- Program was unable to find attackable vectors

**root@elliot$** `Successfully Failed`   <- Program went through all the passwords and none of them worked!
