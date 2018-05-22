# Running Kogu server on alternative interface and port

It is possible to run Kogu server on other network interface and port besides the default (localhost:8193). 

***Important:***

***Running the server on other network interface(s) besides localhost exposes your server to the other machines in the network. As Kogu currently lacks configurable user access and connection security be sure that you know what you are doing.***

If you have chosen to run the server on other port or interface you can use the following environment variables to do so:

Variable | Description | Default
- | - | -
KOGU_HOST | Network interface to bind the server to. Use 0.0.0.0 to bind to every available interface | localhost
KOGU_PORT | Port to use for the server | 8193


## Connecting Kogu CLI to the server running on specific port and interface

By default Kogu CLI connects to server located in http://localhost:8139. If you have server running on any other IP address or port you can define environment variable ```KOGU_SERVER``` with the correct information.


## Example

Assuming that you want to run Kogu server on port 8000 define environment variable KOGU_PORT and restart the server process.
```bash
export KOGU_PORT=8000
```
Note that when you have altered server configuration so you also have to define ```KOGU_SERVER``` environment variable for the Kogu CLI as:
```bash
export KOGU_SERVER=http://localhost:8000
```