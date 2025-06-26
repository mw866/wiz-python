# README
## Get started

1. Make sure you are using the correct python version.
```
python3 --version
```

2. Install the Wiz Python SDK 
```
pip3 install -r requirements.txt 
```
3. Create `wiz_config.json`
```
{	
  "wiz_client_id":     "xxx",
  "wiz_client_secret": "xxx",
  "wiz_auth_url":      "https://auth.app.wiz.io/oauth/token",
  "wiz_api_timeout":   180,
  "wiz_debug":         false
}
```

4. Execute the script
```
python3 main.py --query sdr.graphql --variables sdr.json
```

## Trouhleshooting
# "SSL: CERTIFICATE_VERIFY_FAILE" on MacOS
Install the official MacOS Python. See [Using Python on macOS](https://docs.python.org/3/using/mac.html)
In this `ReadMe.rtf`, 

<blockquote>
 This package includes its own private copy of OpenSSL 3.0.   The trust certificates in system and user keychains managed by the Keychain Access application and the security command line utility are not used as defaults by the Python ssl module.  A sample command script is included in /Applications/Python 3.13 to install a curated bundle of default root certificates from the third-party certifi package (https://pypi.org/project/certifi/).  Double-click on Install Certificates to run it.
</blockquote>
