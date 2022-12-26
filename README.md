# Purpose **PROJECT WIP**

This project was proof that I understand basic programming concepts and could use them to make something interesting. This project lets you input a screen size and viewing distance and returns a pdf/png of where it stands on the horizontal FOV scale.



## What makes a good FOV?

I can sit here and tell you that one source recommends X, while another recommends Y. In my personal experience, a FOV between 36° and 50° is acceptable. I don't recommend viewing a screen with a FOV over 60° because anything >60° exists outside of a human's *image recognition FOV*. The image recognition FOV, or IRFOV, is the field of vision in which a human can identify what is there. This means that anything above 60° is in your peripheral vision, and is wasted screen space.

### Prerequisites:

    Must have Python installed. (developed on 3.11)
    Must have R installed. (Keep track of installation PATH)

### Steps:

1. Download necessary files and place in a commond folder. (fovCalculator.py, fovRun.py, graphing.R, data.csv, fov.txt)

2. Change PATH in graphing.R to the path of the common folder. (any backlashes MUST be forward slash)

3. Edit fov.txt to make PATH the same location of your R download. Likely: C:\Program Files\R\R-VERSION#\bin

4. Rename fov.txt to fov.sh - This makes the file a bash script, executing the program.

5. Open a terminal window set to the PATH of the common folder.

6. Type bash fov.sh

7. Respond to the questions.

8. A png and pdf will appear in the directory of the other files containing a graph. #It was intended to only produce a png, but testing revealed it gives both.

### Example: ![Screenshot](Repository_Assets/Rplots.pdf)



###Remaining Files:
pixelDensity.py

    Gives pixel density of a screen based on diagonal length and screen type.

pythagoreanPixelDensity.py

    Gives pixel density based on the width or height of a desired screen.

FOV/identified_pattern.txt

    This is a pattern I identified regarding dimension change of screens.

