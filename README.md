# SAP_challenge

Requirements:

User needs to be able to subscribe the message board.

User needs to be able to unsubscribe from the message board.

The message board can be either public or private. Private message boards require password to subscribe, public ones don't. If the provided password is incorrect, an error should be returned back to the user. (Message board has a pre-determined password. Basic string comparison for password checking is fine, no need for encryption)

At the time of subscription, user needs to be able to specify how they want to be notified of new messages. The following channels are available: Email, WhatApp, SMS.

When a new message is posted to the message board, all subscribers need to be notified via channels they have indicated.

No user interface is required here. The solution should be implemented entirely using classes & built in python data types.

Output should be printed to console using built in methods.

Entire solution should be contained within a single python module. No external communication is required.

User needs to be able to update their subscription preferences after registering.

Provide unit tests with your solution.

## To Run:

The tests rely on the pytest package. Install it with.

pip install -r requirements.txt

run the tests with 

py.test

