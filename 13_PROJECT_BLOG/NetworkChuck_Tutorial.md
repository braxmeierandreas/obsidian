# My Insane Blog Pipeline (NetworkChuck)
2024-11-15
#networkchuck #blog

## Obsidian - Why I love it
Obsidian is the BEST notes application in the world. Go download it: https://obsidian.md/

## The Setup
Create a new folder labeled posts. This is where you will add your blog posts
….that’s all you have to do
Actually…wait….find out where your Obsidian directories are. Right click your posts folder and choose show in system explorer
You’ll need this directory in upcoming steps.

## Setting up Hugo
### Install Hugo
#### Prerequisites
* Install Git: https://github.com/git-guides/install-git
* Install Go: https://go.dev/dl/
* Install Hugo: https://gohugo.io/installation/

### Create a new site
#### Verify Hugo works
`hugo version`

#### Create a new site
`hugo new site websitename`
`cd websitename`

### Download a Hugo Theme
Find themes from this link: https://themes.gohugo.io/
follow the theme instructions on how to download. The BEST option is to install as a git submodule

#### Initialize a git repository
`git init`

#### Set global username and email parameters for git
`git config --global user.name "Your Name"`
`git config --global user.email "your.email@example.com"`

#### Install a theme (Terminal theme)
`git submodule add -f https://github.com/panr/hugo-theme-terminal.git themes/terminal`

### Adjust Hugo settings
Edit the `hugo.toml` file:
```toml
baseurl = "/"
languageCode = "en-us"
theme = "terminal"
paginate = 5

[params]
  contentTypeName = "posts"
  showMenuItems = 2
  showLanguageSelector = false
  fullWidthTheme = false
  centerTheme = false
  autoCover = true
  showLastUpdated = false

[languages]
  [languages.en]
    languageName = "English"
    title = "Terminal"
    [languages.en.params]
      subtitle = "A simple, retro theme for Hugo"
      menuMore = "Show more"
      readMore = "Read more"
      readOtherPosts = "Read other posts"
      newerPosts = "Newer posts"
      olderPosts = "Older posts"
      missingContentMessage = "Page not found..."
      missingBackButtonLabel = "Back to home page"
      minuteReadingTime = "min read"
      words = "words"
      [languages.en.params.logo]
        logoText = "Terminal"
        logoHomeLink = "/"
      [languages.en.menu]
        [[languages.en.menu.main]]
          identifier = "about"
          name = "About"
          url = "/about"
        [[languages.en.menu.main]]
          identifier = "showcase"
          name = "Showcase"
          url = "/showcase"
```

### Test Hugo
`hugo server -t terminal`

## Syncing Obsidian to Hugo
### Windows
`robocopy sourcepath destination path /mir`

### Frontmatter Template
```markdown
---
title: blogtitle
date: 2024-11-06
draft: false
tags:
  - tag1
  - tag2
---
```

## Transfer Images (Python Script)
```python
import os
import re
import shutil

# Paths
posts_dir = r"C:\Users\chuck\Documents\chuckblog\content\posts"
attachments_dir = r"C:\Users\chuck\Documents\my_second_brain\neotokos\Attachments"
static_images_dir = r"C:\Users\chuck\Documents\chuckblog\static\images"

# Process each markdown file
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        images = re.findall(r'[[^]]*\.png]]', content)
        for image in images:
            markdown_image = f"![Image Description](/images/{image.replace(' ', '%20')})"
            content = content.replace(f"[[{image}]]", markdown_image)
            image_source = os.path.join(attachments_dir, image)
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)
```
