import sublime, sublime_plugin

#To Run view.run_command('drupal_generator')

class DrupalGeneratorCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.window().show_input_panel('Somthing', 'Default Value', None, None, None)
