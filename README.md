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
