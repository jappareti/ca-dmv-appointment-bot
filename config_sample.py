TGT_DATE = 'August 18, 2017'

# You'll need to find the code for your DMV location, just open up chrome,
# go to https://www.dmv.ca.gov/foa/clear.do?goTo=officeVisit&localeName=en
# right click on the DMV location dropdown "Inspect Element"
# find for your code corresponding to your DMV office
OFFICE_ID = '556' # officeid for SF DMV. See HTML code for other office ids
NUMBERITEMS = 'one_task' # number of tasks for dmv; should be 'one_task', 'two_tasks', or 'three_tasks'

# taskDLO = Apply for original driver license
# taskDL = Apply for a California ID card, replacement or renewal of a California driver license 
# taskDLN = Apply for a California driver license and already have a driver license from another state. 
# taskRWT = Return to take another written knowledge test.  
# taskVR = Register or title a vehicle or vessel (boat):
REASONS_FOR_VISIT = ['taskDLO', 'taskDL', 'taskDLN']


FIRSTNAME = 'Bob'
LASTNAME = 'Smith'
DLNUMBER = 'F123456789' # Only if it's a drivers license appointment (taskDL, NOT taskDL0 or taskDLN )
# Number looks like (TELAREA) TELPREFIX-TELSUFFIX
TELAREA = '123'
TELPREFIX = '555'
TELSUFFIX = '1234'