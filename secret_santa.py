#!/usr/bin/env python3

import random
import sys

def create_secret_santa_pairings(names):
    """
    Create Secret Santa pairings where no one is assigned to themselves.
    
    Args:
        names (list): List of participant names
        
    Returns:
        dict: Dictionary mapping givers to receivers
    """
    if len(names) < 2:
        print("Error: Need at least 2 participants for Secret Santa.")
        sys.exit(1)
    
    # Make a copy of the names list to avoid modifying the original
    receivers = names.copy()
    
    # Shuffle the receivers list
    random.shuffle(receivers)
    
    # Check if anyone is assigned to themselves
    for i in range(len(names)):
        if names[i] == receivers[i]:
            # If someone is assigned to themselves, swap with the next person
            # (or the first person if we're at the end of the list)
            next_idx = (i + 1) % len(names)
            receivers[i], receivers[next_idx] = receivers[next_idx], receivers[i]
    
    # Double-check no one is assigned to themselves
    for i in range(len(names)):
        if names[i] == receivers[i]:
            # Try again with a different shuffle
            return create_secret_santa_pairings(names)
    
    # Create the pairings dictionary
    pairings = {}
    for i in range(len(names)):
        pairings[names[i]] = receivers[i]
    
    return pairings

def main():
    print("🎅 Secret Santa Pairing Generator 🎁")
    print("-----------------------------------")
    
    # Get participants from user input
    print("Enter participant names (one per line).")
    print("When finished, enter a blank line.")
    
    names = []
    while True:
        name = input("Name: ").strip()
        if not name:
            break
        names.append(name)
    
    if len(names) < 2:
        print("Error: Need at least 2 participants for Secret Santa.")
        return
    
    while True:
        # Create the pairings
        pairings = create_secret_santa_pairings(names)
        
        # Display the results
        print("\n🎄 Secret Santa Pairings 🎄")
        print("-------------------------")
        for giver, receiver in pairings.items():
            print(f"{giver} → {receiver}")
        
        # Ask if user wants to reshuffle
        reshuffle = input("\nWould you like to reshuffle? (y/n): ").strip().lower()
        if reshuffle != 'y':
            break
    
    print("\nHappy Holidays! 🎄🎁")

if __name__ == "__main__":
    main()