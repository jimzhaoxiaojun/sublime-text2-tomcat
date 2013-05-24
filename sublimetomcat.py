# -*- coding: UTF-8 -*-
import sublime, sublime_plugin, os, shutil

class SaveEvent(sublime_plugin.EventListener):
    def on_post_save(self, view):
        curfile = view.file_name()       

        ehrParam = self.load_ehr_param()
        ehrDir = ehrParam["ehr_dir"];
        tomcatDir = ehrParam["tomcat_dir"]
        print ehrParam
        #jsp文件直接拷到tomcat相应目录下
        isEhrJsp = curfile.startswith(ehrDir + "\\hrms")
        if isEhrJsp:
            tomcatEhrJsp = curfile.upper().replace(ehrDir, tomcatDir + "\\webapps")
            shutil.copyfile(curfile, tomcatEhrJsp)
            return

        #java文件需要先编译成class，然后拷贝到tomcat相应目录下
        isEhrJava = curfile.startswith(ehrDir + "\\src")


        print os.path.splitext(curfile)

    def load_ehr_param(self):
        s = sublime.load_settings("eventtest.sublime-settings")
        return {"ehr_dir": s.get("ehr_dir"), "tomcat_dir": s.get("tomcat_dir")}
