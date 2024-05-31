
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

