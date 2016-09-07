# -*- coding:utf-8 -*-

"""
这是用来快速上手Evernote API的测试代码
注意：由于Evernote官方Py库使用的是py2, 其py3分支很久没有更新了，因此这里统一使用py2

个人感觉最好的学习资源，就是sublime-evernote插件
https://github.com/bordaigorl/sublime-evernote/blob/master/sublime_evernote.py
因为那是一个全功能的插件（包括增删改查）

另外一个比较好的资源，是evernote官方代码里的样例
https://github.com/evernote/evernote-sdk-python/blob/master/sample/client/EDAMTest.py

还有一个是国内网友写的几个工具
https://github.com/littlecodersh/EasierLife

Evernote API使用的thrift框架，所有语言的API都是同样的接口定义
"""


from evernote.api.client import EvernoteClient
from evernote.edam import type
import evernote.edam.type.ttypes as Types
import evernote.edam.notestore.NoteStore as NoteStore

# 这个是用来测试的沙盒Token，需要自己去申请
#  https://sandbox.evernote.com/api/DeveloperToken.action
dev_token = "S=s1:U=92e22:E=15e5ac1167d:C=157030fe988:P=1cd:A=en-devtoken:V=2:H=1ef28ef900ebae2ba1d1385bffbb6635"
client = EvernoteClient(token=dev_token)

userStore = client.get_user_store()
print userStore.token

user = userStore.getUser()


# 这个note_store是最重要的数据API
note_store = client.get_note_store()

for nb in note_store.listNotebooks():
    print n.name

n = type.ttypes.Note()
n.title = "First evernote using api"
n.content = u"哈哈wahahahaha"  # 貌似需要对中文进行编码
n.content = "haha"
note_store.createNote(n)


note = Types.Note()
note.title = "Test note from EDAMTest.py"
note.content = '<?xml version="1.0" encoding="UTF-8"?>'
note.content += '<!DOCTYPE en-note SYSTEM ' \
    '"http://xml.evernote.com/pub/enml2.dtd">'
note.content += '<en-note>Here is the Evernote logo:<br/>'
note.content += '</en-note>'

created_note = note_store.createNote(note)

books = note_store.listNotebooks()
bid = books[1].guid # 拿到第二个笔记本（因为第一个测试笔记本没数据）
search = {'notebookGuid':bid}

results = note_store.findNotesMetadata(
                NoteStore.NoteFilter(**search), 
                None, 
                10, 
                NoteStore.NotesMetadataResultSpec(
                    includeTitle=True, includeNotebookGuid=True)
            )
print results.notes[0].title
print results.notes[0]content

haha = results.notes[0].guid # 'e3570976-3dbd-439e-84fa-98d8d2aae28e'
n = note_store.getNote(haha, True, False, False, False)

print n.created
print n.resources
print n.tagNames
print n.contentHash
