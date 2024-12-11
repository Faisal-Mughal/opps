
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")



class EBook(Book):
    def __init__(self, title, author, genre, file_size):
        super().__init__(title, author, genre)
        self.file_size = file_size

    def display_info(self):
        super().display_info()
        print(f"File Size: {self.file_size} MB")



class AudioBook(Book):
    def __init__(self, title, author, genre, duration):
        super().__init__(title, author, genre)
        self.duration = duration

    def display_info(self):
        super().display_info()
        print(f"Duration: {self.duration} hours")



def main():
   
    regular_book = Book("Bang.e.Dara", "Iqbal", "Fiction")
    ebook = EBook("Tow Nation Theory", "Syed Ahmed Khan", "knowledge", 9)
    audiobook = AudioBook("Hamd", "Hafeez Jalandhari", "Allah", 10)

    
    print("Regular Book Info:")
    regular_book.display_info()
    print("\nEBook Info:")
    ebook.display_info()
    print("\nAudioBook Info:")
    audiobook.display_info()



if __name__ == "__main__":
    main()