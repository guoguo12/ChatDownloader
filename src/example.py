import convert
import download

def main():
    """
    Downloads all chats for the account Username@Gmail.com
    and outputs them in a single HTML file ("chats.html").
    """

    filelist = download.download('Username', 'Password') # 'filelist' lists downloaded files
    convert.convertFilelist(filelist, False, 'chats.html')

if __name__ == '__main__':
    main()