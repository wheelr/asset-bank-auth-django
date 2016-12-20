# asset-bank-auth-django
Django app to allow integration with the Asset Bank 'Secure Link to App' functionality

## Setup

From the project root run

	. activate
	
To run the tests

	./manage.py test assetbankauth

##Usage

The module has one decorator which when added to a view will ensure the user has been authenticated with Asset Bank before accessing the view.
 
If they have not been authenticated they will be redirected to the associated Asset Bank for authentication 

```
@ensure_assetbank_authenticated_user_in_session()
def my_view(request):
    ...
```

The authentication is governed by following four settings in your Django settings.py file 

```
ASSETBANK_AUTH_ENABLED = True
ASSETBANK_URL = 'http://localhost:8080/asset-bank'
ASSETBANK_AUTH_TOKEN_KEY = ''
ASSETBANK_LOG_OUT_AFTER_AUTH = 'false'
```

__ASSETBANK_AUTH_ENABLED: True/False__

Should be set to True on production for the authentication to the be applied. 

Can be set to False and turned off in local environments to avoid having to have a running Asset Bank
    
__ASSETBANK_URL__

The URL of the authenticating Asset Bank e.g. 'http://my-assetbank.com/asset-bank

__ASSETBANK_AUTH_TOKEN_KEY__

This should match the 'remote-app-token-key' setting in the authenticating Asset Bank

__ASSETBANK_LOG_OUT_AFTER_AUTH = True/False__

True if the user should not be logged in to Asset Bank after being redirected back to the your application.



The function
```
assetbankauth.utils.get_authenticated_user_in_session 
```
can be used to get the authenticated user from the session. For available properties on the user object see
```
assetbankauth.models.AssetBankUser 
```

