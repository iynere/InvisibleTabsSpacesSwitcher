"""Invisible Tabs Spaces Switcher Sublime Text plugin"""

import sublime, sublime_plugin # modules provided by Sublime Text

class InvisibleTabsSpacesSwitcher(sublime_plugin.EventListener):
  def on_load(self, view): # event triggered when file is loaded
    if view.settings().get('invisible_tabs_spaces_switching') == True:
      if view.settings().get('view_files_with_tabs') == True:
        view.run_command('unexpand_tabs')
      else: # aka, we want to view files with spaces
        view.run_command('expand_tabs')

  def on_pre_close(self, view): # event triggered before file closes
    if view.settings().get('invisible_tabs_spaces_switching') == True:
      if view.file_name(): # avoid untitled dummy/background files
        if view.settings().get('view_files_with_tabs') == True:
          view.run_command('expand_tabs')
        else: # aka, we want to save files with tabs
          view.run_command('unexpand_tabs')
        view.run_command('save')
