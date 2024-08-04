# TokenGateService-Lite
TokenGateService is a flask application for creating token gated applications. Can be used as a standalone system or as a middle-ware. 



Currently the index page exposes a page that allows a user to connect wallet and to verify ownership of a token by singing a message.   
  
Currently it is using a simple nonce and personal sign method in web3.js but needs to be upgraded to using eip-712 message by creating the strucutred data and singing with signTypedData()



Note this is a proof of concept. 



### Main page 

![tokenGateEntry](demoFiles/tokenGateEntry.png)


### Connected Wallet 

![tokenGateEntry](demoFiles/connected.png)


### Signature Request 

![tokenGateEntry](demoFiles/signatureRequest.png)



### Fail 

![tokenGateEntry](demoFiles/signatureRequest.png)

### Content unlocked 
![tokenGateEntry](demoFiles/success.png)


### Content Locked 
![tokenGateEntry](demoFiles/fail.png)



