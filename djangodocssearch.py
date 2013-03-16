#!/usr/bin/python

import sublime, sublime_plugin


class DjangoDocsSearchCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        settings = sublime.load_settings('DjangoDocsSearch.sublime-settings')
        version = settings.get('version')
        for region in self.view.sel():
            word = self.view.word(region)
            if not word.empty():
                url = "http://readthedocs.org/docs/django/en/%s/"\
                		"search.html?q=%s" % (version,self.view.substr(word))
                sublime.active_window().run_command('open_url', {"url": url})
