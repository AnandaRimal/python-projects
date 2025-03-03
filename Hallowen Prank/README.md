Pygame Horror Readme
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
# Pygame Horror Prank

## Introduction
This Python script creates a jump scare effect using Pygame. It plays eerie music and then displays a scary image on a full-screen window after a short delay.

## Features
- **Full-screen mode** for maximum effect.
- **Plays two audio tracks** sequentially to build suspense.
- **Displays a scary image** to complete the jump scare.

## Requirements
- Python 3
- Pygame library
- Audio files (`ratsasan.mp3`, `scary.mp3`)
- Image file (`scr.jpg`)

## Installation
1. Install Pygame if not already installed:
   ```sh
   pip install pygame
   ```
2. Place the required files (`ratsasan.mp3`, `scary.mp3`, and `scr.jpg`) in the same directory as the script.

## Running the Script
Execute the script using:
```sh
python horror_prank.py
```

## How It Works
1. The script starts in full-screen mode.
2. It plays `ratsasan.mp3` for suspense.
3. After 5 seconds, it switches to `scary.mp3`.
4. After 1 second, it displays `scr.jpg` to scare the user.

## Future Improvements
- Randomize image display time for unpredictability.
- Add a quit event to exit when the scare happens.
- Use multiple images and sounds for variation.

Use this responsibly and have fun scaring your friends! 👻
