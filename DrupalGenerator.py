import sublime, sublime_plugin

# To Run view.run_command('drupal_generator')
class DrupalGeneratorCommand(sublime_plugin.TextCommand):
  def run(self, edit, dirs):
    self.view.window().show_input_panel('Module Name:', '', None, None, None)

#Command to Generate Module
class DrupalGeneratorModuleCommand(sublime_plugin.WindowCommand):
  def run(self, dirs):
    self.window.show_input_panel('Module Name:', dirs[0], None, None, None)

#Command to Generate Theme
class DrupalGeneratorThemeCommand(sublime_plugin.WindowCommand):
  def run(self, dirs):
    self.window.show_input_panel('Theme Name:', '', None, None, None)
