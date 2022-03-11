# Server status

Server status a simple bot script to show a list of players on a Fivem/Redm server.

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
MIT License

Copyright (c) 2022 Hamidreza Farzin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

