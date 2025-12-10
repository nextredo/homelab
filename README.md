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
- Customisable columns/lists
  - Can change what lists I have in a board
  - And more importantly, have more than 3 boards
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

#### Ideally it also has:
- Task dependencies??
  - This is potentially making the system too complex
  - Stuff like this might make it a pain in the ass
  - But would be cool I guess????
- Can move tasks between boards
- Recurring task functionality
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

#### Organisation
**THE SYSTEM EXISTS TO MANAGE TASKS**
**DO NOT GET CAUGHT UP MANAGING THE SYSTEM**
**IT SHOULD BE A TOOL, NOT A TASK**

##### Projects
- Top of the hierarchy
- Mutually exclusive - tasks in one at a time
- Not sure about this
- For work, it'd be different products
- But I only have 1 life, so that's 1 product/1 lifecycle
- Different people use user/account fields instead, not this
##### Boards
- Top of the hierarchy
- Mutually exclusive - tasks in one at a time
- **Based on categories/classifications that might require different lists within them**
  - e.g. habits requires
    - Backlog, habituating, habituated, discarded, completed
  - Regular tasks
    - Backlog/inbox/dump
    - To do (ready), doing (in progress), done (finished)
    - Ready, archived
    - Failed, expired
  - Shit to buy
    - To buy, not needed, en route/in progress, bought, used, get rid of (return/sell)
  - Groceries
    - To buy, not needed, en route/in progress, bought, used, get rid of (return/sell)
  - To consume?
    - Watchlist, to listen/podcast/music list, reading/book list
  - Stuff management
    - Take home, get from home
    - Sell, dispose, use
- A board per year?
- Board per area of interest?
##### Lists (✅ concept locked in)
- **The state of the task**
- Mutually exclusive - tasks in one at a time
- Unambiguous, we know what goes here
- States
  - To do/ready
  - Doing/in progress
  - Done/finished
  - Blocked, archived, failed, expired
  - Terminated, forwarded
  - Graveyarded? (that's just terminated ig)
##### Tags/labels (〰️ concept mostly locked in)
- Multiple, boolean - taks can have either have/not have any combo of these at once
- Not sure if you can have tags *and* labels
- Qualitites than can overlap on a given task
  - e.g.
  - The task "Complete the fan control knob project for Dad"
    - Get measurements from it
    - 3D model it
    - Print it
    - Check it's correct
    - Give it to Dad
  - This is in the categories of "Social" and "Engineering"
    - Requires me to do something in relation to someone else
    - Requires Engineering skills and/or helps improve them
  - Or reading something from the work reading list might be work + personal dev
  - Or meal prepping for someone is social + food
  - Or sw dev on an open src project is social + personal dev + engineering
  - Good for showing which tasks are twofers
- Areas of study/interest
  - Engineering, Language (German), Fitness, Personal Dev
  - Finance, Work-esque, Chores, SES/Volunteering, Food
  - Labour
  - Admin/Life Admin, Event/Someday??, CRM (Social)??
- Would sub areas help?
  - e.g. Engineering --> Software --> Self-Hosting
  - Fitness --> Cycling
- Or maybe attributes?
  - Long-term, short-term?
  - These are probably irrelevant, recurring/non-recurring tasks can handle that
##### Swimlanes
- Not sure what these would help with to be honest
- Seems to be used for people
- Could be a nice looking way to filter by tags I guess
- Due dates maybe? Priorities?
##### Tasks (✅ concept locked in)
- The unit of doingness
- The things to be done themselves
- e.g. setup a self-hosted kanban app
##### Subtasks (✅ concept locked in)
- Subunits of doingness
- Things within a task that need to be done
- e.g. read chapter 1, 2, 3, ... in task "read 20,000 Leagues Under the Seas"


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
