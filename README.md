Gmail Chat Downloader
=============

Efficiently download chat conversation logs from Gmail using the Internet Message Access Protocol (IMAP) and convert raw (quoted-printable encoded) logs into HTML files viewable with any web browser.

Note that, as of Summer 2013, Gmail Chat Downloader no longer works with Gmail's current chat system.
Old chats can still be downloaded, however, which makes Gmail Chat Downloader an excellent archival tool.

Instructions
-------

You will need Python to use Gmail Chat Downloader. Python 2.7 is preferred.

`download.py` handles the IMAP download process while `convert.py` handles the conversion from raw chat logs to HTML files.

`example.py` contains an example of Gmail Chat Downloader in use. 

If you encounter an IMAP error, make sure IMAP is enabled for chats on Gmail. 
IMAP can be enabled in the Settings menu under Labels (check "Show in IMAP" next to "Chats").

License
-------

Gmail Chat Downloader is licensed under the [GNU GPLv3](http://www.gnu.org/licenses/gpl.html).
