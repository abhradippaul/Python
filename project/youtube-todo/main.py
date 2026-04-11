# Youtube video manager

# with open("youtube.txt", 'w') as file:
#     file.write("Hello world")

from json import dump, load

file_name = "youtube.txt"

def load_data():
    try:
        with open(file_name, "r") as file:
            file_data = load(file)
            # print(file_data)
            return file_data
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    try:
        with open(file_name, "w") as file:
            dump(videos, file)
    finally:
        print("Video added successfully")

def list_all_videos(videos):
    print()
    print("*" * 70)
    print("List of videos is: ")
    for index, video in enumerate(videos, 1):
        print(f"{index}. {video["name"]}, Duration: {video["time"]} ")

    print("*" * 70)

def add_videos(videos):
    video_name = input("Enter video name: ")
    video_time = input("Enter video time: ")
    videos.append({"name": video_name, "time" : video_time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(videos):
        video_name = input("Enter the video name: ")
        video_time = input("Enter the video duration: ")
        videos[index - 1] = {"name": video_name, "time" : video_time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to delete: "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("Invalid index selected")

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | Choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a you video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        print()
        choice = input("Enter your choice: ")
        print()

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_videos(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()