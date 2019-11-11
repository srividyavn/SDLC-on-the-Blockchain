from flask import Flask, render_template, request, redirect
import requests
import json 
import random
import os
import dateutil.parser

app = Flask(__name__)

# Helper function to parse the raw string from the Blockchain
def myOwnerFunc(newOwner):
	return newOwner.split("#")[1].title()

# Helper function to get the current state of the Order asset
def myFunc(orderId):
	r = requests.get('http://localhost:3000/api/Order')
	try:
		json_val = r.json()[0]['state']
	except:
		json_val = " "
	return(str(json_val).title())

# Helper function to parse a raw timestamp to a desired format of "H:M:S dd/mm/yyy"
def myChangeFunc(timestamp):
	t = dateutil.parser.parse(timestamp)
	finalT = t.strftime("%H:%M:%S %d/%m/%Y")
	return finalT

# This allows using the above 3 functions in-line from the HTML templates 
app.jinja_env.globals.update(myFunc=myFunc) 
app.jinja_env.globals.update(myChangeFunc=myChangeFunc) 
app.jinja_env.globals.update(myOwnerFunc=myOwnerFunc) 

# Route: index page
@app.route("/")
@app.route("/index")
def index():
	return render_template('index.html')

# Route: company page
@app.route("/company")
def company():
	print("Hello!")
	r = requests.get('http://localhost:3000/api/ChangeOwner') 
	if r.json()==None or r.json()=={}:
		transactions = {}
	else:
		transactions = r.json()
	return render_template('company.html', title="Company", transactions=transactions)

# Route: submitOrder transaction
@app.route("/submitOrder", methods=['POST', 'GET'])
def submitOrder():
	state_info = request.form['state'].encode('utf-8').lower()
	if(state_info=="production"):
		json_val = {
			  "$class": "org.acme.howto.Order",
			  "orderId": "0rd3r",
			  "timestamp": request.form['timestamp'].encode('utf-8'),
			  "date": request.form['date'].encode('utf-8'),
			  "state": request.form['state'].encode('utf-8').lower(),
			  "owner": "company"
			}	
		transactions_val = {
			  "$class": "org.acme.howto.ChangeStateTo"+state_info.title(),
			  "order": "0rd3r"
			}
		# Making 2 POST requests with JSON data as a parameter 
		# POST Request 1: Create a new Order element with its respective fields 
		r = requests.post('http://localhost:3000/api/Order', data=json_val)
		# POST Request 2: Issue a ChangeStateToProduction transaction
		rT = requests.post('http://localhost:3000/api/ChangeStateTo'+state_info.title(), data=transactions_val)
	else:
		json_val = {
			  "$class": "org.acme.howto.Order",
			  "orderId": "0rd3r",
			  "timestamp": request.form['timestamp'].encode('utf-8'),
			  "date": request.form['date'].encode('utf-8'),
			  "state": request.form['state'].encode('utf-8').lower(),
			  "owner": "company"
			}	
		transactions_val = {
			  "$class": "org.acme.howto.ChangeStateTo"+state_info.title(),
			  "order": "0rd3r"
			}
		# Making 1 POST request with JSON data as a parameter
		# POST Request: Issue a ChangeStateTo<state>; where <state> is the state selected from the dropdown
		rT = requests.post('http://localhost:3000/api/ChangeStateTo'+state_info.title(), data=transactions_val)
	# return("The status code of the POST/PUT is: "+ str(rT.status_code) + " , " + str(rT.text))
	return redirect("/company")

# Route: changeOwner transaction (owner's name is passed as a parameter) 
@app.route("/changeOwner/<owner>", methods=['POST','GET'])
def changeOwner(owner):
	owner_data = {
	  "$class": "org.acme.howto.Entity",
	  "entityId": str(owner)
	}
	# POST Request 1: Create a new Entity element with its respective fields
	r1 = requests.post('http://localhost:3000/api/Entity', data=owner_data)
	# Change Ownership
	owner_data = {
		  "$class": "org.acme.howto.ChangeOwner",
		  "order": "0rd3r",
		  "newOwner": str(owner)
		}
	# POST Request 2: Issue a ChangeOwner transaction
	rT = requests.post('http://localhost:3000/api/ChangeOwner', data=owner_data)
	return redirect("/"+str(owner))

# Route: Engineer page
@app.route("/engineer")
def engineer():
	# GET Request 1: Get ChangeOwner transaction data
	r = requests.get('http://localhost:3000/api/ChangeOwner') 
	if r.json()==None or r.json()=={}:
		transactions = {}
	else:
		transactions = r.json()
	return render_template('engineer.html', title="Engineer", transactions=transactions)

# Route: Add Engineer
@app.route("/addengineer")
def addengineer():
	# GET Request 1: Get ChangeOwner transaction data
	r = requests.get('http://localhost:3000/api/ChangeOwner') 
	if r.json()==None or r.json()=={}:
		transactions = {}
	else:
		transactions = r.json()
	return render_template('engineer.html', title="Engineer", transactions=transactions)

# Route: Delete Engineer page
@app.route("/deleteengineer")
def deleteengineer():
	# GET Request 1: Get ChangeOwner transaction data
	r = requests.get('http://localhost:3000/api/ChangeOwner') 
	if r.json()==None or r.json()=={}:
		transactions = {}
	else:
		transactions = r.json()
	return render_template('engineer.html', title="Engineer", transactions=transactions)

# Route: tester page
@app.route("/tester")
def tester():
	# GET Request 1: Get ChangeOwner transaction data
	r = requests.get('http://localhost:3000/api/ChangeOwner')
	if r.json()==None or r.json()=={}:
		transactions = {}
	else:
		transactions = r.json()	
	return render_template('tester.html', title="Tester", transactions=transactions)

# Route: deployment page
@app.route("/deployment")
def deployment():
	# GET Request 1: Get ChangeOwner transaction data
	r = requests.get('http://localhost:3000/api/ChangeOwner')
	if r.json()==None or r.json()=={}:
		transactions = {}
	else:
		transactions = r.json()	
	return render_template('deployment.html', title="Deployment", transactions=transactions)	

# Route: customer page
@app.route("/customer")
def customer():
	# GET Request 1: Get ChangeOwner transaction data
	r = requests.get('http://localhost:3000/api/ChangeOwner')
	if r.json()==None or r.json()=={}:
		transactions = {}
	else:
		transactions = r.json()
	return render_template('customer.html', title="Customer", transactions=transactions)

# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))

# Entry point to the program
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=True)
