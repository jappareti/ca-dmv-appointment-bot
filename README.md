# DMV Appointment Scheduler
Automated appointment scheduler for California DMV appointments.

## Problem
Appointments at the DMV in California can be booked out months in advance. For example, on August 17, 2017 the earliest appointment for my local DMV office was October 19, 2017 (2+ months). What if I want to go next week? Or maybe tomorrow? Python script powered by `selenium` and `BeautifulSoup` to the rescue!

## Solution
Anyone can cancel a DMV appointment anytime without any retribution so it's easy to assume that slots open up a lot. This script constantly checks for DMV appointments, and if there's an opening for the set date, then it books the appointment.

## Requirements

* Python 3+
* bs4
* selenium
* PhantomJS (optional)

## Setup and Install

* Clone this to your computer (obvi)
* Open up `book_dmv.py` and set your variables at the top. (Note: you'll need to find the code for your DMV location, just open up chrome, go to https://www.dmv.ca.gov/foa/clear.do?goTo=officeVisit&localeName=en, right click on the DMV location dropdown, *Inspect Element*, find for your code corresponding to your DMV office)
* Run `$ python book_dmv.py`
* Wait

## Notes
This script only checks for **exact dates**. Yes it's possible to set it up so that it's smarter (e.g within the next two weeks) but why not be pickier? The first time I ran it, it booked an appointment within 2 mins for a date only 4 days away, but YMMV!

If you don't want to use PhantomJS, then you can change `br = webdriver.PhantomJS()` to `br = webdriver.Firefox()`