This project is a simple music playlist application implemented in Python.
It uses a custom doubly linked list, not Python lists, to manage songs.

You can:
- Add songs
- View the playlist
- Navigate forward/backward between songs.
- See the currently selected song
- Delete songs
- Loop between the beginning and the end of the list

The purpose of this project is to practice fundamental data structure concepts:
- Nodes
- Pointers (prev/next)
- Edge cases (head/tail deletion, empty list, etc.)

Features:
- Add song: Append a new song to the end of the playlist.
- Show Playlist: Print songs in order, highlighting the current track.
- Next / Previous Song: Navigate through songs (wraps around).
- Delete current song: Safely remove the current node from the list.
- Interactive CLI: Simple command-line user interface.
