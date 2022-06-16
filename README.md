# BIP-Tool
My early attempts at a simple project management/business operations/bookkeeping web tool.

I want to make a change and see if it gets uploaded to github

2022-06-13
So this is my running server. Making any changes terrifies me. Still, I've done it before. Let's give it a go again.

Goals:
The main thing is that I need to change some value from 1000 to none. Specifically, DATA_UPLOAD_MAX_NUMBER_FIELDS.
Based on how that's written, I'd say that has to do with the database, which adds a level of pita to it.

While I have this all pulled to work on, I would also like to take care of a few small convenience things I've been salivating for. Get rid of all opening/closing columns. I don't use them and they're all stupid.

I'd also like to make everything sortable by basically everything. Specifically, I want to sort tasks by date. That would help a great deal, especially if it can happen within the task view.

Well, let's start by pulling these changes to readme

First, my local test database had 'complete' columns in projects and tasks, my migration failed. I deleted them manually from the database and reran migrate, which then worked. This shouldn't interfere with production as I didn't change anything that production sees. I only altered the local db, and migrate doesn't change the django code, I think...

Next, changed the model to remove opening and closing from tasks and reports. I made migrations, and then I migrated. I checked the local database and it reflected those changes.

I added the following line to settings.py: DATA_UPLOAD_MAX_NUMBER_FIELDS = None
As I understand, this opens the possibility of dos attacks, or rather disables one protection against them. Seeing as my defenses are fuck all at the moment, we'll just put a pin in that one.

So fun news, somehow production didn't match github. So I have to learn how to rollback (is that the right word) my local dev version, push production to git, and then pull git to dev. AAAAHAHHAHAHHAHHHHHH!!!!! Have I mentioned I'm not good at git.

I want this record, so I will back it up and then attempt to preserve it correctly.

2022-06-15
Okay, so a bunch of mess trying to get things lined up. I'm not sure what all happened, but I think a big part of it was that I was on master instead of main, and I don't know what the difference is or why that mattered.

Reimplemented the changes I lost in that mess.

I haven't figured out how to make inlines sortable by user choice of columns, but I made inline reports and tasks to default sort by date, so better than nothing. Now we save, make migrations, migrate, and see if we can make this shit work. 
