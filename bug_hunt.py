count = 1
total = 0

# syntax error due to missing full colon(:) fix by adding (:) after 5 in while count < 5:
while count <=5:
# total and count were not identified so the loop was 0 to 4(sum=10 not 15) initialize count=1 , total=0 and change condition to <=5
    total = total + count
    count = count + 1
#can only concatenate str (not "int") to str fix by making total a string also (str(total))
print("Sum of 1 to 5 is: " +str(total))