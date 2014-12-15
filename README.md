# VendaSublimeText

Sublime Package and recommended settings for Venda Template Development. Includes Venda Tag autocompletion and snippets.

## First Time Setup
If you're installing Sublime fresh, or don't mind overwriting your current settings, you can do a `git clone` of the settings:
1. In your terminal, `cd` to your `Sublime Text 3` folder, e.g., `cd /Users/sgoldberg/Library/Application Support/Sublime Text 3`
2. Delete your default `Packages` folder: `rm -rf Packages`
3. Clone down making sure to change the name of the folder (repo). As you're testing my work, you'll need to clone from my fork: `git clone https://github.com/venda/VendaSublimeText.git Packages`. This will create a folder called `Packages` with the contents in it and set it up as a Git repo.
4. Restart Sublime. All of the user packages should have loaded fine.
5. Test: create a blank HTML file and save it. After it's saved, test all the cool things that these preferences do: e.g., typing `html` and then tabbing, or the Venda tag autocomplete.

## Packages > Venda
 * Tag autocompletion
 * Snippets for venda_block and venda_tpcomment

### How to install
 * Preferences > Browse Packages
 * Copy the whole Venda directory into your Packages Directory
 * Restart Sublime

## Packages > User > Preferences.Example.sublime-settings
 * These are Venda's recommended settings

### How to install

** Warning - copying the contents of this file will overwrite your current settings. **

 * Preferences > Settings - User
 * Cut and paste the settings from Preferences.Example.sublime-settings to add them to your personal preferences.
 * If any of the fields are used already in your personal preferences, remove the existing fields.

## Packages > User > DataRec.sublime-settings
 * These are settings for Venda data.rec files
 * data.rec files are tab-delimited and hence need to have translate_tabs_to_spaces set to false.

### How to install
 * Preferences > Browse Packages:
 * Copy the DataRec.sublime-settings into your Packages/User Directory
 * Restart Sublime

## Packages > User > JavaScript.sublime-settings
 * Recommended tabbing for JavaScript files
 * Ensures tabbing matches github.com/venda/VendaTemplates

### How to install
 * Preferences > Browse Packages:
 * Copy the JavaScript.sublime-settings into your Packages/User Directory
 * Restart Sublime

## Packages > User > JSON.sublime-settings
 * Recommended tabbing for JSON files
 * Not currently needed for Venda sites

## Packages > User > Ruby.sublime-settings
 * These are settings for Venda Ruby files
 * Not currently needed for Venda sites
