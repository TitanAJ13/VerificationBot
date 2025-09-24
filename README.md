# PMGC Tech Overhaul

## Glee Discord Bot (The Glot)

The Glot is a fully custom multi-purpose Discord Bot tailored for the Pitt Men's Glee Club official Discord server. It's current functionality is as follows:
* Automatically verifies new members using their Pitt emails and cross-referencing our Official Roster
* Generates image previews of any PDF files sent within the server
* A set of slash commands to make changes to the Glanvas
* A context-menu command to post announcements to the Glanvas
* Member management commands to help us update roles and access after each semester (in progress)
* Mass messaging capabilities to send custom messages populated with individual member information taken from the Official Roster (in progress)
* Integrate the Official PMGC Google Calendar into the Discord Events System (in progress)

## Glee Canvas (The Glanvas)

The Glanvas is a fully custom Flask application modeled off of Instructure's Canvas site and built for organization and easy access of Club documents and resources. I have no intention of commercializing this site or using it to replace Instructure's Canvas site on any scale, and I have no intention of breaking intellectual property law or copyright. The design of the Glanvas was based on a dark-mode, PMGC-themed Canvas page because the University of Pittsburgh uses Canvas to organize coursework and its interface is familiar to the student body. The underlying code is drastically different and I have not scraped the real Canvas in any way. Please let me know if I have infringed copyright (and in what ways) so that I may make the necessary changes.

The current functionality of the Glanvas is as follows:
* Organize files, links, and pages into collaspsible modules
* Display announcements pulled from the Official PMGC Discord Server with similar markdown rendering
* Show an embedded version of the Official PMGC Google Calendar
* Display embedded file previews for any file within the Official PMGC Google Drive
* Show embedded musescore files created by members of the PMGC to assist with learning songs
* Render custom markdown pages created by members of the PMGC (in progress)
* Run an API that The Glot uses to edit the structure of the site
    * Link addition, removal, editing, and moving
    * Module addition, removal, editing, moving, and hiding/showing
    * Module item addition, removal, editing, moving, and hiding/showing
    * File and Music registration, deregistration, and editing
        * Registered files and sheetmusic can have custom URL paths within the site
    * Register, deregister, edit, and hide/show custom site pages (in progress)
        * Registered pages have custom URL paths within the site
* Integrate with the Official PMGC Google Calendar to display upcoming events in the sidebar (in progress)
