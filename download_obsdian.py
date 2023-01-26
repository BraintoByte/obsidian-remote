import os

urls = os.popen('curl -s https://api.github.com/repos/obsidianmd/obsidian-releases/releases/latest | grep \"browser_download_url.*AppImage\" | cut -d \'\"\' -f 4').read().split('\n')
download_url = ''

for url in urls:
    if 'arm64' not in url:
        download_url += url

os.system('curl ' + download_url + '' + ' -L -o obsidian.AppImage')