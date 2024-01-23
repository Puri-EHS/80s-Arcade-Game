Recreation of Street Fighter 1 with a twist by Kelyan, Nikil, Ben, Aarna, and Vaibhav. 


**Roles**: 
- Nikil - User Experience 
- Kelyan and Ben - Architecture 
- Aarna - Communication 
- Vaibhav - Testing

**Overview**: 
- Idea: We are going to build Street Fighter but with a twist. While there are mutliple versions that have been released in recent decades, we chose to recreate the original 1987 Street Fighter. The twist would be that there will be power ups that you can activate for 25 seconds by clicking the P key on the keyboard. The player will know that a powerup is activated, as an icon will pop up on the corner of the screen. 
  
- Background: Street Fighter was first released by Capcom in 1987 and its popularity has increased as years have gone by leading 
to multiple updated versions to be released.

- Movation: Across the saturated video game market, fighter games are consistenlty prevelant. Street Fighter was one of the first such fighter games, setting precedents for things like _____. Power Ups are a common feature in many games due to their capabilities to enhance games. We chose to implement Power Ups because they were not added to the original 1987 version but they can make our game more engaging. They create an additional component for the character to control and are also unique to the player selected by the user, leading to more opportunities for the user to strategize customize their experience.
  
- Design Choices Made: One major choice we made was to make our game multiplayer. We looked into creating a computer-controlled player for the user to fight against. But between the limited timeframe for this project and the fact that none of us had experience creating computer-controlled players, we deemed that doing so would be extremely difficult. To ensure that we could still adequately work on the other vital components (such as movements, animations, and fighting abilities), we chose to make our game multiplayer. This would be managable as the only major difference between the two characters would be the controls (one player would use the arrow keys and the other would use WASD). Another design choice made was to display the power-ups through a bar similar to our health bar. Many video games include power-ups and as a result, there are many ways to display them. One common way we considered was dispalying a power-up token at a random location. From here, the player would have to directly go over and 'touch' the power-up to get it and then the effect would immediately begin. However, there would also be more difficulties with this as we would have to sync this with our screen panning and find a way to distinguish between character specific power-ups. Then we implemented an icon that pops up to indicate a power-up is running after a player presses a key that triggers it. This worked to communicate to the user that a power-up was in effect, however it didn't display the time element of power-ups. Thus, we settled on doing a power-up bar that was similar to our health bar. This would indicate how much more time the power-up would be running for as the bar went down every second. 
  
- Anything Interesting:
  
- Instructions to Run the Game: first do the stuff with selecting players and characters. The key controls are detailed below.

Player 1: 
- W: jump 
- D: forward
- A: backward
- F: punch
- G: kick
- H: activate power-up

Player 2
- Up Arrow: jump
- Left Arrow: forward
- Right Arrow: backward
- Period: punch
- Forward Slash: kick
- Shift: activate power-up
  

**Architecture:**

**UX Flow:**
- Experience of a First-Time User (and How They'll Know What to Do): Like most fighting games, the experience of a new user involves many controls to learn. While we have detailed the controls above, there are multiple to memorize and someone who doesn't play games frequently may take more time to adapt. However, because our game is multiplayer, the user can learn the controls without pressure, either by experiementing by themselves or playing against someone for a test-round. 
  
- How is Game Play for an Experienced Player: An experienced player will most likely have limited difficulties with playing our game. After being familiar with the basic instructions, they can focus more on getting to compete with others!
  
- What Will Make the Player Come Back: While our game consists of the same fighting basics everytime, the player has been given many options to customize to make gameplay more interesting. For fun, they have the ability to customize the background. However what affects their gameplay even more is the ability to customize the character they play with. Different characters have varied levels of health, strentgh, and unique powerups. By choosing a different character, the player can approach the same fighting game with a different strategy. In addition, our game is multiplayer as there are two users, each controlling their own fighter. The user can choose who they want to play with, whether its a friend, family member, or someone else. This aspect of choosing who to play against is what makes our game more enjoyable to most players. 

**Retrospection:**

- Process of Writing:
  
- How Our Communication Was:
  
- Major Surprises: dealing w/ sprite sheets
  
- Anything to Improve for Next Time: time management

Sources: 
https://capcom.fandom.com/wiki/Street_Fighter 
https://ehmatthes.github.io/pcc_2e/beyond_pcc/pygame_sprite_sheets/#a-simple-sprite-sheet
