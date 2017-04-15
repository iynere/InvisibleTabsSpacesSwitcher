
# Sublime Text: Invisible Tabs Spaces Switcher

This plugin will convert spaces to tabs in a file as soon as you open it, then convert them back to spaces before you close it (or vice versa!).

Why did I make this? I don't like working with spaces, but many development projects (Package Control, for example) require them—and coders working on teams often have different personal preferences. This lets you work the way you want to, without causing formatting issues online or making it harder to compare files when reviewing pull requests (GitHub will flag identical files for comparision if one has tabs and one has spaces).

## Installation

Until it's in Package Control, you have to install it manually.

Download the project, expand the .zip, and put the folder in Sublime Text's Packages folder. On a Mac and with Sublime Text 3, this folder is in **~/Library/Application Support/Sublime Text 3**.

## Configuration

The plugin is enabled with the following default settings.

```
// if false, will disable the plugin
"invisible_tabs_spaces_switcher": true,

// if false, files will be saved with tabs
"save_files_with_spaces": true,

// if false, files will be loaded with spaces
"view_files_with_tabs": true
```

Add your own settings to Settings – User (in **Preferences -> Package Settings -> InvisibleTabsSpacesSwitcher**)

To uninstall, remove the plugin folder from your Packages folder, or else use `Package Control: Remove Package`.

## Credits

Thanks to [bubenkoff](https://github.com/bubenkoff)'s [Expand Tabs On Save](https://packagecontrol.io/packages/Expand%20Tabs%20on%20Save) plugin for inspiration.

## License

This software is licensed under the [MIT License](http://en.wikipedia.org/wiki/MIT_License).

*© 2017 [r0se kaplan-bomberg](http://r0se.codes)*
