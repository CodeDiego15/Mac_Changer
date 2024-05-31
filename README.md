
# mac_changer

easy use, read the documentation

## how to test?

```
git clone git@github.com:CodeDiego15/Mac_Changer.git
```
```
sudo python3 mac_changer.py --help. view commands
```

## Commands 


| option | short     | Description                |
| :-------- | :------- | :------------------------- |
| ` --interface` | `-i` | **Required**. use the desired interface. EX: enth0, en0|
| `--mac` | `-m` | **Required**. use the mac that seems best to you. EX: 00:11:22:33:44:77
| `--help`| `-h` | Help

### How to see your mac address?
```
  Macos/Linux: 
You have to go to the terminal and see an interface that I have ether and that is active. For example
ether:00:11:22:33:44:55 
status: active. Therefore, one must always be active unless you have Wi-Fi turned off or disconnected.
```


### Commands to see the mac

```
sudo ifconfig
```

## Running macmorph without typing python3 macmorph.py
### Introduction:

To provide a more user-friendly experience for your macmorph project, you can allow users to execute the tool without typing the full command python3 macmorph.py in the terminal. This can be achieved by creating a symbolic link.

## 1. Creating a Symbolic Link:

### On macOS or Linux:

Locate the macmorph.py file in your project.

Create a symbolic link in the `/usr/local/bin` directory with the name macmorph.


| bash|      
| :-------- |
| ```ln -s /path/to/macmorph.py /usr/local/bin/macmorph```|

Ensure that the /usr/local/bin directory is in the users' PATH. If it's not, you can add a note in the README instructing users on how to do so.
