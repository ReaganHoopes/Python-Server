# Python-Server

What this project is:
  - For this project I wrote an HTTP server in Python using the standard http.server library. 
  - The server responds to GET requests and serves the dummy website I created to the web browser.
  - My website was created to utilize a wide range of HTML and CSS properties and selectors.
  - The website is interconnected and utilizes abolute and relative URLs.
 
Languages used:
  - Python
  - HTML
  - CSS
 
How to run the server:
  - From the command line navigate to the directory containing server.py
  - To make server auto-restart run command $ while sleep .25; do python server.py; echo Restarting...; done
  - Going to your browser and going to http://localhost:8000/ will redirect you to the main page of the dummy site
  - You can view live requests in the shell
  - Hit Ctrl-C twice quickly to break out of the loop and disconnect from the server
