SERVER STATUS REPORTER

Purpose/Overview
Monitors server status values and reports whether each server is operational. 
This script checks a list of servers and prints either an alert message
or a normal status message based on each server's current condition.

Usage Instructions
Run in Python 3 using the command line. 
python server_status_monitor.py

After running, the script will print the status of every server in the list of servers to be checked.

Configuration Variables
Variable                       Type    Description
DOWN_STATUS = "down"           String  Status for a server that is down
WARNING_STATUS = "warning"     String  Status for a server that is needing attention
servers                        List    Dictionary list of server names and status conditions

Data Structures
list
 {"hostname": "web01", "status": "up"},
   {"hostname": "db01", "status": "down"},
   {"hostname": "app01", "status": "warning"},
   {"hostname": "dns01", "status": "up"}

Logic Overview
This script will be pasted or written into Python3. At which time the results of the script will be printed to the screen. Those results will give you the status of each server that is in the list of registered servers. 

Example Execution Output
web01 is operational
ALERT: db01 is down
WARNING: app01 needs attention
dns01 is operational