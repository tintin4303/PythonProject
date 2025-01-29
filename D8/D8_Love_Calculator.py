def calculate_love_score(name1, name2):
    name_list = [name1.lower(), name2.lower()]
    true_count = 0
    love_count = 0
    for name in name_list:
        for i in name:
            if i in "true":
                true_count+=1
            if i in "love":
                love_count+=1
    print("Love Score: ",str(true_count) + str(love_count))

calculate_love_score("Kanye West","Kim Kardashian")