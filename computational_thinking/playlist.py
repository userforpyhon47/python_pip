from queque import NodeBasedQueue
import random

class Track:
    def __init__(self, name=None, duration=0) -> None:
        self.name = name
        self.duration = duration
    
    def __str__(self):
        return f"{self.name} - {self.duration}"

class PlayList:
    def __init__(self) -> None:
        self.queue = NodeBasedQueue()

    def add_song(self, data: Track):
        self.queue.enqueue(data)
    
    def next_song(self):
        return self.queue.dequeue()

    def show_songs(self):
        return self.queue

if __name__ == "__main__":

    song_list = [f"Song {x}" for x in range(10)]

    playlist = PlayList()

    [playlist.add_song(Track(song, random.randint(1, 5))) for song in song_list]


for song in playlist.show_songs():
    print(song)
    