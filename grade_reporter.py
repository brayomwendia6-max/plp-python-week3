scores = [72, 45, 90, 61, 38]
passed = 0
failed = 0
total = 0


for score in scores:
    if score >=80:
       Grade = "A"

    elif score >=70:
        Grade = "B"

    elif score >=50:
        Grade = "C"

    else:
      #  below 50
      Grade = "F"

    print(f"{score}: {Grade}")

      # count pass/fail
    if score >= 50:
         passed +=1

    else:
        failed +=1
     
Total = sum(scores)
average = Total / len(scores)
print(f"passed: {passed}")
print(f"failed: {failed}")
print(f"Average: {round(average, 1)}")