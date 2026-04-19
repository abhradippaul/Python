# Youtube todo mongodb

from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
from os import getenv

def connect_mongodb():
    try:
        load_dotenv()
        MONGO_URI = getenv("MONGO_URI")
        print("Youtube todo mongodb")
        client = MongoClient(MONGO_URI, tlsAllowInvalidCertificates=True)
        db = client["python_practice"]
        return db["videos"]
    except Exception as e:
        print(str(e))

video_collection = connect_mongodb()

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video["_id"]}, Name: {video["name"]}, time: {video["time"]}")

def add_video(name, time):
    video_collection.insert_one({"name": name, "time" : time})

def update_video(video_id, video_name, video_duration):
    video_collection.update_one({"_id": ObjectId(video_id)}, {"$set":{"name": video_name, "time": video_duration}})

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})


def main():
    while True:
        print("\n Youtube Manager with DB | Choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a you video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        print()
        try:
            choice = input("Enter your choice: ")
        except KeyboardInterrupt:
            print("\nThank you for using the application")
            exit()
        print()

        match choice:
            case "1":
                list_videos()
            case "2":
                video_name = input("Enter the video name: ")
                video_duration = input("Enter the video duration: ")
                add_video(video_name, video_duration)
            case "3":
                video_id = input("Enter the video id to update: ")
                video_name = input("Enter the video name: ")
                video_duration = input("Enter the video duration: ")
                update_video(video_id, video_name, video_duration)
            case "4":
                video_id = input("Enter the video id to delete: ")
                delete_video(video_id)
            case "5":
                break
            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()