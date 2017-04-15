"""Invisible Tabs/Spaces Switcher Sublime Text plugin"""

import sublime, sublime_plugin # modules provided by Sublime Text
import webbrowser # for support

# hook for opening files when ST is closed (b/c files load before plugins)
def plugin_loaded():
  if sublime.load_settings('InvisibleTabsSpacesSwitcher.sublime-settings').get('invisible_tabs_spaces_switcher') == True:
    for view in sublime.active_window().views(): # loop through opened files
      format_for_load(view)
    
# loading & closing methods for the plugin to use
def format_for_load(view):
  if view.file_name(): # ignore untitled default/background files
    if not view.file_name().endswith('.sublime-settings') and not view.file_name().endswith('.sublime-keymap'): # ignore preferences and key-bindings files
      if sublime.load_settings('InvisibleTabsSpacesSwitcher.sublime-settings').get('view_files_with_tabs') == True:
        view.run_command('unexpand_tabs') # convert to tabs
      else: # aka, we want to view files with spaces
        view.run_command('expand_tabs') # convert to spaces
      view.run_command('save')
  
def format_for_close(view):
  if view.file_name():
    if not view.file_name().endswith('.sublime-settings') and not view.file_name().endswith('.sublime-keymap'):
      if sublime.load_settings('InvisibleTabsSpacesSwitcher.sublime-settings').get('view_files_with_tabs') == True:
        view.run_command('expand_tabs')
      else: # aka, we want to save files with tabs
        view.run_command('unexpand_tabs')
      view.run_command('save')

# the plugin itself
class InvisibleTabsSpacesSwitcher(sublime_plugin.EventListener):
  def on_load(self, view): # event triggered when file is loaded
    if sublime.load_settings('InvisibleTabsSpacesSwitcher.sublime-settings').get('invisible_tabs_spaces_switcher') == True:
      format_for_load(view)

  def on_pre_close(self, view): # event triggered before file closes
    if sublime.load_settings('InvisibleTabsSpacesSwitcher.sublime-settings').get('invisible_tabs_spaces_switcher') == True:
      format_for_close(view)
      
# support
class InvisibleTabsSpacesSwitcherOpenSiteCommand(sublime_plugin.ApplicationCommand):
    def run(self, url):
      webbrowser.open_new_tab(url)
