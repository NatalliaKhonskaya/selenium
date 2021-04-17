# selenium


Note:

1. Selenium requires a driver to interface with the chosen browser.
For Chrome browser the link if following: https://sites.google.com/a/chromium.org/chromedriver/downloads.
P.S. Check the version of Chrome under use you can this way: Chrome -> Help -> About Google Chrome.

2. Then you should be sure that Selenium is installed. 
For installation use the "pip install selenium" in PyCharm's terminal or cmd.

3. API acts as an intermediary for two pieces of software.
Implementing APIs into the code requires two steps:

      a. the script must create a Query with parameter that is sent to the API. 
     To constuct the Query use the Python Request Library ("pip install requests" in PyCharm's terminal)
     
      b. API returns JSON response
