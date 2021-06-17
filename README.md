![Probie-Lite](https://raw.githubusercontent.com/serialwaffle/probie-lite/main/probie.png)

# probie-lite
Probie-lite is a lightweight, standalone version of the Probe-Project (also written by SerialWffle, still in development) which is a full-featured, Wi-Fi probe Request aggregator and analyzer. The Probie Project was born out of the need to track pesky solicitors that ignore my "no Soliciting" sign.   

Probe-lite uses a wireless interface in monitor-mode (```airmon-ng start <interface>```) to passively collect probe requests from wireless devices in the vicinity.  Probie-lite desplays pertinant information about the collected probe request while also identifying whether or not the MAC is a Locally Assigned Address (LAA) vs an address assigned by its manufacturer (UAA).  Probie-lite also collects much more data and writes it to a local CSV for later ingestion.    


## Dependencies
- [termcolor](https://pypi.org/project/termcolor/)
- [scapy](https://pypi.org/project/scapy/)
- [This project runs best on Kali OS](https://www.kali.org/)

## Installation
```
git clone https://github.com/serialwaffle/probie-lite.git
```

## Usage
```
airmon-ng start wlan1

python3 probie-lite.py wlan1mon
```

## Screenshot

![Probie-Lite in action](https://raw.githubusercontent.com/serialwaffle/probie-lite/main/pl_example.png)

## More Information on Probe Requests and Anonymity 

Probe reqquests are commonly used by smart devices to initiate a Wi-Fi association to a known and previously associated SSID.  Typically, a device will send probe requests frequenty when not associated with a Wi-Fi SSID and commonly these probe requests will contain identifing information about the device that is sending the request along with information about the SSID that the device is probing for.  These pieces of information have been used in the past to track consumers in [large retail venues](https://medium.com/@brannondorsey/wi-fi-is-broken-3f6054210fa5) and is well-known.  Probe requests have also been suggested for use in tracking the number of [people in spaces](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8747391).  In order to offer some anonymity, mobile platforms such as Android and IOS will often use Locally Administered Addresses in place of the mobile device's Universally Administered Address, designated by the manufacturer.  Probie-lite evaluates the source MAC address and determines if it is a real or anonymized MAC address, hence the UAA (manufacture) or LAA (anonymous) flag in its output. 

More on probe request packets can be found [here](https://en.wikipedia.org/wiki/IEEE_802.11#Management_frames).


This project was greatly inspired by the following works:

- [How we tracked and analyzed over 200,000 people's footsteps at MIT](https://www.freecodecamp.org/news/tracking-analyzing-over-200-000-peoples-every-step-at-mit-e736a507ddbf/)
- [Tracking people via WiFi (even when not connected](https://www.crc.id.au/tracking-people-via-wifi-even-when-not-connected/)
- [ESP8266 TURNED SECRETIVE WIFI PROBE REQUEST SNIFFER](https://hackaday.com/tag/probe-requests/)
- [How I tracked +500 people with ESP8266](https://hackaday.io/project/174644-how-i-tracked-500-people-with-esp8266)

## Feedback and issues? 
If you would like to get involved with The Probie-lite or Probie Project, please reach out via twitter @serialwaffle. 

If you have any feedback, anything that you want to see implemented or running into issues using probie-lite, please feel free to file an issue on https://github.com/serialwaffle/probie-lite/issues   

## Support 
If you appreciate my work and HackTheBox, feel free to give me some respect:  

<a href="https://www.hackthebox.eu/profile/5305"><img src="https://www.hackthebox.eu/badge/image/5305" width="150"></a>
