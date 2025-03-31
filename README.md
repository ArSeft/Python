New in 1.5:

  New Features & Improvements:

    Max HP System: Added a maxhp attribute, ensuring HP cannot exceed a maximum value when leveling up or using potions.

    Healing on Level Up: Players now fully recover HP when leveling up.

    Clear Console Functionality: Implemented clear_console() to refresh the screen after actions, improving readability and reducing clutter.

    New Shop Interface: The shop now displays the player’s Gold before purchasing.

  Quality of Life Changes:
    
    Better spacing between texts so it feels less compact and unnatural to read.

    Simplified Mining Input: Players can now press ENTER to mine XP instead of selecting a numbered option.

    More Responsive Menus: Added input("\nPress any key...") to pause the game after key actions, preventing instant screen refresh.

    Health Potions System Refinement:

        Inventory system renamed from inventory to health_potions.

        Potion usage now restores HP to maxhp instead of 100.

  Combat Adjustments:

    Improved Enemy Scaling: Enemy HP and attack now scale more consistently based on player level.

    Escape Confirmation: If a player runs away, the console is cleared for a smoother transition.
