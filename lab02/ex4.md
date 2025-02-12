### 1. Describe the algorithm you will use to find the room. Assume all the information you have is the one given by the sign; you have no knowledge of the floor plan [0.5 pts] 

I would go through the floor and compare each room with the room number I have to see which is the correct one (Linear search).


### 2. How many "steps" it will take to find room EY128? And what is a "step" in this case? [0.25 pts] 

In this case it would take 15 steps as we would need to compare 15 rooms with the desired room number before
actually reaching our goal. A "step" in this case is comparing each room number and checking if it is EY128.


### 3. Is this a best-case scenario, worst-case scenario, or neither? [0.25 pts] 

The best-case scenario would have been if the room number EY128 was the first room checked, the worst-case 
scenario would've been if EY128 was the last room in the layout. However, as EY128 was in the middle it was neither
worse-case nor best-case.


### 4. With this particular sign and floor layout, explain what a worst-case or best-case scenario would look like [0.5 pts] 

The best-case scenario as stated prior would've been if the room desired was the first room. So in this layout if the room we were
looking for was room EY100 would be the best-case scenario. As for the worst-case scenario it would be if we were looking for 
room EY138 as that room is last room that would be checked in the layout.

### 5. Suppose after a few weeks in the term you memorize the layout of the floor. How would you improve the algorithm to make it more efficient? [0.5 pts]

When searching for a room I would first start at the middle of the section, which would be room EY118. If the room number of the
the desired room was larger I would personally go to the middle of room EY118 and EY138, if it was smaller I would go to the middle of EY100 and EY118. I would use this method (Binary Search) to continue this process of breaking the amount of rooms required to search in half until I found the room desired.