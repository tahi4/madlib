# madlibs

# word inputs

animal = input("Animals: ")
feeling = input("Feeling: ")
things1 = input("Things (plural): ")
professional = input("A Professional (like “Baker”): ")
clothing = input("A Piece of Clothing: ")
things2 = input("Things (plural): ")
person = input("A Person: ")
place = input("A Place:")
verb_ing = input("Verb (ending in “ing”):")
food = input("Food: ")

# actual madlib, added f" " so i can use other input variables 

madlib = f"Say '{food},' the photographer said as the camera flashed! {person} and I had gone to the {place} to get our photos taken today. The first photo we really wanted was a picture of us dressed as {animal} pretending to be a {professional}. When we saw the proofs of it, I was a bit {feeling} because it looked different than in my head. (I hadn't imagined so many {things1} behind us.) However, the second photo was exactly what I wanted. We both looked like {things2} wearing {clothing} and {verb_ing} --exactly what I had in mind!"

print(madlib)
