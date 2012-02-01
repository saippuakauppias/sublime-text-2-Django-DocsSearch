#!/usr/bin/python

import sublime, sublime_plugin


class DjangoDocsSearchCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        for region in self.view.sel():
            word = self.view.word(region)
            if not word.empty():
                url = "http://readthedocs.org/docs/django/en/1.3/"\
                		"search.html?q=%s" % self.view.substr(word)
                sublime.active_window().run_command('open_url', {"url": url})