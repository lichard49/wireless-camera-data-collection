# Wireless Camera Data Collection

Simple web tool to collect image data from small, wireless IP cameras (often marketed as "spycams" or security cameras).  The device used in this example is:

# Hardware set up

Make sure the camera is charged because the connection drops quickly if it's not.  Switch it on with the slider switch, and then connect the computer to the camera's wifi network, which should start with CMS.

# Software set up

Install dependencies:
```pip install flask```

## Getting the IP address of the camera

On Linux, use:
```ip route```
The result will say "default via <ip>"

On Mac, use:
```arp -a```
The result should be the first line (192.168.x.x)

Make sure the IP address you find corresponds to the ```IP_ADDRESS``` variable in ```app.py```.  If not, be sure to update it.

## Running the app

Simply run in a terminal:
```python2 app.py```

A localhost URL should be printed out, such as 127.0.0.1:5000.  Navigate to that URL in a browser.

# Using the app

You should see the live preview in the center of the screen.

Press the capture button to save an image.  Image file names are simply timestamps to prevent overwriting or losing any data.

Optionally, set a prefix or suffix for the file name.  This enables adding details, such as labels, to each picture.

The names of the captured images are listed at the bottom of the app.  Locally, they are stored in the ```data/``` directory next to this README file.