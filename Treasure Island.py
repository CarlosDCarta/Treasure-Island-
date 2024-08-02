
print(''' (_      __)
 .||~"~~b. 
 |||:.:::|
 `||::::p'
  ||b:d||
  ||p:q||
 .|| : `b.
 ||| .   |
 _||::::p_
(_________)''')

print("Welcome to tresure island!")
print("Your mission is to find the tresure.")
first_ans = str(input("Choose a path. Left or right? ")).lower() #we can lower inline
if first_ans == "left":
    print("Gameover")
else:
    second_ans = str(input("You reach a river. Do you swim or wait?"))
    second_ans = second_ans.lower()
    if second_ans == "swim":
        print("Game over")
    else:
        third_ans = str(input("You made it to three doors. Choose either: Blue, Red, Yellow."))
        third_ans = third_ans.lower()
        if third_ans == "red" or "yellow":
            print("Game Over")
        else:
            print("You Win!")

