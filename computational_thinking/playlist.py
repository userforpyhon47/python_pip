from queque import NodeBasedQueue


class PlayList:
    def __init__(self) -> None:
        self.queue = NodeBasedQueue()

    def add_song(self, data):
        self.queue.enqueue(data)
    
    def next_song(self):
        return self.queue.dequeue()

    def show_songs(self):
        return self.queue

if __name__ == "__main__":

    song_list = [f"Song {x}" for x in range(10)]

    playlist = PlayList()

    [playlist.add_song(song) for song in song_list]


for song in playlist.show_songs():
    print(song)
    