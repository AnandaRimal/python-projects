import time

def print_heart_art():
    heart = """
       ******       ******
     **      **   **      **
   **         ** **         **
  **           **           **
 **             **             **
**               **               **
 **             **             **
  **           **           **
   **         ** **         **
     **      **   **      **
       ******       ******
    """
    print(heart)

def love_calculator():
    print("Welcome to the Love Calculator! 💖")
    time.sleep(1)
    print_heart_art()
    time.sleep(1)
    
    name1 = input("Enter the first person's name: ")
    name2 = input("Enter the second person's name: ")
    
    combined = name1 + name2
    lowercase = combined.lower()
    
    t = lowercase.count("t")
    r = lowercase.count("r")
    u = lowercase.count("u")
    e = lowercase.count("e")
    true_score = t + r + u + e
    
    l = lowercase.count("l")
    o = lowercase.count("o")
    v = lowercase.count("v")
    e = lowercase.count("e")
    love_score = l + o + v + e
    
    total_score = str(true_score) + str(love_score)
    love_percentage = int(total_score)
    
    print("\nCalculating your love score... 💘")
    for _ in range(3):
        print("❤️", end="", flush=True)
        time.sleep(1)
    print("\n")
    
    print_heart_art()
    print(f"💖 The love score of {name1} and {name2} is: {total_score}% 💖")
    
    if love_percentage < 20:
        print("\nYour love score is like coke and mentos! ⚡️")
    elif love_percentage < 50:
        print("\nYou have an average love score. 💕 Keep working on it!")
    elif love_percentage < 80:
        print("\nYou have a good love score! 💘 A lovely bond!")
    else:
        print("\nYou two are an outstanding couple! 💖🌟 Made for each other!")

love_calculator()

