# Halal Lab
A student-led start up that aims to provide halal food recommendations for Muslims living abroad.

## Backend 

![Image of Serverless vs Server API](https://www.gocd.org/assets/images/blog/serverless-continuous-delivery/traditional-vs-serverless-ee2afc44.jpeg)

https://www.gocd.org/assets/images/blog/serverless-continuous-delivery/traditional-vs-serverless-ee2afc44.jpeg

### Serverless Architecture
Serverless architectures are internet-based systems where the application development does not use the usual server process. Instead, they rely solely on a combination of third-party services, client-side logic and service-hosted remote procedure calls (Functions as a Service).

“Not the usual server process” means that your software isn't running on a server that you have access to. You don't own those servers. You can't log in to them, even if you wanted to. They are abstracted away and managed for you by someone else, typically a cloud provider.

There are many immediate benefits to not managing your own servers:

* You don't have to worry about them randomly rebooting or going down.
* You don't end up with snowflake servers, where you don't know quite what's installed on them but they are mission-critical to your organisation.
* You're not responsible for installing software on them. Even if you use configuration management tools such as Chef or Ansible to automate this, that’s still extra code you have to maintain over time.
* Pretty neat and let’s you build basic CRUD (Create, Read, Update, Delete) operations in real time

### Server vs. Serverless Architecture
Since most of the team is pretty comfortable with Python, we have two options:

Server | Serverless
------ | -------------
Django | Firebase

Firebase is what we call **BaaS** (Backend as a service). Through the use of APIs and SDKs, Firebase provides web and mobile apps developers with a way to link their applications to backend cloud storage.

### Progress of the Django Backend 
By experimenting with Django, I have created a back end admin page to Add, Delete and Update (Put) the halal ingredients database, as shown below. 

![Image of Serverless vs Server API](https://github.com/puaqieshang/halal-lab/blob/master/Screenshot%202020-01-03%20at%2012.07.13%20PM.png)

![Image of Serverless vs Server API](https://github.com/puaqieshang/halal-lab/blob/master/Screenshot%202020-01-03%20at%2012.09.41%20PM.png)

### References
* https://www.fullstackfirebase.com/introduction/what-is-serverless 
* https://appinventiv.com/blog/top-react-native-databases/?utm_campaign=Quora_Ria_ReactNativeDatabases&utm_medium=Quora_Ria&utm_source=Quora#A1
* https://www.quora.com/What-is-the-back-end-for-apps-built-with-react-native

