# Wake on wan
## AKA Turn your pc on from internet when you are outside home.

This little program launches a Flask application that exposes a simple html page on a web that given a passcode, sends
a magic packet to the network using the Wake on Lan feature

https://en.wikipedia.org/wiki/Wake-on-LAN

You can install it on any host compatible with python, a raspberry, maybe your own router, expose it to internet via port forwarding and enter on the web
from your mobile to launch your computer.

This is a cool combination with Chrome Remote Desktop, TeamViewer, AnyDesk, or any other remote desktop control tool.

* https://remotedesktop.google.com/
* https://www.teamviewer.com/en-us/ 
* https://anydesk.com/en 

## How to use it
Set up your passcode/mac address relation editing the line 5 of the app.py file to the one that suits you

    macs = {
        '<passcode>': '<MAC_ADDRESS>',
    }
For example:

    macs = {
        'dtc_f09ba4b3-8363-46e1-9fb8-10feaeb27f8c': '2a:2a:2a:2a:2a:2a',
    }


Start it from command line as a python flask application: 

        python app.py

### What if I don't have a public IP since my ISP hides me behind NAT

A solution I made when working on this, since I was on this situation, was using an intermediate server hosted on oracle
public cloud, since it gives users 24/7 VMs on free tier.
* https://www.oracle.com/cloud/free/

Then, the host of this program configured a SSH Tunneling with the server, forwarding the application port.

It's important to configure the ssh tunnel to auto reconnect on network failures, since the free server could be down at any time.

I think I made it using autossh. If I feel it I would rescue the raspberry to check the configuration.

* https://github.com/Autossh/autossh

Also, set it up on a script to launch it when the PI4 reboots, just in case.

### The code is really really really improvable
This was just a PoC that resulted veeeery useful and I wanted to keep it on git and share it to whoever
may need it. PRs welcome :D.

Also, I'm not a frontend and don't know almost anything of web development (yet), so I just grabbed a free template 
and replicated the three states (put passcode, passcode OK and passcode KO) to get it to work. 

### Warnings 
I put a passcode so not anyone scanning opened ports on random IPs could just launch the computer. 

However, even if something like that happens, there is no danger since it will just consume power, nothing too special.

I think it's a nice layer of protection that could have a better protection, but it's better than nothing.

### Future improvements.
If this is iterated, it will be nice docker it, make the password/macs be an environmental argument, and maybe add the 
capacity to launch a reverse proxy like caddy to configure a domain with a https certificate. Also, include in the project
how to autostart it on host launch, and provide also easiness for the behind-NAT scenarios. 

