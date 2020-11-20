# Authentication 

##EGI

### Access token 

Obtain the OS_ACCESS_TOKEN go to https://aai.egi.eu/fedcloud/refreshtoken.php 

Execute the command on the bottom of the page.

### stack-server.ct.infn.it
Add the following environment variables

```
export OS_ACCESS_TOKEN="SECERT"
export OS_AUTH_URL="https://stack-server.ct.infn.it:35357/v3"  
export OS_PROJECT_ID="745695ccd17042fabf96d2410a4278d9" 
export OS_AUTH_TYPE="v3oidcaccesstoken"
export OS_IDENTITY_PROVIDER="egi.eu"
export OS_PROTOCOL="openid"
```


### fedcloud-osservices.egi.cesga.es




```
export OS_ACCESS_TOKEN="SECERT"
export OS_PROJECT_ID=c1c9c25774fe418599bced1d45862c60
export OS_AUTH_TYPE="v3oidcaccesstoken"
export OS_IDENTITY_PROVIDER="egi.eu"
export OS_PROTOCOL="openid"
```

On the dashboard on the top right you can download a script to set 
these variables
