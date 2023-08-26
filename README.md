# Scene Manager

-  ## System
   
  ### **Title**
  - Loads important initial game state info
  - Puts the player in the correct state of the map scene.
  - Exit the game?
  
  ### **Map**
  - Make a Tileset class to handle tiles info
      - Takes in an image
      - And takes in a JSON File with info on the tiles in the tileset
  - Make a map base class
      - Make it take in a tileset class and json file for info
      - Make it take the tileset and info and draw the map
      - Also lay the start of where events on a map will be placed
  - make a scene_map class that loads data from a json file as the map data to  the map base class  and handles it.

  ### **Event**
   - Make a base event with potential controllors for:
      - Movement
      - Combat
      - Decisions/Action
   - Various kinds of events
       - NPC
       - Conditionally triggered event commands
- Base Event has an Array that tells it to move it has a move command inside it.
       - Move Controller handles the logic on how it gets around.
     - Have the ability to multiple pages of event commands that can be set to different pages with an array of booleans or numbers.
  
## Plugin  

### **Event command plugins**
  - plugins to use things in events like
  - Transport to another map
  - Add items, gold, exp, or party members
  - Trigger dialog and/or choices
  - Effects triggered on screen
  - Set movement path
  - And whatever you can think of.
### **Event Controllers**
  - Movement
  - Battle
  - Decision/Action
### **Battle System**
  - ABS Style Battle system or...
  - Battle system that goes into another scene like FF or Pokemon
### **Menu**
  - Menu to interact with player info and save or exit
### **Save/Loading file**
  - Save current game state 
  - Load current game state
### **Items**
  - Ability to Store/Use Items
### **Shop**
  - Ability to use in game currency to purchase items
