# SDLC on the Blockchain

An end-end SDLC Application using Blockchain.

Before stating with the application let's discuss some of the terms used here.

# Hyperledger Fabric
Hyperledger Fabric is an enterprise-grade permissioned distributed ledger framework for developing solutions and applications. Its modular and versatile design satisfies a broad range of industry use cases. It offers a unique approach to consensus that enables performance at scale while preserving privacy.

# Hyperledger Composer
Hyperledger Composer is a set of collaboration tools for building blockchain business networks that make it simple and fast for business owners and developers to create smart contracts and blockchain applications to solve business problems.

# Install the development environment
Follow these instructions to obtain the Hyperledger Composer development tools (primarily used to create Business Networks) and stand up a Hyperledger Fabric (primarily used to run/deploy your Business Networks locally). Note that the Business Networks you create can also be deployed to Hyperledger Fabric runtimes in other environments e.g. on a cloud platform:
https://hyperledger.github.io/composer/v0.19/installing/development-tools.html

Set up the Business Network

Head over to the Composer Playground: https://composer-playground.mybluemix.net/

![](https://github.com/srividyavn/SDLC-on-the-Blockchain/blob/master/Screenshots/Screenshot%207.png)

Select “Deploy a Business Network”

Under the “Model Network Starter Template”, select “browse”, and choose the sdlc-on-the-blockchain@0.0.1.bna file from this repository.

![](https://github.com/srividyavn/SDLC-on-the-Blockchain/blob/master/Screenshots/Screenshot%208.png)

Select "Deploy"

![]( https://github.com/srividyavn/SDLC-on-the-Blockchain/blob/master/Screenshots/screenshot%209.png)

Select "Connect Now"

Click on the "Model File" in the left pane. From this section you can model your business network. 

In my case, we are tracking the SDLC of the order which is placed from the company, to the Engineer, to the Tester, and finally to the Customer. We're assuming each Entity (i.e. company), will make use of RFID tags to store information of the order, and will scan that tag as it's received. This information, such as timestamp, the date, and state (production, development, testing, deployment) is stored on the Blockchain.

![](https://github.com/srividyavn/SDLC-on-the-Blockchain/blob/master/Screenshots/screenshot%2010.png)

We will create multiple instances of type Entity.

![](https://github.com/srividyavn/SDLC-on-the-Blockchain/blob/master/Screenshots/screenshot%2011.png)

we define the transactions that will take place on the Blockchain ie.,change state to different state in the SDLC lifecycle.

![](https://github.com/srividyavn/SDLC-on-the-Blockchain/blob/master/Screenshots/screenshot%2012.png)

![](https://github.com/srividyavn/SDLC-on-the-Blockchain/blob/master/Screenshots/screenshot%2013.png)

Select "Script File" in the left pane. The transaction processor functions will be invoked.

Select "Access Control" from the left pane. From here, you can determine which participants of the business network have access to which assets and transactions.

On the Top Pane, select "Test".

From here, you can test out the transactions that you defined in the model file. On the top left, select “+ Create New Participant, and enter a unique identifier for the entity.

Select “Create New”. You should see a new entity being created. In the left Pane, under Assets, select Order. Select “+ Create New Asset.” Fill in the details for the order, and select “Create New”. (For the state, select from “production”, “development”, “testing”, and “deployment). For the Owner field, select the ID of the entity you just created.

You should see a new order asset being created.

Select “Submit Transaction” on the bottom left. For the Transaction Type, select the “ChangeStateToTesting” transaction, and for the “order” field, pass in the ID you just created when creating your order asset.

Select “Submit”

You should see a notification pop up saying “Submit Transaction Successful”. You can double-check by selecting “All Transactions” in the left pane, under Transactions.

In the ChangeStateToTesting transactions, select “view record”, and you can see all the transaction related information.

That’s it! You’re ready to deploy your business network to the Hyperledger Fabric.

# Setting up the Environment

Follow these instructions to install the pre-requsities for installing Hyperledger Composer on a local Mac OS X machine. You need to install these tools before you attempt to install Hyperledger Composer.

Install nvm and Apple Xcode
First install nvm (the Node version manager). nvm is a tool that allows you to easily install, update and switch between versions of Node.js.

Open the terminal (command line) by clicking on the magnifier in the menu bar at the top right of your screen. Type terminal and press enter.

In the terminal window paste the text below and press enter:

curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash

When you hit enter you should see the pop-up below, prompting you to install git. Press the Get Xcode button to install the full Apple Xcode IDE, including a C++ compiler, used to install native Node.js modules.

The download and install process for Xcode may take 20 minutes or more. Be patient!

After the installation of Xcode has completed launch Xcode. Accept the license agreement. It will prompt you for your username and password and will install additional components.

After Xcode finishes installing additional components and launches, simply quit Xcode.

Switch back to the terminal and create your bash profile (stores user preferences for bash):

touch .bash_profile

Then rerun the original curl command:

curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash

Close the terminal and reopen it.

Check that nvm is installed and is accessible:

nvm —-version

Install Node
Install the latest (long term support) version of Node:

nvm install --lts

Switch to the LTS version of Node:

nvm use --lts

Check that Node is installed:

node --version

Install Docker
Follow the instructions here to install Docker for Max (stable): Install Docker

After running the installed Docker application you should have the whale icon in your menu bar, with a green “Docker is running” status.

Install VSCode
Install VSCode by visiting: Install VSCode

Press the “Download for Mac” button and copy the downloaded application into your Applications folder.

# Install the Hyperledger Composer Extension for VSCode
Type composer into the search bar and then press the Install button next to the Hyperleger Composer extension. Once the install completes you need to press the Reload button to activate the extension.

# Installing the Development Environment
Follow these instructions to obtain the Hyperledger Composer development tools (primarily used to create Business Networks) and stand up a Hyperledger Fabric (primarily used to run/deploy your Business Networks locally). Note that the Business Networks you create can also be deployed to Hyperledger Fabric runtimes in other environments e.g. on a cloud platform.

# Installing Components
# Step 1: Install the CLI Tools
There are a few useful CLI tools for Composer developers. The most important one is composer-cli, which contains all the essential operations, so we'll install that first. Next, we'll also pick up generator-hyperledger-composer, composer-rest-server and Yeoman plus the generator-hyperledger-composer. Those last 3 are not core parts of the development environment, but they'll be useful if you're following the tutorials or developing applications that interact with your Business Network, so we'll get them installed now.

# Essential CLI tools:
npm install -g composer-cli

Utility for running a REST Server on your machine to expose your business networks as RESTful APIs:
npm install -g composer-rest-server

Useful utility for generating application assets:
npm install -g generator-hyperledger-composer

Yeoman is a tool for generating applications, which utilises generator-hyperledger-composer:
npm install -g yo

# Install Playground
If you've already tried Composer online, you'll have seen the browser app "Playground". You can run this locally on your development machine too, giving you a UI for viewing and demonstrating your business networks.

Browser app for simple editing and testing Business Networks:

npm install -g composer-playground

# Install Hyperledger Fabric
This step gives you a local Hyperledger Fabric runtime to deploy your business networks to.

In a directory of your choice (we will assume ~/fabric-tools), get the .zip file that contains the tools to install Hyperledger Fabric:
mkdir ~/fabric-tools && cd ~/fabric-tools

curl -O https://raw.githubusercontent.com/hyperledger/composer-tools/master/packages/fabric-dev-servers/fabric-dev-servers.zip

unzip fabric-dev-servers.zip

A tar.gz is also available if you prefer: just replace the .zip file with fabric-dev-servers.tar.gz1 and the unzip command with a tar xvzf command in the above snippet.

Use the scripts you just downloaded and extracted to download a local Hyperledger Fabric runtime:
cd ~/fabric-tools ./downloadFabric.sh

# Start Hyperledger Fabric
Start the fabric:

./startFabric.sh

Generate a PeerAdmin card:

./createPeerAdminCard.sh

You can start and stop your runtime using ~/fabric-tools/stopFabric.sh, and start it again with ~/fabric-tools/startFabric.sh.

At the end of your development session, you run ~/fabric-tools/stopFabric.sh and then ~/fabric-tools/teardownFabric.sh. Note that if you've run the teardown script, the next time you start the runtime, you'll need to create a new PeerAdmin card just like you did on first time startup.

# Deploying the Business Network to Hyperledger Fabric

# Creating the .bna file
Once you have the environment set up, it's time to package everything into a .bna file. In order to do this, we're going to use a Yeoman generator to create a skeleton business network, then replace the model, script, and access control files with the ones we created earlier on in the tutorial.

Create a skeleton business network using Yeoman. This command will require a business network name, description, author name, author email address, license selection and namespace.
yo hyperledger-composer:businessnetwork

Enter sdlc-on-the-blockchain for the network name, and desired information for description, author name, and author email.

Select Apache-2.0 as the license.

Select org.acme.biznet as the namespace.

cd into the folder which was just created and replace the contents of /sdlc-on-the-blockchain/lib/org.example.biznet.cto with the model file generated earlier on in the tutorial.

Replace the contents of /sdlc-on-the-blockchain/lib/logic.js with the script file generated earlier on in the tutorial.

Create a new file in the sdlc-on-the-blockchain folder, called permissions.acl and paste the contents of the Access Control file generated earlier on in the tutorial.

Now that you have your busines network, it's time to package it up into a .bna file. In the sdlc-on-the-blockchain directory, enter the following command:

composer archive create -t dir -n .

After the command has run, a business network archive file called sdlc-on-the-blockchain@0.0.1.bna has been created in the tutorial-network directory.

#Deploy the Business Network
After creating the .bna file, the business network can be deployed to the instance of Hyperledger Fabric. Normally, information from the Fabric administrator is required to create a PeerAdmin identity, with privileges to deploy chaincode to the peer. However, as part of the development environment installation, a PeerAdmin identity has been created already.

After the runtime has been installed, a business network can be deployed to the peer. For best practice, a new identity should be created to administrate the business network after deployment. This identity is referred to as a network admin.

# Retrieving the Correct Credentials
A PeerAdmin business network card with the correct credentials is already created as part of development environment installation.

# Deploying the Business Network
Deploying a business network to the Hyperledger Fabric requires the Hyperledger Composer chaincode to be installed on the peer, then the business network archive (.bna) must be sent to the peer, and a new participant, identity, and associated card must be created to be the network administrator. Finally, the network administrator business network card must be imported for use, and the network can then be pinged to check it is responding.

To install the composer runtime, run the following command:
composer runtime install --card PeerAdmin@hlfv1 --businessNetworkName sdlc-on-the-blockchain

The composer runtime install command requires a PeerAdmin business network card (in this case one has been created and imported in advance), and the name of the business network.

To deploy the business network, from the sdlc-on-the-blockchain directory, run the following command:
composer network start --card PeerAdmin@hlfv1 --networkAdmin admin --networkAdminEnrollSecret adminpw --archiveFile sdlc-on-the-blockchain@0.0.1.bna --file networkadmin.card

The composer network start command requires a business network card, as well as the name of the admin identity for the business network, the file path of the .bna and the name of the file to be created ready to import as a business network card.

To import the network administrator identity as a usable business network card, run the following command:
composer card import --file networkadmin.card

The composer card import command requires the filename specified in composer network start to create a card.

To check that the business network has been deployed successfully, run the following command to ping the network:
composer network ping --card admin@sdlc-on-the-blockchain

The composer network ping command requires a business network card to identify the network to ping.

# Generating a REST Server
Hyperledger Composer can generate a bespoke REST API based on a business network. For developing a web application, the REST API provides a useful layer of language-neutral abstraction.

To create the REST API, navigate to the sdlc-on-the-blockchain directory and run the following command:
composer-rest-server

Enter admin@sdlc-on-the-blockchain as the card name.

Select never use namespaces when asked whether to use namespaces in the generated API.

Select No when asked whether to secure the generated API.

Select Yes when asked whether to enable event publication.

Select No when asked whether to enable TLS security.

The generated API is connected to the deployed blockchain and business network.

Once the REST server is up and running, head over to https://localhost:3/explorer


It should look a little like this:

![](https://github.com/srividyavn/SDLC-on-the-Blockchain/blob/master/Screenshots/Screen%20Shot%2014.png)

# Running the Application
# Purpose
This is a Python Flask web application built as an interface for the Blockchain network running on Hyperledger Fabric. The application utilises REST APIs (generated using the Composer REST Server) to connect to the Blockchain network and perform GET, POST and PUT requests.

# Technology
This application was built with the Flask Microframework. The UI of the application was built with MaterializeCSS, a front-end framework based on Material Design.

# How to run
Ensure Python is installed on your local environment (Both Python 2 and Python 3 are supported).
Install the requirements using the command pip install -r requirements.txt.
Run the application as: python application.py.
Point your web browser to the address localhost:<port>.
Help
Please feel free to contact me with any questions/comments.

# Navigating the Application
Once you start up the application, you should be able to see this page:

![](https://github.com/srividyavn/SDLC-on-the-Blockchain/blob/master/Screenshots/Screen%20Shot%201.png)

![](https://github.com/srividyavn/SDLC-on-the-Blockchain/blob/master/Screenshots/Screenshot%202.png)

![](https://github.com/srividyavn/SDLC-on-the-Blockchain/blob/master/Screenshots/Screenshot%203.png)

![](https://github.com/srividyavn/SDLC-on-the-Blockchain/blob/master/Screenshots/Screenshot%204.png)

![](https://github.com/srividyavn/SDLC-on-the-Blockchain/blob/master/Screenshots/Screenshot%205.png)

![](https://github.com/srividyavn/SDLC-on-the-Blockchain/blob/master/Screenshots/Screenshot6.png)

From here, the Customer can keep track of their orders through the entire process.

# Summary
We showed you how to create a simple business network using Hyperledger Composer Playground, export it and create a business network archive file, and deploy it to the Hyperledger Fabric. We also showed how you can spin up a REST server for your applications to consume, and demonstrated that fact by connecting a Python-based application to the Blockchain to realize the use-case of a frozen pizza supply chain.

# References

https://developer.ibm.com/tutorials/pizza-on-the-blockchain/

https://developer.ibm.com/tutorials/cl-ibm-blockchain-101-quick-start-guide-for-developers-bluemix-trs/


