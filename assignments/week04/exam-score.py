score_list = []
for i in range(5):
    score = int(input(f"Enter score of student {i+1}: "))
    score_list.append(score)

print("")

for s in range(len(score_list)):
    if score_list[s] >= 50:
        print(f"Student {s + 1}: {score_list[s]} -> ผ่าน")
    else:
        print(f"Student {s + 1}: {score_list[s]} -> ไม่ผ่าน")   