# fritz-google-cloud-dns

This is a Python script that reads the current WAN address from your FRITZ!Box router and updates a zone on Google Cloud DNS with that address.

When run from a crontab this script makes sure that your home server is accessible from the internet using a static hostname.

## Installation

```
pip3 install -r requirements.txt
```

## Usage

The following invocation updates the record `home.example.com` in the zone `example` with the current WAN address:

```bash
GOOGLE_APPLICATION_CREDENTIALS=service-account.json
./fritz-google-cloud-dns.py example home.example.com
```

The file `service-account.json` contains the service account key.

```json
{
    "type": "service_account",
    "project_id": "i-abcd-000000",
    "private_key_id": "...",
    "private_key": "...",
    "client_email": "example@i-abcd-000000.iam.gserviceaccount.com",
    "client_id": "...",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/..."
  }
  ```
