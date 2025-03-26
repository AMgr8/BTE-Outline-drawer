# BTE-Outline-drawer
A python script to create outlines in the build the earth project

## How to use
### default mode
- draw a path on google earth pro 
- save the path to google earth
- export the path to the same folder as the python script and save as "path*.xml" where * is the number of the path from 1 to the number of paths you wish to draw at once
- ensure you delete all previous paths from the folder before you attempt to run it with new paths
- right click inside the folder that the files are stored within and click "Open in Terminal"
- for servers that are fast like the uk run: python OutlineGen.py
- for servers that are slower or kick for spam if the previous command doesn't work run: python OutlineGen.py --slow="s"
- the program will do nothing for about 5 seconds, in this time change your screens focus to the minecraft server and wait.
- DO NOT TOUCH ANY KEYS OR PRESS ANY BUTTONS. you cannot use your computer until the script is finished
- the script will type Done in the terminal and turn your gamemode back to creative when finished
- if something goes wrong with the script you can stop it by opening the terminal and doing ctrl+c

### 2d house mode
- works in a very similar way to above but there's a few key differences. make sure you're familiar with the default mode first
- this is used exclusivly for getting the tpll points for 2d houses. it won't fill in the lines
- draw a path around the roof of the house/building make sure that the final point is the point where the wall of the house meets the ground. example below
![image](https://github.com/user-attachments/assets/f5b5968a-3d5b-4ce6-bf8e-1a7dc3640384)
- do the same steps as above except add --mode="h" to the command

