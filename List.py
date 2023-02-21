#learning list
bycicle = ['walk','trek','hustle']
print(bycicle[-1].title())

message = f"My First bike was {bycicle[2].title()}"
print(message)

#chapter 3 taks
Names = ['Fife','Olu','Bishop','terah','Hills','Dayo']
print(Names[0].title())
print(Names[1].title())
print(Names[2].title())
print(Names[3].title())
print(Names[4].title())
print(Names[5].title())

message = f"Hello my beloved friend {Names[0].title()}"
message1 = f"Hello my beloved friend {Names[1].title()}"
message2 = f"Hello my beloved friend {Names[2].title()}"
message3 = f"Hello my beloved friend {Names[3].title()}"
message4 = f"Hello my beloved friend {Names[4].title()}"
message5 = f"Hello my beloved friend {Names[5].title()}"


print(message)
print(message2)
print(message1)
print(message3)
print(message4)
print(message5)



cars = ['motor','toy','tesla']
print(f"I'd like to own a {cars[2].upper()}, what abt you?")
print(f"I'd like to own a {cars[1].upper()}, what abt you?")
print(f"I'd like to own a {cars[0].upper()}, what abt you?")

#changing element value
New_List = ['hoda', 'suziki','omne']
print(New_List)
New_List[0] = 'carryme'
print(New_List)

#adding element 

New_List.append('omo')
print(New_List)

#addingvalues to begining of list

New_List.insert(0, 'whyme')
print(New_List)

#deleting entry

del New_List[0]
print(New_List)

popped_new_list = New_List.pop()
print(New_List)

last_new = New_List.pop()

print(f"the last kini {last_new.title()}")

#remove 

New_List.remove('suziki')
print(New_List)



guest_list = ['obs', 'destiny', 'favour', 'dami']
print(f"hello {guest_list[0]} You're invited for dinner")
print(f"hello {guest_list[1]} You're invited for dinner")
print(f"hello {guest_list[2]} You're invited for dinner")
print(f"hello {guest_list[3]} You're invited for dinner")

print(f"{guest_list[3]} cannot make it")

guest_list[3] = 'omo'

print(f"hello {guest_list[0]} You're invited for dinner")
print(f"hello {guest_list[1]} You're invited for dinner")
print(f"hello {guest_list[2]} You're invited for dinner")
print(f"hello {guest_list[3]} You're invited for dinner")


print("We found a bigger dinner table.")

guest_list.insert(0, 'MyGod')
guest_list.insert(3, 'whyme')
guest_list.append('tesla')

print(guest_list)

print(f"hello {guest_list[0]} You're invited for dinner")
print(f"hello {guest_list[1]} You're invited for dinner")
print(f"hello {guest_list[2]} You're invited for dinner")
print(f"hello {guest_list[3]} You're invited for dinner")

guest_list.remove('omo')

print(guest_list)

print(f"hello {guest_list[0]} You're invited for dinner")
print(f"hello {guest_list[1]} You're invited for dinner")
print(f"hello {guest_list[2]} You're invited for dinner")
print(f"hello {guest_list[3]} You're invited for dinner")
print(f"hello {guest_list[4]} You're invited for dinner")
print(f"hello {guest_list[5]} You're invited for dinner")


print("We can only invite two people for dinner")

uninvited = guest_list.pop()
print(f"{uninvited}, so sorry")
uninvited = guest_list.pop()
print(f"{uninvited}, so sorry")
uninvited = guest_list.pop()
print(f"{uninvited}, so sorry") 
uninvited = guest_list.pop()
print(f"{uninvited}, so sorry")

print(guest_list)
print(f"hello {guest_list[0]} You're invited for dinner")
print(f"hello {guest_list[1]} You're invited for dinner")

# del guest_list[1]
# del guest_list[0]

print(guest_list)

Car_i_will_buy = ['Tesla','BMW','MessiBenz','Tesla','BMW','MessiBenz']
Car_i_will_buy.sort(reverse=False)
print(Car_i_will_buy)

print(sorted(Car_i_will_buy))
print(Car_i_will_buy)

Car_i_will_buy.reverse()
Car_i_will_buy.reverse()

print(Car_i_will_buy)

print(len(Car_i_will_buy))

I_would_like_to_visit = ['dubi','paris', 'mumbai','america']
print(I_would_like_to_visit)

print(sorted(I_would_like_to_visit))
print(I_would_like_to_visit)

I_would_like_to_visit.reverse()
print(I_would_like_to_visit)

I_would_like_to_visit.reverse()
print(I_would_like_to_visit)

I_would_like_to_visit.sort()
print(I_would_like_to_visit)

I_would_like_to_visit.sort(reverse=True)
print(f"{I_would_like_to_visit[0].title()}")
print(f"{I_would_like_to_visit[1].title()}")
print(f"{I_would_like_to_visit[2].title()}")
print(f"{I_would_like_to_visit[3].title()}")


guest_list1 = ['obs', 'destiny', 'favour', 'dami']
print(f"There are {len(guest_list1)} guest at our party")

Items = ['apple', 'mountains','people','happy']

Items[3]='sad'
print(Items)
Items.append('sun')
Items.insert(2, 'young')
Items.remove('sad')
del Items[0]
Items.reverse()
print(len(Items))
print(Items)

