from matplotlib import pyplot as plt

hobby = ["Coding","Learning","Reading",'Chatting','S Media','Business','Drinking','RS status','Gaming','Leading','Money',"Broke","Women",'Losing','Winning']
rating = [9.5,10,6.5,5.8,7,9,5,3.5,9,9.2,9.8,0.1,7,0.5,10]

plt.bar(range(len(hobby)), rating)
plt.plot(range(len(hobby)), rating, marker = '*',color = 'orange')
#create your ax object here
ax = plt.subplot()
ax.set_xticks(range(len(hobby)))
ax.set_xticklabels(hobby)
plt.title("Just A Funny Meo Rating... Haha", color = 'green')
plt.xlabel("A list of things I know of ... Hehehe", color = 'blue')
plt.ylabel("Rating Over 10",color = 'blue')


plt.show()
