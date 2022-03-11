# Server status

Server status a simple bot script to show a list of Fivem/Redm server players on Discord Channel .

## Installation

install the requirements.txt with  


```bash
pip install -r requirements.txt
```

## Config
open config.json file and edit the values
```json5
{
  "TOKEN": "your-token", //Don’t forget that you’ll need to replace the Token
  "prefix": "H!", //Set Your Intended Prefix
  "Server_ip": "Your ip:30120", //Set Your Server Fivem or Redm Ip and Port
  "Channel_id": null, //Do not edit Channel_id
  "Message_id": null, // Do not edit Message_id
  //Do not edit color filters
  "color_filter": [ 
    "^0",
    "^1",
    "^2",
    "^3",
    "^4",
    "^5",
    "^6",
    "^7",
    "^8",
    "^9"
  ]
}
```
## Run and setup
After installation the all requirements and edit config.json file

run the server_status.py and do the following steps :

1. give yourself a administrator role

2. Use the "[Your-Prefix]set_status #mention-a-channel" command in a channel

3. Done


## License
[MIT](https://github.com/H-VICTOOR/Fivem-Status/blob/main/LICENSE)