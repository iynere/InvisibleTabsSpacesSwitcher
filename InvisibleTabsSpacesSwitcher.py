"""Invisible Tabs/Spaces Switcher Sublime Text plugin"""

import sublime, sublime_plugin # modules provided by Sublime Text

# hook for opening files when ST is closed (b/c files load before plugins)
def plugin_loaded():
  if sublime.load_settings('Preferences.sublime-settings').get('invisible_tabs_spaces_switching') == True:
    for view in sublime.active_window().views(): # loop through opened files
      load_file(view)

# loading & closing methods for the plugin to use
def load_file(view):
  if view.file_name(): # ignore untitled default/background files
    if not view.file_name().endswith('.sublime-settings') and not view.file_name().endswith('.sublime-keymap'): # ignore preferences and key-bindings files
      if view.settings().get('view_files_with_tabs') == True:
        view.run_command('unexpand_tabs') # convert to tabs
      else: # aka, we want to view files with spaces
        view.run_command('expand_tabs') # convert to spaces
      view.run_command('save')
  
def close_file(view):
  if view.file_name():
    if not view.file_name().endswith('.sublime-settings') and not view.file_name().endswith('.sublime-keymap'):
      if view.settings().get('view_files_with_tabs') == True:
        view.run_command('expand_tabs')
      else: # aka, we want to save files with tabs
        view.run_command('unexpand_tabs')
      view.run_command('save')

# the plugin itself
class InvisibleTabsSpacesSwitcherCommand(sublime_plugin.EventListener):
  def on_load(self, view): # event triggered when file is loaded
    if view.settings().get('invisible_tabs_spaces_switching') == True:
      load_file(view)

  def on_pre_close(self, view): # event triggered before file closes
    if view.settings().get('invisible_tabs_spaces_switching') == True:
      close_file(view)


