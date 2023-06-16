

game=[
    {"Question":{"Question_text":"You_name","Option 1":"Ankit","Option 2":"Das","Correct option":"1"}},
    {'Question':{"Question_text":"last_name","Option 1":"Ankit","Option 2":"Das","Correct option":"2"}}
]
choice=[]
for each_item in game:
    print(each_item['Question']['Question_text'])
    print(f"1-{each_item['Question']['Option 1']}")
    print(f"2-{each_item['Question']['Option 2']}")
    choice.append(int(input("Enter the correct option ")))
i=0
for each in game:
    if int(each['Question']["Correct option"])==choice[i]:
        print(f"Correct Answer:User Answer:{choice[i]},Correct Answer:{each['Question']['Correct option']}")
    else:
        print(f"Incorrect Answer:User Answer:{choice[i]},Correct Answer:{each['Question']['Correct option']}")
    i+=1
