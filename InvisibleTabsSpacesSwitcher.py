"""Invisible Tabs Spaces Switcher SublimeText plugin"""

import sublime, sublime_plugin # modules provided by SublimeText
import os # Python module for interacting with your computer's operating system

class InvisibleTabsSpacesSwitcher(sublime_plugin.EventListener):
  def on_load(self, view): # event triggered when file is loaded
    if view.settings().get('invisible_tabs_spaces_switching') == 1:
      if view.settings().get('view_files_with_tabs') == 1:
        view.run_command('unexpand_tabs')
      else: # aka, we want to view files with spaces
        view.run_command('expand_tabs')
        
  def on_pre_save(self, view): # event triggered BEFORE file saves
    if view.settings().get('invisible_tabs_spaces_switching') == 1:
      if view.settings().get('view_files_with_tabs') == 1:
        view.run_command('expand_tabs')
      else: # aka, we want to view files with spaces
        view.run_command('unexpand_tabs')
  
  def on_post_save(self, view): # event triggered AFTER file saves
    if view.settings().get('invisible_tabs_spaces_switching') == 1:
      if view.settings().get('view_files_with_tabs') == 1:
        view.run_command('unexpand_tabs')
      else: # aka, we want to view files with spaces
        view.run_command('expand_tabs')