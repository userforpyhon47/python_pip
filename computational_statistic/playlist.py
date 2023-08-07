class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Playlist:
    def __init__(self):
        self.bottom = None
        self.top = None
        self.length = 0

    def addSong(self, song):
        new = Node(song)

        if self.bottom == None:
           self.bottom = new
           self.top = self.bottom
        else:
           new.next = self.top
           self.top = new

        self.length += 1

    def playSong(self):
        node = self.top
        
        if node is None:
           raise Exception("No hay canciones en la lista")
        
        self.top = self.top.next
        self.length -= 1

        return node.value

    def getPlaylist(self):
        return [item for item in self]

    def __iter__(self):
       node = self.top
       while node:
          yield node.value
          node = node.next

if __name__ == "__main__":
   
    playlist = Playlist()

    playlist.addSong("Bohemian Rhapsody")
    playlist.addSong("Stairway to Heaven")
    playlist.addSong("Hotel California")

    print(playlist.getPlaylist()) 


    print(playlist.playSong())
    print(playlist.playSong())
    print(playlist.playSong())
    print(playlist.playSong())
