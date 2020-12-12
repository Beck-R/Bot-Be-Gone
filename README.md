# Bot-Be-Gone
Bot-Be-Gone/AvailCheck Version 2.1

## Licensing
**THIS SOFTWARE IS MEANT TO BE OPEN-SOURCE AND FREE TO USE. YOU MAY REDISTRIBUTE WITH OR WITHOUT MODIFICATION, HOWEVER YOU MUST RETAIN THIS LICENSING INFORMATION, GIVE CREDIT TO THE ORIGINAL CREATOR(Beck-R). YOU MAY NOT CHARGE ANY FEE WHEN DISTRIBUTING. YOU MAY NOT USE THIS SOFTWARE INTENDING TO USE IT FOR PROFIT, HOWEVER PERSONAL USE IS FINE. NO DISTRIBUTOR OR CONTRIBUTOR IS LIABLE FOR ANY DAMAGES OF ANY TYPE.**

## Authors:
Beck-R

## Thanks:
To all the creators of used third-party modules (listed below)

 1. bs4 (Beautiful Soup)
 2. playsound (Playsound)
 3. colorama (Colorama)
 4. requests (Requests)

## Changelog:

Version 2.1 | Version 2.1 added product availability and error logging. Also made it so you have to put your user agent in the user-info.json

## Installation/Usage:
To use this software just clone the github repo and install the third-party python modules listed in the Thanks section(This will be stream-lined when I figure it out). To get started you will need to open the User-Info.json file (Fig 2).

![enter image description here](https://cdn.discordapp.com/attachments/756610458496139325/781972672682786846/unknown.png)

The first thing you will need to is change the "EMAIL" object to you gmail, right now I am using the smtplib module and I am not quite sure if it supports other types of email services. The next thing is to change the "PASS" object to you gmail's third party app login password I won't be explaining how to do this because there are plenty of videos online, and I would like to keep this relatively simple. The final thing to do in the User-Info.json is to change the "PEMAIL" object to your cellphone carriers email attached to your phone number (examples listed below), 

 1. txt.att.net (AT&T)
 2. tmomail.net (T-Mobile)
 3. vtext.com (Verizon)
 
 ETC. ([here](https://20somethingfinance.com/how-to-send-text-messages-sms-via-email-for-free/) is a good website)

please note that it isn't the one you use to login but something along the lines of 111-222-3333@carrieremailhere. Also it only supports SMS but there are MMS emails listed in the website linked too, MMS will be supported in future updates if they provide a decent benefit. Now that you have that sorted you will need to fill in the information for the Product-Info.json file. Before starting I recommend you read up on how to write a json but you should be okay. The first thing to note that by default there are seven arrays, please note that you can have as many as you want just make sure they are named "GPU" and then a number **STARTING FROM ZERO** and incrementally increasing one number at a time. Please make sure that you are retaining the format of the file and also that you place a comma after each array but not after the last one(Example below)

![enter image description here](https://cdn.discordapp.com/attachments/756610458496139325/782492596169211914/unknown.png)

After you have familiarized yourself with how to write a json file you will need to change the "STORE" object to the store you are buying the product from and enclosed in brackets, this is not super important but it is a good bit of information to have and it makes the output look nice. After this you will want to change the "GPU" object to the name of the product, I will be changing the object to something more universal but it works for now. Then change the "LINK" object to the link of the product you want to scrape **IT IS VERY IMPORTANT FOR THIS TO BE EXACT.** The next thing you need to change is the object "IND" to the class name of the add-to-cart button or availability indicator(Examples below). To find this hit inspect element on the availability indicator on the website and go from there.
 
 1. product-inventory (Newegg)
 2. padding:0 8px (Best-Buy)

After you have pulled out all you hair figuring that out you need to change the object "TYPE" to the class type of the indicator. Examples include: class_, style, span, etc. Currently the program only supports class_ and style but this will be the first change and soon(Mainly because I'm lazy).  Then the final two things to do is to change the object "SOT" object to the string the availability indicator should return when sold-out and then change the "AT" object to the string the availability indicator should return when the product is available. Congratulations if you made it this far, you are now ready to get your ps5s and graphics cards. **IF YOU NEED ANY HELP MAKE A TICKET UNDER THE ISSUES TAB IN GITHUB (I'M NEW TO GITHUB SO I'M NOT REALLY SURE IF THAT'S HOW IT WORKS)**

## BUGS:
Possible issue with the if/else statement in the log() funtion. More testing needed
