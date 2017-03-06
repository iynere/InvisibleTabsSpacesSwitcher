
# Sublime Text: Invisible Tabs Spaces Switcher

This plugin will convert spaces to tabs in a file as soon as you open it, then convert them back to spaces before you close it (or vice versa!).

Why did I make this? I hate working with spaces. The internet hates code files with tabs. Coders working on team projects often have different personal preferences. This lets you work the way you want to, without causing formatting issues online or making it harder to compare files when reviewing pull requests.

## Installation

Until it's in Package Control, you have to install it manually.

Clone the project into Sublime Text's Packages folder (or download it as a .zip, decompress it, and move it there yourself). On a Mac and with Sublime Text 3, this folder is in **~/Library/Application Support/Sublime Text 3**.

Invisible Tabs Spaces Switcher won't do anything unless you configure it.

## Configuration

Enable the plugin by adding the following lines to your Sublime Text user settings:

```
"invisible_tabs_spaces_switching": true,
"save_files_with_spaces": true,
"view_files_with_tabs": true
```

`"save_files_with_spaces"` and `"view_files_with_tabs"` configure how you'd like tab/space conversion to happen; default is working with tabs and saving with spaces. By toggling either or both of these options to `false`, you can work with spaces and save with spaces, work with spaces and save with tabs, or work with tabs and save with tabs.

To uninstall, remove the plugin folder from your Packages folder, or else use `Package Control: Remove Package`.

## Credits

Many thanks to [bubenkoff](https://github.com/bubenkoff)'s [Expand Tabs On Save](https://packagecontrol.io/packages/Expand Tabs on Save) plugin for inspiration.

## License

This software is licensed under the [MIT License](http://en.wikipedia.org/wiki/MIT_License).

*© 2017 r0se kaplan-bomberg*
