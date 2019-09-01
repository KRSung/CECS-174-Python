class Media:  # Super class with constructor
    def __init__(self, title, author, publisher):
        self.title = title
        self.author = author
        self.publisher = publisher

    def getInfo(self):  # Function retrieves information about the book or movie
        if self.__class__.__name__ == 'Book':
            return (' Book--> {} written by {}'.format
                    (self.title, self.author))
        else:
            return (' Video--> {} mins video {}, created by {}'.format
                    (self.running_time, self.title, self.author))


class Book(Media):
    book_dict = {}  # Dictionary created to store all book instances associated with member name
    book_count = 0  # Counter for amount of videos

    def __init__(self, title, author, publisher, number_of_pages):  # All inherited except number_of_pages
        self.number_of_pages = number_of_pages
        super().__init__(title, author, publisher)
        Book.book_dict[self] = self.getInfo()
        Book.book_count += 1


class Video(Media):
    video_dict = {}  # Dictionary created to store all video instances associated with member name
    video_count = 0  # Counter for amount of videos

    def __init__(self, title, author, publisher, running_time):  # All inherited except running_time
        self.running_time = running_time
        super().__init__(title, author, publisher)
        Video.video_dict[self] = self.getInfo()
        Video.video_count += 1


class Member:  # Class will track all movement of media ie. checking in and out as well as whats been checked out by who
    checked_out_dict = {}  # Using dictionary to keep track of media name and member who checked it out by value/key
    checked_out_book_count = 0
    checked_out_video_count = 0
    member_count = 0

    def __init__(self, name):
        self.name = name
        self.check_out_list = []  # List will keep track of individual check outs
        Member.member_count += 1

    def checkIn(self, media_item):
        if media_item.__class__.__name__ == 'Book':  # Verifies the type of media by checking origin class name
            Member.checked_out_book_count -= 1
        else:
            Member.checked_out_video_count -= 1
        Member.checked_out_dict.pop(media_item)  # Removing checked in media from Member specific list
        print('\n{} checked in:{}'.format(self.name, media_item.getInfo()))

    def checkOut(self, media_item):
        if media_item in Member.checked_out_dict:  # Validation of whether media can be checked out or not
            print('\nSorry {},{} is not available, checked out by {}'.format
                  (self.name, media_item.getInfo(), Member.checked_out_dict[media_item]))
        else:
            if media_item.__class__.__name__ == 'Book':  # Verifies the type of media by checking origin class name
                Member.checked_out_book_count += 1
            else:
                Member.checked_out_video_count += 1
            if len(self.check_out_list) == 2:  # Checks if limit of checked out media is met by the member
                print(self.name, 'reached the maximum number (2)'
                                 ' of borrowed items, so can\'t check out:', media_item.getInfo())
            else:
                Member.checked_out_dict[media_item] = self.name
                self.check_out_list.append(media_item)
                print('\n{} has checked out:{}'.format(self.name, media_item.getInfo()))

    def printCheckedOutItems(self):  # Will print list of individual checked out items by checking dictionary
        print('\nItems checked out by {}:\n'.format(self.name))
        for item, person in Member.checked_out_dict.items():
            if person == self.name:  # Will print only the items checked out under members name by analyzing dictionary
                print(item.getInfo(), '\n')


def displayStats():
    print('\n\n\n******************************************\n\nRecord of Library:')

    information = (book1, video1, joe)  # List of instances from the test case
    for i in information:  # Allows the program to figure out what class for i to be based on.
        if i.__class__.__name__ == "Book":
            print('\nTotal number of books =', i.book_count)
            if i in Member.checked_out_dict:
                print("\nNumber of books checked out =", Member.checked_out_book_count)
        if i.__class__.__name__ == "Video":
            print("\nTotal number of videos =", i.video_count)
            # if i in Member.checked_out_dict:          # Wasn't in the test case but uncomment if needed
            #     print("\nNumber of videos checked out =", Member.checked_out_video_count)
        if i.__class__.__name__ == "Member":
            print("\nTotal number of members =", Member.member_count)
    print('\n\n\n**************************************************************************')

    print('\nThe following items are checked out of the library:\n')
    for value, key in Member.checked_out_dict.items():
        print(value.getInfo(), 'checked out by {}\n'.format(key))


# Test Case
if __name__ == "__main__":
    book1 = Book('Python for Beginners', 'Unknown', 'Unknown', 'Unknown')
    book2 = Book('Python for Kids', 'Jason R. Briggs', 'Unknown', 'Unknown')
    video1 = Video('Tom and Jerry', 'W. Hannah', 'J.Barbara', 30)
    joe = Member('Joe Smith')
    jim = Member('Jim Stuart')
    joe.checkOut(book1)
    joe.checkOut(book2)
    joe.printCheckedOutItems()
    joe.checkOut(video1)
    joe.checkIn(book1)
    jim.checkOut(book2)
    joe.checkIn(book2)
    jim.checkOut(video1)
    jim.checkOut(book1)
    displayStats()
