# Server status

Server Status a simple bot script to display a list of Fivem / Redm server’s players on the Discord channel.

Developed By H_VICTOR#2999

## Preview

![in channel](https://user-images.githubusercontent.com/60010616/157981567-1c97d98e-8639-43a1-abf8-19505f367602.png)


![Profile](https://user-images.githubusercontent.com/60010616/157981218-ac8d2dd6-1f45-4c7c-9138-7f81f9fdfac8.png)

## Installation
1. Download the Project 

2. install the requirements.txt with  


```bash
pip install -r requirements.txt
```

## Config
open config.json file and edit the values
```json5
{
  "TOKEN": "your-token", //Don’t forget that you’ll need to replace the Token
  "prefix": "H!", //Set Your Intended Prefix
  "Server_ip": "Your ip:30120", //Set Your Fivem or Redm Server Ip and Port
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

Follow the steps below :
1. Create a bot in Discord developer Portal and copy the token to config.json

2. run the server_status.py

3. give yourself a administrator role

4. Use the "[Your-Prefix]set_status #mention-a-channel" command in a channel

5. Done


## License
[GNU General Public License v3.0](http://www.gnu.org/licenses/)
