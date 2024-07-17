
def predict_name():
    # Step 1: Initial letter grid
    letters = [
        ['A', 'B', 'C', 'D'],
        ['E', 'F', 'G', 'H'],
        ['I', 'J', 'K', 'L'],
        ['M', 'N', 'O', 'P'],
        ['Q', 'R', 'S', 'T'],
        ['U', 'V', 'W', 'X'],
        ['Y', 'Z', '', '']
    ]
    
    predicted_name = []
    
    while True:
        # Display current grid
        for row in letters:
            print(' '.join(row))
        
        # Get user input
        column = input("Enter the column number (0-3) containing your letter, or 'done' to finish: ")
        
        if column.lower() == 'done':
            break
        
        try:
            column = int(column)
            if column < 0 or column > 3:
                raise ValueError
            
            # Create new grid based on selected column
            new_letters = [row[column] for row in letters if row[column]]
            
            # Display new grid
            print("Selected letters:")
            for letter in new_letters:
                print(letter)
            
            # Add selected letter to predicted name
            letter_choice = input("Which letter from this column? ").upper()
            if letter_choice in new_letters:
                predicted_name.append(letter_choice)
                print(f"Current name: {''.join(predicted_name)}")
            else:
                print("Invalid letter choice. Please try again.")
            
            # Update letters grid for next iteration
            letters = [new_letters[i:i+4] for i in range(0, len(new_letters), 4)]
            # Pad the last row if necessary
            if len(letters[-1]) < 4:
                letters[-1] += [''] * (4 - len(letters[-1]))
        
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 3.")
    
    print(f"Final predicted name: {''.join(predicted_name)}")

predict_name()