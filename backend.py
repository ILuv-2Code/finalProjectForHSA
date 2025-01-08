# Port Scanner
from flask import Flask, request, render_template, url_for

# Port Scanner
import requests
from bs4 import BeautifulSoup
import re

# Port Scanner
import socket
from queue import Queue
import threading 




app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        return render_template('index.html')

    else:
        return render_template('index.html')
        

@app.route('/aboutUs.html')
def aboutUs():
    return render_template('aboutUs.html')


@app.route('/parser.html', methods=["POST", "GET"])
def parser():
    if request.method == "POST":
        linkToParce = request.form.get("parce_Link")
        
    # Function Fun
        parseURL = requests.get(linkToParce)
    
    ## Status Code, Indicates the Website Availability
#       print("Status Code:", parseURL.status_code)
    ## This is the actual parser, information gathered from the website (parseURL)
        soup = BeautifulSoup(parseURL.content, 'html.parser')
    
    # This is just the information gathered
        try:
        ## Website Title
            website = soup.title.text
        #---------#
        ## Links
        
#            print('Wesbite Links:\n')
            linkList = []
            for link in soup.find_all('a'):
                linkPrint = link.get('href')
                if "https" in linkPrint and linkPrint not in linkList:
                    linkList.append(linkPrint)
            linkString = "\n".join(linkList)
                
        
        ## Phone Numbers
#            print("Phone Numbers: ")
            phoneTXT = soup.html.find_all('p')
            phoneRegex = '\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}'
            Phonematch = re.findall(phoneRegex, str(phoneTXT))
            phoneTOTAL = "\n|\n".join(Phonematch)

        ## Emails
#            print("Emails: ")
            emailTXT = soup.html.find_all('p')
            emailRegex = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
            Emailmatch = re.findall(emailRegex, str(emailTXT))
        except: 
            None

        # Posting info on page
        websitePOST = website
        webLinksPOST = linkString
        phonePOST = phoneTOTAL
        emailPOST = Emailmatch


        return render_template('parser.html', websitePOSTED=websitePOST, linksPOSTED=webLinksPOST, phonePOSTED=phonePOST,emailPOSTED=emailPOST)

    else:
        return render_template("parser.html")

@app.route('/portScanner.html', methods=["POST", "GET"])
def portScan():
    
    ## Function Stuff
    queue = Queue()
    openPorts = []


    def portScanner(target, port):
        try:
            sock = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
            sock.connect((target, port))
            return True
        except:
            None

    def fillQueue(portList):
        for port in portList:
            queue.put(port)

    def worker(): 
        while not queue.empty():
            port = queue.get()
            if portScanner(target, port) == True:
                print('Port Open: ', str(port))
                openPorts.append(port)


    threadList = []

    for t in range(10):
        thread = threading.Thread(target=worker)
        threadList.append(thread)

    for thread in threadList:
        thread.start()

    for thread in threadList:
        thread.join()

#    print('Open Ports are: ', openPorts)

    if request.method == "POST":
        
        ipAddr = request.form.get('ip_ADDRESS')
        ipPort = request.form.get('ip_PORT')
        
        addrPOST = ipAddr 
        portsPOST = ipPort  
    

    # Function Stuff Actual
        target = str(ipAddr)


        portList = range(1, int(ipPort))
        fillQueue(portList)

        threadList = []

        for t in range(100):
            thread = threading.Thread(target=worker)
            threadList.append(thread)

        for thread in threadList:
            thread.start()

        for thread in threadList:
            thread.join()
        
        openPORTSPOST = openPorts
        

        return render_template('portScan.html', addrPOSTED=addrPOST, portsPOSTED=portsPOST, openPORTSPOSTED=openPORTSPOST)



    else:    
        return render_template('portScan.html')

    

 
if __name__=='__main__':
   app.run(debug=True)