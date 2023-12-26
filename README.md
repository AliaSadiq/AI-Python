# AI-Python
This GitHub repository serves as a comprehensive collection of Python  code samples that revolve around the fascinating field of Artificial Intelligence (AI).

<b>OnlineComputerShop(week#1):</b>
<br>An online computer shop sells customized personal computers. Every
computer sold includes a basic set of components costing $200 and
additional items can be added.As well as the basic set of components every computer must include one case, one RAM, and one Main Hard Disk Drive from the table.<br>
A computer is supplied with or without an Operating System.<br><br>
Write and test a program or programs for the online computer shop.
Your program or programs must include appropriate prompts for the entry of
data; data must be validated on entry.<br>
Error messages and other outputs need to be set out clearly and understandably.
All arrays, variables, constants and other identifiers must have meaningful names.
You will need to complete these three tasks. Each task must be fully tested.<br>
<b>Task 1 – Setting up the system and ordering the main items.</b>
write program to :
use arrays to store the item code, description and price
allow a customer to choose one case, one RAM and one Main Hard Disk Drive
calculate the price of the computer using the cost of the chosen items and the
basic set of components
store and output the chosen items and the price of the computer.<br>
<b>Task 2 – Ordering additional items.</b>
Extend TASK 1 to:
allow a customer to choose whether to purchase any items from the other
categories – if so, which item(s)
update the price of the computer
store and output the additional items and the new price of the computer.<br>
<b>Task 3 – Offering discounts.</b>
Extend TASK 2 to:
apply a 5% discount to the price of the computer if the customer has bought only
one additional item.
apply a 10% discount to the price of the computer if the customer has bought two
or more additional items.
output the amount of money saved and the new price of the computer after the
discount.

<br><br>
<b> Week #2</b>
An electric mountain railway makes four return trips every day. In each trip, the train
goes up the mountain and back down. The train leaves from the foot of the mountain
at 09:00, 11:00, 13:00, and 15:00. The train returns from the top of the mountain at
10:00, 12:00, 14:00, and 16:00. Each train has six coaches with eighty seats available
in each coach. Passengers can only purchase a return ticket; all tickets must be
purchased on the day of travel. The cost is $25 for the journey up and $25 for the
journey down. Groups of between ten and eighty passengers inclusive get a free ticket
for every tenth passenger, provided they all travel together (every tenth passenger
travels free). Passengers must book their return train journey, as well as the departure
train journey when they purchase their ticket. Passengers can return on the next train
down the mountain or a later train. The last train from the top
of the mountain has two extra coaches on it.
The train times are displayed on a large screen, together with the number of tickets
still available for each train. Every time a ticket is booked the display is updated.
When a train is full, the word ‘Closed’ is displayed instead of the number of tickets
available.
Write and test a program for the electric mountain railway.
Your program or programs must include appropriate prompts for the entry of
data; data must be validated on entry.
Error messages and other outputs need to be set out clearly and understandably.
All variables, constants, and other identifiers must have meaningful names.

You will need to complete these three tasks. Each task must be fully tested.<br>
<b>Task 1 – Start of the day.</b><br>
Write a program to set up the screen display for the start of the day. Initialize suitable
data structure(s) to total passengers for each train journey and total the money taken
for each train journey. Each train journey must be totaled separately. There are four
journeys up and four journeys down every day.<br>
<b>Task 2 – Purchasing tickets.<b><br>
Tickets can be purchased for a single passenger or a group. When making a purchase,
check that the number of tickets for the required train journeys up and down the
mountain is available. If the tickets are available, calculate the total price including
any group discount. Update the screen display and the data for the totals.<br>
<b>Task 3 – End of the day.</b><br>
Display the number of passengers that traveled on each train journey and the total
money taken for each train journey. Calculate and display the total number of
passengers and the total amount of money taken for the day. Find and display the
train journey with the most passengers that day.
<br><br>


Units of electricity consumption are given in the form of a matrix in source data. You are
required to write user-defined functions and create a repeating menu in Python or C++ keeping
in mind the following requirements:
1.The student’s ID should be displayed at the top of the menu.
Press 1 to display the bill of slab 1 and slab 2. (Hint: In slab 1, the unit range is 0 to 100, each
unit costs Rs.10, and the data of slab 1 is in the first row of the matrix. While in slab 2, the
unit range is 101-200, each unit costs Rs.15, and the data of slab 2 is in the second row of
the matrix)
Press 2 to display the bill of slab 3.(Hint: In slab 3, the unit range is 201 to 300, each unit
costs Rs.20, and the data of slab 3 is in the third row of the matrix.)
Press any other key to exit.

<br><br>
<b> Week #3</b>

Hexagon is a geometrical shape having six sides while square is a shape which has four equal sides. You
are required to write Python or C++ program for hexagon and square having data members and
member functions, and create a repeating menu keeping in mind the following requirements:

Consider last digit of your CNIC as the length of one side of hexagon. For example, if your CNIC is
XY210351532, the last digit will be 2.
Calculate area and perimeter of hexagon. (Hint: Area of hexagon= 1.5*1.732*s ; where ‘s’ is the
length of one side of hexagon. Perimeter of hexagon= 6*s; where ‘s’ is the length of one side of
hexagon)
Calculate sum of all the angles of hexagon. (Hint: Sum of all the angles of hexagon= 6*a; where ‘a’ is
the measurement of one angle of hexagon which is equal to 120.)
When the input of user is ‘1’, display area, perimeter and sum of all the angles of hexagon.
Calculate area and perimeter of square whereas;
Length of one side of square=last digit of CNIC + 1. (Hint: Area of square= (length)2; where ‘length’
is the length of one side of square. Perimeter of square= 4*length; where ‘length’ is the length of
one side of the square.)
When the input of user is ‘2’, display the area and perimeter of the square.
On any other input, the program should exit.
Use the last digit of your own CNIC. If you do not use it, your marks will be deducted.
Write member functions to calculate and display area, perimeter, and sum of angles of the hexagon.
The following function names should be used for consistency in the hexagon class.

Write member functions to calculate and display area and perimeter of square. Following function
names should be used for consistency in square class.
Hexagon is a geometrical shape having six sides while square is a shape which has four equal sides. You
are required to write Python or C++ program for hexagon and square having data members and
member functions, and create a repeating menu keeping in mind the following requirements:

Instructions to write the program:

To calculate area of hexagon calcArea();
To calculate Perimeter of hexagon calcPeri();
To calculate Sum of angles of hexagon calcAngleSum();
To display area, perimeter, and sum of
angles of hexagon display();

Write member functions to calculate and display area and perimeter of square. Following function
names should be used for consistency in square class.
To calculate area of Square calcAreaSquare();
To calculate Perimeter of Square calcPeriSquare();
To display area and perimeter of Square display();
<br><br>
<b> Week #4</b>
Consider last digit of your CNIC as the length of one side of hexagon. For example, if your CNIC is
XY210351532, the last digit will be 2.
Calculate area and perimeter of hexagon. (Hint: Area of hexagon= 1.5*1.732*s ; where ‘s’ is the
length of one side of hexagon. Perimeter of hexagon= 6*s; where ‘s’ is the length of one side of
hexagon)
Calculate sum of all the angles of hexagon. (Hint: Sum of all the angles of hexagon= 6*a; where ‘a’ is
the measurement of one angle of hexagon which is equal to 120.)
When the input of user is ‘1’, display area, perimeter and sum of all the angles of hexagon.
Calculate area and perimeter of square whereas;
Length of one side of square=last digit of CNIC + 1. (Hint: Area of square= (length)2; where ‘length’
is the length of one side of square. Perimeter of square= 4*length; where ‘length’ is the length of
one side of the square.)
When the input of user is ‘2’, display the area and perimeter of the square.
On any other input, the program should exit.
Use the last digit of your own CNIC. If you do not use it, your marks will be deducted.
Write member functions to calculate and display area, perimeter, and sum of angles of the hexagon.
The following function names should be used for consistency in the hexagon class.

Write member functions to calculate and display area and perimeter of square. Following function
names should be used for consistency in square class.
Hexagon is a geometrical shape having six sides while square is a shape which has four equal sides. You
are required to write Python or C++ program for hexagon and square having data members and
member functions, and create a repeating menu keeping in mind the following requirements:Write member functions to calculate and display area and perimeter of square. Following function
names should be used for consistency in square class.
<br><br>
<b> Week #5</b>
write a pcode for a game of tictactoe.
<br><br>
<b> Week #6</b>

he manager of a building materials delivery service needs a program to check the contents and
weight of sacks to ensure that correct orders are made up for delivery. A price for the order will be
calculated.
Write and test a program for the manager.
Your program must include appropriate prompts for the entry of data.
Error messages and other output need to be set out clearly.
All variables, constants and other identifiers must have meaningful names.
You will need to complete these three tasks. Each task must be fully tested.
TASK 1 – Check the contents and weight of a single sack
Each sack must obey the following rules to be accepted:
contain cement, gravel or sand, with a letter on the side for easy identification
C - cement
G - gravel
S - sand
sand or gravel must weigh over 49.9 and under 50.1 kilograms
cement must weigh over 24.9 and under 25.1 kilograms
Input and store the weight and contents for one sack. The contents must be checked and an incorrect
sack rejected. The weight must be validated on entry and an overweight or underweight sack rejected.
Output the contents and weight of an accepted sack. If a sack is rejected, output the reason(s).
TASK 2 – Check a customer’s order for delivery
Input and store the number of sacks of each type required for the order. Use TASK 1 to check the
contents and weight of each sack. Ensure that the delivery contains the correct number and type of
sacks for the order.
Output the total weight of the order.
Output the number of sacks rejected from the order.
TASK 3 – Calculate the price for a customer’s order
Extend TASK 2 to calculate a price for an order. Prices for the sacks are as follows:
regular price for each sack
cement, $3
gravel, $2
sand, $2
discount price for a special pack containing 1 sack of cement, 2 sacks of sand and 2 sacks of gravel,
$10
Calculate and output the regular price for the order. Check how many special packs are in the order. If a discount price applies then output the new price for the order and the amount saved
<br><br>
<b> Week #7</b>
The manager of a supermarket needs a program to record donations to charity. Each customer has
the choice of three charities to donate to, and 1% of their shopping bill will be donated to the chosen
charity.
Write and test a program for the manager.
Your program must include appropriate prompts for the entry of data.
Error messages and other outputs need to be set out clearly.
All variables, constants, and other identifiers must have meaningful names.
You will need to complete these three tasks. Each task must be fully tested.
TASK 1 – Set up the donation system
Set up a routine that allows:
the names of three charities to be input and stored
the charity names to be displayed with a number (1, 2 or 3) beside each name
a choice of 1, 2 or 3 to be entered to choose the charity, all other entries rejected
the value of a customer’s shopping bill to be entered
the donation to be calculated
three totals to be set to zero ready to total each charity donation
TASK 2 – Record and total each donation
For a customer’s shopping bill:
input a charity choice of 1, 2 or 3
input the value of a customer’s shopping bill
calculate the donation
add the donation to the appropriate total
Output the name of the charity and the amount donated.
TASK 3 – Show the totals so far
Extend TASK 2 to accept:
donations from more customers
a charity choice of -1 to show the totals so far
Display the charities’ names and the totals in descending order of totals.
Calculate a grand total of all three totals.
Output ‘GRAND TOTAL DONATED TO CHARITY’ and the amount of the grand total.
<br><br>
<b> Week #8</b>

The owner of a river boat hire company wants to calculate the daily profits from hiring out 10 rowing
boats on the river. Boats are numbered 1 to 10. Boats can be hired for use between 10:00 and 17:00
every day.
Write and test a program for the owner.
Your program must include appropriate prompts for the entry of data.
Error messages and other output need to be set out clearly and understandably.
All variables, constants and other identifiers must have meaningful names.
You will need to complete these three tasks. Each task must be fully tested.
TASK 1 – calculate the money taken in a day for one boat.
The cost of hiring a boat is $20 for one hour or $12 for half an hour. When a boat is hired the payment
is added to the money taken for the day. The running total of hours hired that day is updated and the
time when the boat must be returned is stored. At the end of the day the money taken and the total
hours hired is output.
No boat can be hired before 10:00 or returned after 17:00.
TASK 2 – find the next boat available.
Extend TASK 1 to work for all 10 rowing boats. Use the data stored for each boat to find out how
many boats are available for hire at the current time. If no boats are available show the earliest time
that a boat will be available for hire.
TASK 3 – calculate the money taken for all the boats at the end of the day.
At the end of the day use the data stored for each boat to calculate the total amount of money taken
and the total number of hours boats were hired that day. Find out how many boats were not used
that day and which boat was used the most. Provide a report for the owner to show this information.