###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background ("summer")
q1 = codesters.Square (100,100,200,'white')
q2 = codesters.Square (-100,100,200,'red')
q3 = codesters.Square (-100,-100,200,'pink')
q4 = codesters.Square (100,-100,200,'orange')

s1 = codesters.Sprite("cardinal", 100, 100)
s2 = codesters.Sprite("dog.gif", -100, 100)
s2.set_size(0.2)
s3 = codesters.Sprite("shopping-bags.png", -100, -100)
s3.set_size(0.5)
s4 = codesters.Sprite("Starbucks.gif", 100, -100)
s4.set_size(0.3)



message1 = codesters.Text ("Stella Tangen", 0, 220) 
message2 = codesters.Text ("Turning in Project 1", 0, -220)
