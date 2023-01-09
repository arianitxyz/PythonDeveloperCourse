import webbrowser

#
# webbrowser.open("https://python.org")
#
# help(webbrowser)

# for i in range(10):
#     print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='; ', end=' ')

chrome = webbrowser.get(using='"C:\Program Files\Google\Chrome\Application\chrome.exe" %s').open("http://google.com")
edge = webbrowser.get(using='"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" %s').open("http://google.com")
