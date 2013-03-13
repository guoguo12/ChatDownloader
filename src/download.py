import convert
import imaplib
import sys

def download(username, password, range = []):
    imap = imaplib.IMAP4_SSL('imap.gmail.com')
    imap.login(username, password)

    if imap.select('[Gmail]/Chats', True)[0] != 'OK':
        print "IMAP access error. Please check IMAP is enabled for chats."
        closeExit(imap)

    status, data = imap.search(None, 'ALL')
    if status != 'OK':
        print "IMAP search error."
        closeExit(imap)
    chats = data[0].split()

    if range == []:
        range = chats
    chatsToDownload = str(len(range))

    print str(len(chats)) + " chats found."
    filelist = []
    for num in range:
        filename = "chat " + str(num) + ".txt"
        print "Downloading chat #" + str(num) + " of " + chatsToDownload + "."
        status, data = imap.fetch(num, '(RFC822)')
        if status == 'OK':
            filelist.append(filename)
            toFile(filename, data[0][1])
        else:
            print "Unable to download chat #" + str(num) + "."

    imap.close()
    imap.logout()
    return filelist

def toFile(filename, data):
    file = open(filename, 'w')
    file.write(data)
    file.close()

def closeExit(imap):
    imap.close()
    imap.logout()
    sys.exit()

def main():
    args = sys.argv
    if len(args) != 3:
        username = raw_input("Username: ")
        password = raw_input("Password: ")
    else:
        username = args[1]
        password = args[2]

    download(username, password)

if __name__ == '__main__':
    main()