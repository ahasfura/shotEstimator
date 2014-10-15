shotEstimator
=============

This project predicts the likelihood that a given shot will go in, given the shot data from the beginning of the 2006 season through some given point in time

the function takes 4 parameters, a player, an integer x coordinate, an integer y coordinate, and an integer specifying for many season you would like to be considered. The function then searches through yearly event data to find shots within a small margin of the x,y input, and returns the number of makes in that area divided by the total number of shots taken by that player in that same area. If there were no shots taken within the specified x,y location, a the function return "no shots taken in that area".

If I had more time to work on this project, I would make it faster by checking only the games which contain the team of the specified player, and I would find a player trading database to check to keep player's teams up to date. I would also try to incorporate the type of shot into determining the final likelyhood of a shot going in. For example, in the given event data shots are classified as many things, including jumpers and lay-ups, and I suspect lay-ups have a much greater probability of going in than a jumper which would improve the method's output.

To change the inputs to the function, simply open the shotEstimator.py file and change the last line of the file to run the method with whatever player, x and y coordinates, and number of years wanted. Finally, execute the script.
