# Codefundo-
Team Name - Two and a half men
Rishabh Jain, Himanshu Goyal, Adithya Iyer
Our aim is to help manage natural disasters and we believe that decreasing losses of human life should be our number one priority in this agenda. With that in mind, we present Save-D, a disaster management app which will have your back when you need it the most, even if no one else does. Our app will allow users to get help, even if they themselves are incapacitated to ask for it. Here’s how:

While initially setting up the app, it will ask for the user‘s name, medical record, phone number, alternate phone number and access to the device’s location. Users will also be asked to fill contact details of 4 people (who will henceforth be addressed as the ‘protectorate’) whom he can rely upon for help if any disaster strikes. These need to be people from different walks of life who are located at different distances from the user so that at least one of them is able to help in times of need.

We aim to use a pre-existing API to get the latest possible news about any disaster/crisis as soon as possible. We then send safety alerts to any user in and around ground zero, confirming his/her well being through a Yes or No question. This can result in 3 possibilities, which are as follows:

1.  If the user responds yes, we go on to ask who all is he/she with (let’s call it the ‘safe list’). The app will provide data regarding places which are comparatively safer and ask whether how he/she will be able to help others. If the user’s response is positive, they will be added to the list of ‘healthy survivors’.  

2. If the user does not respond at all in 10 minutes, this means that there are chances of a very serious situation. In this scenario, the app plays its most crucial role. The app will send the user’s last known location with contact details, the severity of the disaster, user’s medical record and the contact information of some members of the ‘healthy survivors’ list who are closest to the last known location of the user to all members of the protectorate. Meanwhile, the app will run background checks and if the user pops up in anyone else’s safe list, the app will notify the protectorate with the contact information of the person on whose safe list the user has been found. This search will go on until either the user himself responds or if any member of the protectorate can confirm his/her well being.

3. If in a rare case, the user responds ‘no’, then we will present the user with a list of important contact information which can be helpful in such a situation (closest hospital, police station, fire station, etc.). The steps of case 2 will be followed from there on. 

