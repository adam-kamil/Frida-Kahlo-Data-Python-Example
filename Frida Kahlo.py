

#PROJECT GOAL:
#Congratulations! You’ve been hired to work on a retr3ospective of Frida Kahlo’s work at a major museum in Mexico.
#Your job is to put together the audio tour, but in order to do that, you need to create a list of each painting featured in the exhibit, the date it was painted, and its spot on the tour.
#Use your knowledge of Python lists to create a master list of each painting, its date, and its audio tour ID.

paintings = ['The Two Fridas', 'My Dress Hangs Here', 'Tree Of Hope', 'Self Portrait With Monkeys']
dates = [1939, 1933, 1946, 1940]
paintings = list(zip(paintings, dates))
print (paintings)
paintings.append(('The Broken Column', 1944))
paintings.append(('The Wounded Deer', 1946))
paintings.append(('Me and My Doll', 1937))
print (paintings)
len(paintings)
audio_tour_number = list(range(1, 8))
print (audio_tour_number)
master_list = list(zip(audio_tour_number, paintings))
print (master_list)
