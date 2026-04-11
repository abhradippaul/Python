# Youtube todo sqllite

import sqlite3

print("Youtube todo sqllite")

def load_data():
    pass

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(video_id, video_name, video_duration):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(video_name, video_duration, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id, ))
    conn.commit()

conn = sqlite3.connect("youtube_videos.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL
    )
''')

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

    conn.close()

if __name__ == "__main__":
    main()