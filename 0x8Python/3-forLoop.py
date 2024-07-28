my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}
total_point = 0
for rank in my_ranks:
    if my_ranks[rank] == 'A':
        total_point += 100
        print(f"My Rank in {rank} Is A and This Equal 100 points")
        
    elif my_ranks[rank] == 'B':
        total_point += 80
        print(f"My Rank in {rank} Is B and This Equal 80 points")

    elif my_ranks[rank] == 'C':
        total_point += 40
        print(f"My Rank in {rank} Is C and This Equal 40 points") 
    else:
        print("Your Rank is not True")       
else:
    print("Total poin is {}".format(total_point))        
