
''' YouTube and Instagram Scrapper by Rishu
    Only Public insta Id get Scrapped '''

import instaloader
from pytube import YouTube


def start():   #Function that run at the beginning

    print('''
    1. YouTube Scrapping 
    2. Instagram Scrapping
    3. Exit
    ''')

    choice = int(input("Enter Your Choice : "))
    if choice==1:
        result=yt()
        print(result)
    elif choice==2:
       result=insta()
       print(result)
    elif choice==3:
        print("\n Thank You :) ")
        print("\n")
    else:
        result=start()
        print(result)
        

def yt():      #Function for YouTube Scrapping and Downloading.         

    link = input("\n Please Enter Youtube Video Link : ")
    print("\n")
    yt = YouTube(link)
    # To print title
    print("Title :", yt.title)
    # To get number of views
    print("Views :", yt.views)
    # To get the length of video
    print("Duration in Seconds :", yt.length)
    # To get description
    print("Description :", yt.description)
    # To get ratings
    print("Ratings :", yt.rating)

    choice = input("\n Do you want to Download this video (Y/N) : ")
    print("\n")
    if (choice.lower()=='y'):
        print("\n Downloading.... ")
        stream = yt.streams.get_highest_resolution()
        stream.download()
        print("\n Download completed!! \n")
        result=start()
    elif(choice.lower()=='n'):
        print("\n Download Cancel \n")
        result=start()
    else:
        print("\n Invalid Input  \n")
        result=start()

def insta():       #Function for Instagram Scrapping and Downloading.

    bot = instaloader.Instaloader()

    id = input("\n Enter the Instagram id : ")
    # Load a profile from an Instagram handle
    profile = instaloader.Profile.from_username(bot.context, id)

    print("\n")

    print("Username: ", profile.username)
    print("User ID: ", profile.userid)
    print("Number of Posts: ", profile.mediacount)
    print("Followers: ", profile.followers)
    print("Followees: ", profile.followees)
    print("Bio: ", profile.biography,profile.external_url)

    choice = input("\n Do you want to Download All Posts (Y/N) : ")
    if (choice.lower()=='y'):
        print("\n Downloading....\n")
        posts = profile.get_posts()
        for index, post in enumerate(posts, 1):
            bot.download_post(post, target=f"{profile.username}_{index}")
        print("\n Download completed!! \n")
        result=start()
    elif(choice.lower()=='n'):
        print("\n Download Cancel \n")
        result=start()
    else:
        print("\n Invalid Input  \n")
        result=start()

if __name__ == "__main__":   #Main Function
    start()