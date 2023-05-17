# Working of Horoscope

from random import choices
import random
import time

did=input(print("Enter your name:"))
print("Name:",did)
hi=int(input(print("Enter your Birth Year:")))
age=2022-hi
print("Hi",did,"your age is:",age)

signs = ("taurus","aquarius", "leo","virgo", "sagittarius", "pisces", "libra", "gemini", "cancer", "scorpio","aries", "capricorn", "goat", "moon", "ophiuchus", "capricornus","scorpius", "sun" )
i = str(input('Enter Your Horoscope sign'))
while True:
    if i in signs:
        print(i)
        break
    else:
        print('Please enter proper signs')
        break
color=['red', 'blue', 'green', 'yellow', 'pink', 'black', 'white','purple' ,'cream','orange', 'brown', 'golden', 'silver']
while True:
    if i == "taurus":
        if age >= 50:
            time.sleep(2)
            print(" Give more preferences for God , lucky color=", choices(list(color)))
        elif age >= 30:
            time.sleep(2)
            print(" Didn't be in hurry, lucky color=", choices(list(color)))
        elif age >= 20:
            time.sleep(2)
            print(" Bevare of animals, lucky color=", choices(list(color)))
        elif age>=14:
            time.sleep(2)
            print(" Use water as much as possible, lucky color=", choices(list(color)) )
        elif age>=10:
            time.sleep(2)
            print(" Play outdoor games, lucky color=", choices(list(color)))
        else:
            print(" Be relax just chill, lucky color=", choices(list(color)))
        break

    if i == "leo":
        if age >= 50:
            time.sleep(2)
            print(" Give more preferences for family, lucky color=", choices(list(color)) )
        elif age >= 30:
            time.sleep(2)
            print(" Think and do the work, lucky color=", choices(list(color)) )
        elif age >= 20:
            time.sleep(2)
            print(" Go with excellence, lucky color=", choices(list(color)))
        elif age>=14:
            time.sleep(2)
            print(" Suffer more on your read, lucky color=", choices(list(color)))
        elif age>=10:
            time.sleep(2)
            print(" Hear as much as possible,  lucky color=", choices(list(color)))
        else:
            print(" relax just chill, lucky color=", choices(list(color)))
        break

    if i == "aquarius":
        if age >= 50:
            time.sleep(2)
            print(" Give more preferences for Health, lucky color=", choices(list(color)))
        elif age >= 30:
            time.sleep(2)
            print(" Think a bit before a step ahead, lucky color=", choices(list(color)))
        elif age >= 20:
            time.sleep(2)
            print(" Don't travel for cilly works, lucky color=", choices(list(color)) )
        elif age>=14:
            time.sleep(2)
            print(" Eat healthy foods , lucky color=", choices(list(color)))
        elif age>=10:
            time.sleep(2)
            print(" Don't go to an argument, lucky color=", choices(list(color)) )
        else:
            print(" just chill relax, lucky color=", choices(list(color)))
        break

    if i == "virgo":
        if age >= 50:
            time.sleep(2)
            print(" Bevare of high buildings, lucky color=", choices(list(color)))
        elif age >= 30:
            time.sleep(2)
            print(" Be sensior towards jobs, lucky color=", choices(list(color)) )
        elif age >= 20:
            time.sleep(2)
            print(" Travel a bit, lucky color=", choices(list(color)))
        elif age>=14:
            time.sleep(2)
            print(" Take care of your elders, lucky color=", choices(list(color)) )
        elif age>=10:
            time.sleep(2)
            print(" Don't lack with sleep, lucky color=", choices(list(color)) )
        else:
            print("Relax, just chill, lucky color=", choices(list(color)))
        break

    if i == "sagittarius":
        if age >= 50:
            time.sleep(2)
            print(" Take care of your health more,  lucky color=", choices(list(color)))
        elif age >= 30:
            time.sleep(2)
            print(" Eat more and work more, lucky color=", choices(list(color)))
        elif age >= 20:
            time.sleep(2)
            print(" Describe your feelings to your loved once, lucky color=", choices(list(color)))
        elif age>=14:
            time.sleep(2)
            print(" Listen to your parents more, lucky color=", choices(list(color)))
        elif age>=10:
            time.sleep(2)
            print(" Do the things as you wish with some suggestions,  lucky color=", choices(list(color)))
        else:
            print("relax, just chill,  lucky color=", choices(list(color)))
        break

    if i == "pisces":
        if age >= 50:
            time.sleep(2)
            print(" Take care of your younger once, lucky color=", choices(list(color)))
        elif age >= 30:
            time.sleep(2)
            print(" Don't travel much after sunset, lucky color=", choices(list(color)))
        elif age >= 20:
            time.sleep(2)
            print(" Pray for sun, lucky color=", choices(list(color)) )
        elif age>=14:
            time.sleep(2)
            print(" Be patient and calm yourself, lucky color=", choices(list(color)))
        elif age>=10:
            time.sleep(2)
            print(" Set yourself well,  lucky color=", choices(list(color)))
        else:
            print("Relax just chill, lucky color=", choices(list(color)))
        break

    if i == "libra":
        if age >= 50:
            time.sleep(2)
            print(" Give time to study about peace of mind, lucky color=", choices(list(color)))
        elif age >= 30:
            time.sleep(2)
            print(" Think twice before doing a particular work, lucky color=", choices(list(color)))
        elif age >= 20:
            time.sleep(2)
            print(" Focus more on your passion then success will follow you, lucky color=", choices(list(color)))
        elif age >= 14:
            time.sleep(2)
            print(" Don't worry more about your future just go on with the things, lucky color=", choices(list(color)))
        elif age >= 10:
            time.sleep(2)
            print(" Be friendly with everyone, lucky color=", choices(list(color)))
        else:
            print("Relax just chill, lucky color=", choices(list(color)))
        break

    if i == "gemini":
        if age >= 50:
            time.sleep(2)
            print(" Take a moment of rest, lucky color=", choices(list(color)) )
        elif age >= 30:
            time.sleep(2)
            print(" Don't risk yourself for silly things, lucky color=", choices(list(color)))
        elif age >= 20:
            time.sleep(2)
            print(" Take a breather then go on with the things, lucky color=", choices(list(color)))
        elif age>=14:
            time.sleep(2)
            print(" Beware of water animals, lucky color=", choices(list(color)))
        elif age>=10:
            time.sleep(2)
            print(" Aware of risky situation, lucky color=", choices(list(color)))
        else:
            print("Relax just chill, lucky color=", choices(list(color)))
        break

    if i == "cancer":
        if age >= 50:
            time.sleep(2)
            print(" Listen to more people, lucky color=", choices(list(color)))
        elif age >= 30:
            time.sleep(2)
            print(" Be more friendly towards nature, lucky color=", choices(list(color)))
        elif age >= 20:
            time.sleep(2)
            print(" Be brave and face the situation in easiest manner, lucky color=", choices(list(color)))
        elif age >= 14:
            time.sleep(2)
            print(" Spend less money, lucky color=", choices(list(color)))
        elif age>=10:
            time.sleep(2)
            print(" Be active more in sports, lucky color=", choices(list(color)))
        else:
            print("Relax just chill, lucky color=", choices(list(color)))
        break

    if i == "scorpio":
        if age >= 50:
            time.sleep(2)
            print(" Spend more time with your family, lucky color=", choices(list(color)))
        elif age >= 30:
            time.sleep(2)
            print(" Stay focussed in any situation, lucky color=", choices(list(color)))
        elif age >= 20:
            time.sleep(2)
            print(" Focus more on your passion then success will follow you, lucky color=", choices(list(color)) )
        elif age>=14:
            time.sleep(2)
            print(" Spend more time outside the house for being healthy, lucky color=", choices(list(color)) )
        elif age>=10:
            time.sleep(2)
            print(" Play more with puzzle, lucky color=", choices(list(color)))
        else:
            print("Relax just chill, lucky color=", choices(list(color)))
        break

    if i == "aries":
        if age >= 50:
            time.sleep(2)
            print(" Focus more on your health, lucky color=", choices(list(color)))
        elif age >= 30:
            time.sleep(2)
            print(" Travel as much as possible, lucky color=", choices(list(color)))
        elif age >= 20:
            time.sleep(2)
            print(" Give your more focus in your job, lucky color=", choices(list(color)))
        elif age>=14:
            time.sleep(2)
            print(" Play outdoor game to stay focussed, lucky color=", choices(list(color)))
        elif age>=10:
            time.sleep(2)
            print(" Go with things you like, lucky color=", choices(list(color)))
        else:
            print("Relax just chill, lucky color=", choices(list(color)))
        break

    if i == "capricorn":
        if age >= 50:
            time.sleep(2)
            print(" Reduce the eating of non-veg dishes, lucky color=", choices(list(color)))
        elif age >= 30:
            time.sleep(2)
            print(" Focus more on today, lucky color=", choices(list(color)) )
        elif age >= 20:
            time.sleep(2)
            print(" Reduce overthinking, lucky color=", choices(list(color)))
        elif age>=14:
            time.sleep(2)
            print(" Beware of pets, lucky color=", choices(list(color)))
        elif age>=10:
            time.sleep(2)
            print(" Create your own happiness, lucky color=", choices(list(color)))
        else:
            print("Relax just chill, lucky color=", choices(list(color)) )
        break

    if i == "goat":
        if age >= 50:
            time.sleep(2)
            print(" Sleep more just for the sake of health,  lucky color=", choices(list(color)))
        elif age >= 30:
            time.sleep(2)
            print(" Work hard and result will be more better, lucky color=", choices(list(color)))
        elif age >= 20:
            time.sleep(2)
            print(" Express yourself more, lucky color=", choices(list(color)) )
        elif age>=14:
            time.sleep(2)
            print(" Wait and be patients for better results, lucky color=", choices(list(color)))
        elif age>=10:
            time.sleep(2)
            print(" Achieve your dreams as faster you can,  lucky color=", choices(list(color)))
        else:
            print("Relax just chill, lucky color=", choices(list(color)))
        break

    if i == "moon":
        if age >= 50:
            time.sleep(2)
            print(" Visit near by Temple,  lucky color=", choices(list(color)))
        elif age >= 30:
            time.sleep(2)
            print(" Forget about your past and focus on future, lucky color=", choices(list(color)))
        elif age >= 20:
            time.sleep(2)
            print(" Don't stress yourself be calm, lucky color=", choices(list(color)))
        elif age>=14:
            time.sleep(2)
            print(" Play with the puzzle like games more, lucky color=", choices(list(color)) )
        elif age>=10:
            time.sleep(2)
            print(" Get away from Negative people,  lucky color=", choices(list(color)))
        else:
            print("Relax just chill, lucky color=", choices(list(color)))
        break

    if i == "ophiuchus":
        if age >= 50:
            time.sleep(2)
            print(" Prefer your younger once suggestions, lucky color=", choices(list(color)))
        elif age >= 30:
            time.sleep(2)
            print(" Go on your own way which makes you happy, lucky color=", choices(list(color)))
        elif age >= 20:
            time.sleep(2)
            print(" Make the better decisions,  lucky color=", choices(list(color)))
        elif age>=14:
            time.sleep(2)
            print(" Take rest and restart the things,  lucky color=", choices(list(color)))
        elif age>=10:
            time.sleep(2)
            print(" Give your best in your job,  lucky color=", choices(list(color)))
        else:
            print("Relax just chill, lucky color=", choices(list(color)))
        break

    if i == "capricornus":
        if age >= 50:
            time.sleep(2)
            print(" Aware of different difficulties,  lucky color=", choices(list(color)))
        elif age >= 30:
            time.sleep(2)
            print(" Wait for results for further actions, lucky color=", choices(list(color)))
        elif age >= 20:
            time.sleep(2)
            print(" Do the work in belief of luck,  lucky color=", choices(list(color)))
        elif age>=14:
            time.sleep(2)
            print(" Take fresh air and restart the work,  lucky color=", choices(list(color)))
        elif age>=10:
            time.sleep(2)
            print(" Don't be shy for silly reasons, lucky color=", choices(list(color)))
        else:
            print("Relax just chill, lucky color=", choices(list(color)))
        break

    if i == "scorpius":
        if age >= 50:
            time.sleep(2)
            print(" Do the work which your heart likes,  lucky color=", choices(list(color)))
        elif age >= 30:
            time.sleep(2)
            print(" Take care of your elders, lucky color=", choices(list(color)))
        elif age >= 20:
            time.sleep(2)
            print(" Don't get into any relationship without any advise,  lucky color=", choices(list(color)))
        elif age>=14:
            time.sleep(2)
            print(" Find your own happiness,  lucky color=", choices(list(color)))
        elif age>=10:
            time.sleep(2)
            print(" Be good and do good, lucky color=", choices(list(color)))
        else:
            print("Relax just chill,  lucky color=", choices(list(color)))
        break

    if i == "sun":
        if age >= 50:
            time.sleep(2)
            print(" Find more better way to do work,  lucky color=", choices(list(color)))
        elif age >= 30:
            time.sleep(2)
            print(" Don't worry about others words, lucky color=", choices(list(color)))
        elif age >= 20:
            time.sleep(2)
            print(" Worry more about others and you will be taken care of,  lucky color=", choices(list(color)))
        elif age >= 14:
            time.sleep(2)
            print(" Listen more words of your elders,  lucky color=", choices(list(color)))
        elif age>=10:
            time.sleep(2)
            print(" Think a bit and then enter to friendship zone,  lucky color=", choices(list(color)))
        else:
            print("Relax just chill,  lucky color=", choices(list(color)))
        break
