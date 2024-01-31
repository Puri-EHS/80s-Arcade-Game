Recreation of Street Fighter 1 with a twist by Kelyan, Nikil, Ben, Aarna, and Vaibhav. 


**Roles**: 
- Nikil - User Experience 
- Kelyan and Ben - Architecture 
- Aarna - Communication 
- Vaibhav - Testing

**Overview**: 
- Idea: We are going to build Street Fighter but with a twist. While there are mutliple versions that have been released in recent decades, we chose to recreate the original 1987 Street Fighter. The twist would be that there will be power ups that you can activate for 25 seconds by clicking the P key on the keyboard. The player will know that a powerup is activated, as a powerup bar will pop up on the corner of the screen. 
  
- Background: Street Fighter was first released by Capcom in 1987 and its popularity has increased as years have gone by leading to multiple updated versions to be released.

- Movation: Across the saturated video game market, fighter games are consistenlty prevelant. Street Fighter was one of the first such fighter games. As none of us have coded a fighting game before, we thought that choosing this game would be challenging for us yet also doable withing our given time frame. Power Ups are a common feature in many games due to their capabilities to enhance games. We chose to implement Power Ups because they were not added to the original 1987 version but they can make our game more engaging. They create an additional component for the character to control and are also unique to the player selected by the user, leading to more opportunities for the user to strategize customize their experience.
  
- Design Choices Made: One major choice we made was to make our game multiplayer. After looking into creating a computer-controlled player for the user to fight against, we deemed that it would be difficult for us to implement as none of us have previous experience with it. We also felt that this may be hard to complete withing our given time frame for the project. Thus, we decided to make our game multiplayer. There were other factors that influenced us to make this choice as well. Making the game multiplayer meant that it would be more engaging for our users. Since much of the fighting element of our game stays consistent each round, allowing the user to play with others in real life allows for more customization and enjoyment! Another design choice we made was how we wished to display the Power Ups. As power ups are extremely common in video games, there were several ways that we were familiar with that we considered. One way was having a moving icon that the player had to 'hit' to activate the power up, yet this would also be more time-consuming to implement. Another way was having an icon be displayed to indicate that the power up is running when the user clicks the power up key. We began by implementing this format, and through this process we realized that just displaying an icon meant that the user wouldn't know how much time they had left since we had limited this. So, we switched over to a bar similiar to our health bar that decreased as time passed to indicate how much time the user had left.  
  
- Anything Interesting: There are more complexities to game movements in fighting then we anticipated. Specifically, if a character is moving forward, backwards, or jumping, we can create controls and animations for that. If they are punching or kicking, we can also create controls and animations for that. However, many games often allow players to do both at the same time, a feature takes more consideration for both animations and controls. 
  
- Instructions to Run the Game:
  
  First, run the 'Game.py' file and a window should be displayed. Here, to move to the next screen, you must press **space**. Then, you will reach the character select screen. As our game is 2-player, a character must be selected for each player (the first character selected will automatically be assigned to player 1). To move around between characters, use the **arrow keys**. To select a specific character, press **enter**. Now, you must select which map you want to play on. Use the **right and left arrow keys** to scroll between the options, then press **space** once you've selected a map (you should press space when your selected map is displayed in the middle). From here, both players can fight. The key controls for fighting are detailed below.

Player 1: 
- W: jump 
- D: forward
- A: backward
- F: punch
- G: kick
- P: activate power-up

Player 2
- Up Arrow: jump
- Left Arrow: forward
- Right Arrow: backward
- Period: punch
- Forward Slash: kick
- Shift: activate power-up

Once a player dies, the window will automatically progress to the game over screen. Here, press the **space bar** to restart the game and press **enter** to end the game.


**Architecture:**

![image](https://github.com/kwandji113/80s-Arcade-Game/assets/90006860/fda7e2d8-f2a5-4b27-896e-3452ff39180f)

![image](https://github.com/kwandji113/80s-Arcade-Game/assets/90006860/3e946118-4217-4d03-9da4-71e76d6088d7)

- Architectural choices made: We chose to make a  class for the player and then create children classes for each of the players. This is because both players have many same functions needed such as attacking and updating health, however they each have different controls so both players can play at the same time. Additionally, we chose to make each of their own screens their own class or function (given more time we would've made fight screen and the game over screen their own class). This is because having them all in screen state originally made it very convoluted and hard to both follow and work on (we had to do a lot of scrolling). Splitting it up made our code easier to debug and also more organized. 


**UX Flow:**
- Experience of a First-Time User (and How They'll Know What to Do): Like most fighting games, the experience of a new user involves many controls to learn. While we have detailed the controls above, there are multiple to memorize and someone who doesn't play games frequently may take more time to adapt. However, because our game is multiplayer, the user can learn the controls without pressure, either by experiementing by themselves or playing against someone for a test-round. 
  
- How is Game Play for an Experienced Player: An experienced player will most likely have limited difficulties with playing our game. After being familiar with the basic instructions, they can focus more on getting to compete with others!
  
- What Will Make the Player Come Back: While our game consists of the same fighting basics everytime, the player has been given many options to customize to make gameplay more interesting. For fun, they have the ability to customize the background. However what affects their gameplay even more is the ability to customize the character they play with. Different characters have varied levels of health, strentgh, and unique powerups. By choosing a different character, the player can approach the same fighting game with a different strategy. In addition, our game is multiplayer as there are two users, each controlling their own fighter. The user can choose who they want to play with, whether its a friend, family member, or someone else. This aspect of choosing who to play against is what makes our game more enjoyable to most players. 

**Retrospection:**

- Process of Writing: Our writing proces for this project began by each of us taking on tasks. As these tasks were of different complexities and lengths, we generally determined what to work on next in a case-by-case bases when we completed them. As we continued making progress, we often had to go back to code we already wrote and adjust it or restructure it to be compatible with our new code.
  
- How Our Communication Was: In class, we communicated by simply asking each other questions when sitting next to each other and participating in stand ups. When group members were absent or we had questions out of class, we used a text groupchat we formed at the beginning of this process.
  
- Major Surprises: We didn't anticipate the difficulties in dealing with sprite sheets. We planned to use sprite sheets for our animations. However, this process took longer than anticipated because we didn't realize that to make our animations work, we had to split up the sprite sheet picture into smaller, centered pictures, something that was difficult to figure. 
  
- Anything to Improve for Next Time: In the future, if we were to approach this project again, something that we would change would be our planning and time management. If we were to set better internal deadlines and be more efficent, we may have been able to accomplish more in our game. Another thing we would change is when we are working on individual tasks, we'd spend more effort on making our code more concise and including comments. This way, it would be easier for us to understand each other's code, and can more easily make changes as needed. 

**Sources:**

https://capcom.fandom.com/wiki/Street_Fighter 

https://ehmatthes.github.io/pcc_2e/beyond_pcc/pygame_sprite_sheets/#a-simple-sprite-sheet

https://www.pygame.org/docs/
