# -*- coding: utf-8 -*-

from EvernoteController.controller import EvernoteController
import evernote.edam.notestore.NoteStore as NoteStore
import collections


def find_duplicate(ec):
    # 先从线上获取所有的笔记标题， 放到内存里
    # e.storage.retrieve_all_notes(dev_token, e.noteStore)   (这个太耗资源了,会产生无数个请求, 不用这个)

    results = ec.noteStore.findNotesMetadata(
        NoteStore.NoteFilter(),
        None,
        2000,
        NoteStore.NotesMetadataResultSpec(
            includeTitle=True, includeNotebookGuid=True)
    )
    all_titles = [note.title.decode("utf-8") for note in results.notes]

    dup_list = [item for item, count in collections.Counter(all_titles).items() if count > 1]

    for t in dup_list:
        print t


if __name__ == '__main__':
    dev_token = "S=s1:U=92e22:E=15e5ac1167d:C=157030fe988:P=1cd:A=en-devtoken:V=2:H=1ef28ef900ebae2ba1d1385bffbb6635"
    ec = EvernoteController(dev_token, True, True)
    find_duplicate(ec)

    # API演示
    # e.create_note('Test/中文', 'Chinese')
    # e.create_notebook('Notebook1')
    # e.create_note('Hello', '<en-note>Hello, world!</en-note>', 'Notebook1')
    # e.show_notebook()
    # e.show_notes()
    # e.get("示例笔记本")
    # e.get("示例笔记本/记录灵感")

