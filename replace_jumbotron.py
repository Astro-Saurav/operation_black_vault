import os

templates_dir = '/home/astro/Documents/modules/ctf/CTFd/CTFd/themes/core/templates'

for root, dirs, files in os.walk(templates_dir):
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r') as f:
                content = f.read()
            
            original_content = content
            content = content.replace('<div class="jumbotron">', '<div class="cyber-page-header jumbotron">')
            content = content.replace('\t<div class="jumbotron">', '\t<div class="cyber-page-header jumbotron">')
            content = content.replace('<h1>', '<h1 class="cyber-title">')
            content = content.replace('<h1>\n', '<h1 class="cyber-title">\n')
            
            if content != original_content:
                with open(path, 'w') as f:
                    f.write(content)
                print(f"Updated {path}")
