# Critical Flight – Hardware Challenge

## Challenge Overview
This challenge involved analyzing **.gbr (Gerber) files**, which are commonly used in PCB (Printed Circuit Board) design.  
The goal was to open and inspect these hardware design files to uncover a hidden flag.

## Files Provided
- Multiple `.gbr` files (Gerber files for PCB design)

## Analysis
1. Gerber files store **circuit board layer information**, such as copper traces, silkscreen, and text.  
2. To view them, a **Gerber viewer** is required. The recommended tool is `gerbv`.  

## Solution Path
- Launched the Gerber viewer tool in the terminal using the command "gerbv".
- In gerbv, to load the files go to File-> Open and select the file.
- There are multiple .gbr files, load all of them in gerb viewer.
- By loading the files into `gerbv`, we could inspect the PCB layout visually.
- We can see the flag in the viewer

## Flag in the form of : HTB{---}
