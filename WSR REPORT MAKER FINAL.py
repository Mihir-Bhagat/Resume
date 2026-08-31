
So i wanted to make a automation where i have this column names 

Specif team Name
User Status
Category 1- schema 1
ID
Transaction Descr.
Priority Text
Posting Date
IN Negociated Date
Category 2- schema 2
GCC Bus. Con. Name
External Reference No.
IN Successor ID
IN Successor Status
Release Cycle ID
Maint Cycle ID
IN First nego Date
Requirement From
ChaRM Project
Budget Project
Business Caller Name
Requester Name
Change date
Last status change
IN Creation Date Boss
IN Negociated Date2
IN Completion Date
IN Awaiting Date
IT Post Activity
Technical complexity
ChaRM Status
ChaRM status descr​‌


i want to make an automation such that when ever i will upload a file 
it will put the filter on Specif team Name and select only values which contain FTS and then put the filter on User Status and select only the values which are IN01 New

Now i will have few values which are received by using this filter now i have to add this value to the main data which will have same fields now the real thing begins 

i will have to create a pivot tables in excel ALL THE BELOW 3 TABLES SHOULD BE IN THE TAB CALLED AS PIVOT
1. Charm Status As Per PAs
for making this pivot table i want you to make a table with the rows should be Specif team Name and ChaRM status descr​‌

values should have Count of ID 
also there should be filter on ChaRM status descr​‌ ir should not contain this value starting with 40 , 98 , 02

2.Overall Status Of Pas
for making this pivot table i want you to make a table with the 
Filter on ChaRM status descr​‌ should not contain this value starting with 40 , 98 , 02
rows Specif team Name
Values Count of ID

3.Overall Charm Status
for making this pivot table i want you to make a table with the 
rows ChaRM status descr​‌
Values Count of ID

BELOW TABLE SHOULD BE IN THE TAB CALLED AS TREND
for trend i have a tab where it is called as trend I HAVE TO ADD TODAYS DATE AND COUNT OF THAT 
Specif team NamE IF TODAYS VALUE IF VALUE IS MORE THAN YESTERDAY IT IS NEGATIVE IF IT IS SAME NO CHANGE IF IT IS LESS THEN POSITIVE I HAVE ATTACHED THE PICTURE FOR YOUR REFERENCE 

THE BELOW TAB SHOULD BE CALLED AS Status last Update
the table should have the following 
Filter should have ChaRM status descr​‌ here do not remove values which start from with 40 , 98 , 02 include everything 
Rows should have  Specif team Name , ID , GCC Bus. Con. Name ,Last status change

now how should be the gui 
Gui should have 2 options one to add the new data one to add the master data which will have trend value you just have to add todays data to the whole data and make a trend and all the pivot 

also there should be option in gui to open a draft in outlook which should be able to reply all to specific mail 
so the subject should be 
SSM Report 27th August this should change like SSM Report [Date Month] it should be todays data and month
body should contain 

Hello 
this is the example 
Please Find SSM Report for 27th August 2026, at 10:30 IST.

then it should contain this tables 
Trend View:

Charm Status As Per PA’s:


Overall Charm Status:
