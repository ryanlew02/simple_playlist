class Node:


    def __init__(self, title: str, artist: str):
        self.title = title
        self.artist = artist
        self.prev = None
        self.next = None



class Playlist:

    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def add_song(self, title: str, artist: str):
        node_to_add = Node(title, artist)
        if self.head is None and self.tail is None and self.current is None:
            self.head = node_to_add
            self.tail = node_to_add
            self.current = node_to_add
        else:
            self.tail.next = node_to_add
            node_to_add.prev = self.tail
            self.tail = node_to_add 

    def show_playlist(self):
        if not self.head:
            print("Playlist is empty!")
            return
        count = 1
        curr_node = self.head
        print("---------Start of Playlist!---------")
        while (curr_node):
            if curr_node == self.current:
                print(f"--> {count}. {curr_node.title} - {curr_node.artist}")
            else:
                print(f"{count}. {curr_node.title} - {curr_node.artist}")
            count += 1
            curr_node = curr_node.next
        print("---------End of Playlist!---------")

    def next_song(self):

        if not self.current:
            print("No current song.")
            return



        if self.current.next:
            self.current = self.current.next
        elif self.head:
            self.current = self.head
        else:
            print("Cannot go to next song")

    def prev_song(self):
        if not self.current:
            print("No current song.")
            return


        if self.current.prev:
            self.current = self.current.prev
        elif self.tail:
            self.current = self.tail
        else:
            print("Cannot go to previous song")

    def current_song(self):
        if not self.current:
            print("No current song")
            return
        print(f"Current song: {self.current.title} - {self.current.artist}")


    def delete_current(self):

        if not self.current:
            print("No current song to delete.")
            return 

        if self.head == self.tail == self.current:
            self.head = None
            self.tail = None
            self.current = None
            return
        

        if self.current == self.head:
            new_head = self.head.next
            new_head.prev = None
            self.head.next = None
            self.head = new_head
            self.current = new_head
            return

        if self.current == self.tail:
            new_tail = self.tail.prev
            new_tail.next = None
            self.tail.prev = None
            self.tail = new_tail
            self.current = new_tail
            return

        
        prev_node = self.current.prev
        next_node = self.current.next

        prev_node.next = next_node
        next_node.prev = prev_node

        self.current = next_node
        

def main():
    playlist = Playlist()

    while True:
        print("\nCommands: add, show, next, prev, current, delete, quit")
        cmd = input("> ").strip().lower()

        if cmd == "add":
            title = input("Song title: ")
            artist = input("Artist: ")
            playlist.add_song(title, artist)
        elif cmd == "show":
            playlist.show_playlist()
        elif cmd == "next":
            playlist.next_song()
        elif cmd == "prev":
            playlist.prev_song()
        elif cmd == "current":
            playlist.current_song()
        elif cmd == "delete":
            playlist.delete_current()
        elif cmd == "quit":
            break
        else:
            print("Unknown Command")


main()