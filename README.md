# Homelab
Collection of services for my homelab

## Other Information
- Workshop repo
- Profile README
- GitHub.io site

## Services
--------------------------------------------------------------------------------
### Photos
#### Options
##### Immich

--------------------------------------------------------------------------------
### Task Management
#### Options (under review)
- [awesome-selfhosted task management](https://awesome-selfhosted.net/tags/task-management--to-do-lists.html)

##### Concepts / Words
- Boards, lists, cards
- Trello, Notion, Jira, Asana

##### Ruled out
- TaskBoard
  - Too basic
  - Unmaintained
- Notion
  - Not FOSS, not self-hostable
- Taiga
  - Full project management/Jira thing seems like overkill
  - [taiga](https://taiga.io/)
  - [kanban](https://community.taiga.io/t/the-5-min-kanban-module-overview/122)
  - Bit heavy (too project management-y) for personal life
- AppFlowy
  - Has a lotta stars on GitHub (>67k)
  - Markets itself as "The Open Source Alternative To Notion"
  - Written in Dart and Rust
  - AI stuff
    - I hope you can disable it / self host a model instead
  - Has mobile app
  - Is becoming "open core" instead of "open source"
  - Has some proper anti-features innit
- OpenProject
  - Probably a bit heavy innit
- Plane.so
  - Pricing stuff makes me worried smhh
- Leantime
  - Not even looking into this bro
  - Project management shii
- Tracks
  - GPLv2
  - Implements the "Getting Things Done" methodology from some guy called David Allen
  - UI pretty dated
  - Less contributors, seems to not get as much love as other projects
- Donetick
  - More of a fledgling thing
  - Mentions pricing and stuff on the subreddit, but no reference to it on the website
  - Doesn't seem kanban-esque, more like a juiced up Microsoft To Do
- Vikunja
  - Bad, user account creation paid
- Brisqi
  - Pricing cringe
- TaskCafe
  - Unmaintained, looks good
- Nimbo
  - Small as hell (64 stars), unmaintained
- Taskosaur
  - 151 stars
  - *Very* AI driven
- TickTick
  - Not open source

##### Other
- Nextcloud (deck extension)
  - This was a pain to setup
  - Seems fragile and annoying? Maybe I'm just a hater
  - Could be worth retrying using another config or smth
  - Seems pretty dang basic
- Trilium
  - No mention of pricing or payment anywhere
  - AGPLv3
  - [What it can do](https://docs.triliumnotes.org/user-guide/)
  - [It has kanbans](https://docs.triliumnotes.org/user-guide/collections/kanban-board)
- Planka
  - UI is snappy as hell, visually appealing
    - This was based on V1 - it's at V2 now
  - Not overly complex
  - German
  - Has its own license ffs
    - Which mentions pro/enterprise bs
- WeKan
  - Saving the best(?) until last(?)
  - Dunno about this one
- FocalBoard
  - GitHub page says it's unmaintained
  - But it looks kinda nice
  - I think it's been made part of "mattermost" - a SW development toolkit thang (looks exactly like Slack)
  - Needs a HTTPS:// wrapper
  - Not sure how the other apps do https without an IP, could be useful to steal and apply to my next cloud
- KanBoard
  - Has docker despite what awesome-selfhosted says
  - Simplistic, probably means no bs, stable
  - Application has reached "maintenance mode"
  - May be a little toooo simplistic
  - Can use extensions like Greenwing to make it pretty

#### Requirements
- Is FLOSS
- Is maintained or feature-complete, stable, maintenance mode (like Kanboard)
- Is relatively simple, robust
- Has a lot of stars on GitHub
  - Makes it less likely to be suddenly unmaintained
  - And will have bugfixes / more support info and better docs/code really
- Limiting tasks in progress
  - So I don't get sidetracked doing 50 things at once
- Kanban style
  - This style really appeals to me
  - Simplistic, functional, good
- >3 columns/lists
  - To do (ready), doing (in progress), done (finished)
  - Ready, archived
  - Failed, expired
  - Other labels from [here](https://en.wikipedia.org/wiki/Task_management#/media/File:TaskLifeCycle.png)
  - e.g. for things like "consistently recurring tasks" (brushing teeth as an example)
- Tags & filtering
  - Input (to consume, like a book, movie, podcast)
    - Reading, watching, learning
  - Output (to produce, like write some code or fix something)
    - Physical, digital
  - Systematic
    - Habits, hobbies
- Projects & sub-projects
  - To represent different areas of my life
  - Computer shit (software, linux, projects)
  - Self-improvement stuff (podcasts, habits)
  - German
  - Gym

#### Organisation
- Projects
  - Top of the hierarchy
- Boards
  - Top of the hierarchy
- Lists
  - Unambiguous, we know what goes here
  - It's the state of the task
  - To do/ready
  - Doing/in progress
  - Done/finished
  - Blocked, archived, failed, expired
  - Terminated, forwarded
  - Graveyarded? (that's just terminated ig)
- Tags/labels
  - Top of the hierarchy

#### Ideally it also has:
- An open file type that can be ported to other platforms later if need be
  - Markdown good
- Is written in a language(s) I'd be interested in learning or have a good opinion of
  - e.g. rust, go, dart
- Is GPL / CopyLeft licensed
  - Makes it harder to be rugpulled into a proprietary / paid solution
- A mobile app
  - But a functional mobile web interface is ok too
- Tags?
- Date logging of stuff
- Tie-in with my notes app somehow?
  - This seems like a FocalBoard/Docmost type thing

--------------------------------------------------------------------------------
### Note-taking
- [awesome-selfhosted wikis](https://awesome-selfhosted.net/tags/wikis.html)

#### Concepts / Words
- Notion, Confluence
- Personal Wiki, PKM

#### Usage Notes
- Stuff I wanna show people publicly can go in my github.io static site
- Stuff I don't goes in here somewhere

#### Options
##### Docmost
- Notion type thing
- Apparently doesn't do kanbans or task management at all

##### Memos
- Like Google Keep

### LLMs

--------------------------------------------------------------------------------
### Volunteer Computing
#### BOINC
