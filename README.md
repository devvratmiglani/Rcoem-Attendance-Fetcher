# Rcoem-Attendance-Fetcher
> A Python script to fetch Rcoem college attendance right into the terminal and shows real-time info to maintain minimum attendance.

`Rcoem-Attendance-Fetcher` allows you to access your Rcoem attendance directly into your terminal from [RCOEM.in](rcoem.in) in a colorful format.

![Demo raf](./demoraf.png)

## Color scheme
Below is subject wise color scheme:
```diff
- attendance < 75%          (red)
# 75% < attendance < 85%    (white)
+ 85% < attendance          (green)
```

it also shows you how much classes are `required/you can miss` so that 75% attendance will be maintained. I don't encourage missing classes 😁

## Installation

```sh
git clone https://github.com/devvratmiglani/Rcoem-Attendance-Fetcher.git

cd Rcoem-Attendance-Fetcher

pip install -r requirements.txt
```

## Adding Credentials
you have to add your credentials to `auth/auth.json` as well as the semester

semester : 0 --> gives attendance of all previous + current
semester : x --> gives attendance of that respective semester

## Usage 
Use as:

```sh
python -u fetcher.py # python3 in case of some linux distributions
```

## Shortcut
### Windows
You can also make a desktop shortcut to the script and then run by just double clicking it,

For windows:
Right click --> New --> Shortcut

In the location prompt write:
```sh
python -u /path/to/fetcher.py
``` 

### Linux
In linux I prefer creating a shell script as script.sh for shortcut:
```sh
#!/bin/sh
python -u /path/to/fetcher.py # python3 in case of some linux distributions
```


