# Task Management
## Concepts / Words
### Components
- Boards, lists, cards
- Swimlanes

## Options (under review)
- Largely from [awesome-selfhosted](aw-sh-t-mgmt)

### Commercial options
- Not picking any of these
- Just good references
- Trello, Notion, Jira, Asana
- TickTick

### Ruled out FOSS options
- TaskBoard
  - Too basic, unmaintained
- Taiga
  - Don't need a full project management tool
- AppFlowy
  - Lot of stars, written in dart + Rust
  - Not as open source as I'd like (open core)
- OpenProject
  - Don't need a full project management tool
- Plane.so
  - Don't need a full project management tool
- Leantime
  - Don't need a full project management tool
- Tracks
  - Seems old, not super maintained
- Donetick
  - Not a Kanban
  - Pricing mentions are weird
- Vikunja
  - Being slowly enshittified
- Brisqi
  - Pricing cringe
- TaskCafe
  - Unmaintained but looks good
  - Still in Alpha
- Nimbo
  - Small, unmaintained
- Taskosaur
  - *Very* AI driven, seems to push pricing
- WeKan
  - UI isn't great
- Trilium
  - Not primarily a Kanban app
  - Could be good for docs though
- Gitea Boards
  - I don't need a whole git server just to have a kanban
  - Though if I need a git server anyway...

### Tempting FOSS options
#### KanBoard
##### Notes
- App in "Maintenance mode"
- Documentation isn't super well organised imho
- Stable, works fine as far as I can see
- Seems much more project management esque than I assumed it would be
- UI is highly utilitarian
  - Difficult to use in mobile mode
- Has extensions to beautify it
  - [Greenwing](https://github.com/p0lym0rphik/Greenwing)

##### Issues
- Time didn't seem to work fully properly
  - I think it needs to use my local time not UTC
- Setting things red when over task limits doesn't work all the time :(
- Interface is a little rough on mobile

##### Features
- `iCal` feed is a cool idea
  - Enables things to appear in Google Calendar I guess
- Task limits
- Swimlanes
- Plugin support
- Categories (1 per task)
- Tags (many per task)
- Timers on subtasks

##### Decision
- Nah, not for me
- Shoutout to the devs tho

### Very tempting FOSS options
#### Nextcloud Deck
##### Notes
- Nextcloud is a pain to setup ngl
- Clean UI tho
- Huge userbase, number of stars
- Works fine on mobile
- Different workflow from what I'm used to
  - Tasks in different columns (lists)
  - Move taks around
  - Separate button to mark as done
  - Then archive xd
  - Thoughts
    - I kinda like it though
    - But makes "equivalent done" statuses like expired, failed harder to show
      - Just tag it ig

##### Issues
- If I'm going to use nextcloud;
  - Optimise the hell out of it
  - Make backups of relevant stuff (db, files)
  - Update things
    - Dockerfile & docker compose
      - Clean, refactor
      - Get new features
    - Nextcloud (running Hub 9 v30, latest is Hub 10, v32)
    - MariaDB
    - Nginx
  - Update my cert
- Doesn't auto update between multiple browers with the same page open

##### Features
- Nextcloud kinda does everything
  - Can be the photos backup, doc storage, and tasks app
- Integrations
  - Notes app
  - Tasks app
- Mobile app
- Card archiving
- Added recently
  - Cloning cards
  - Cloning boards
  - Link previs for cards
  - Card cover images

##### Missing Features
- No export functionality
- Can't limit number of tasks in progress
- No priority field
- No emoji icon / picture cover

#### Planka
##### Notes
- UI
  - Snappy, fast as hell
  - Works great on mobile

##### Issues
- UI loading takes forever to load when you first load the webpage
  - Loads very *slowly* when opening in Firefox
  - Loads very *quickly* when opening in Chrome
- Filtering is lackluster in main board screens
  - Only for labels, users
- Can't add new boards to projects occasionally
  - Make a project
  - Add a board to it
  - Can add multiple boards no worries
  - Close the tab or go back to the projects screen
  - Open the project again
  - Can't add a new board anymore
- Not Copyleft licensed

##### Features
- Trello import
- Actively maintained
- Simple, appears robust
- Great UI/UX
- "Can't connect to server" message when it goes offline
  - Autosync afterwards too supposedly
- Pictures as cover art for tasks
- Dedicated archive section for tasks is cool

##### Missing Features
- No export functionality
- Can't limit number of tasks in progress

#### FocalBoard
##### Notes
- Very Notion-looking
- UI clean, good

##### Issues
- If I'm to actually use it
  - Setup a NGINX to make it HTTPS
  - Setup a proper docker compose
    - So it doesn't delete all data on `docker compose down`
- **Unmaintained :(**
  - Developed by Mattermost
  - They pivoted to focusing on it as a plugin for their Slack clone
- "Mobile web support is currently in early beta"
  - Placement is a little messed up on mobile to be fair
- Due dates don't show up properly in the list (status) metric section

##### Features
- Discord syntax for writing emojis `:see-no-evil:`
- I like task emoji icons
- Both instances of it (open at the same time) kept in sync
- Has board exports :)
  - But in a weird format
  - Strange JSON that's not real valid normal JSON
- Metric to display at the top of each list
- Board templates

##### Missing Features
- Can't view uploaded pics on the site itself
- Can't limit number of tasks in progress

--------------------------------------------------------------------------------
### Chosen FOSS option
- Cooked on this for days man 🔥
- ***Nextcloud Deck***
- Integrates with all the other services I need
- Seems to be pretty dang good
- Maintained etc.

<!-- Links -->
[aw-sh-t-mgmt]: https://awesome-selfhosted.net/tags/task-management--to-do-lists.html
