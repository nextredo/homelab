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
- Nextcloud Deck
  - Nextcloud is a pain to setup ngl
- WeKan
  - UI isn't great
- Trilium
  - Not primarily a Kanban app
  - Could be good for docs though

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

##### Missing Features
- No export functionality
- Can't limit number of tasks in progress

##### Decision
- Let me cook on this 🔥

#### FocalBoard
##### Notes
-

##### Issues
-

##### Features
-


### Chosen FOSS option
-


<!-- Links -->
[aw-sh-t-mgmt]: https://awesome-selfhosted.net/tags/task-management--to-do-lists.html
