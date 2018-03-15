from pywinauto.application import Application


app = Application().Connect(title=u'Logos Smart Card Explorer', class_name='TFormMain')
app1 = Application().start("Notepad.exe")
tformmain = app.TFormMain


ttreeview = tformmain[u'11']
tree_item = ttreeview.GetItem([u'Card', u'MF', u'DF_Telecom'])


for x in range(0,16):
	DF_Telecom = (tree_item.GetChild(x).text())
	app1.UntitledNotepad.Edit.type_keys(DF_Telecom)
	app1.UntitledNotepad.Edit.type_keys('{ENTER}')


ttreeview = tformmain[u'11']
tree_item2 = ttreeview.GetItem([u'Card', u'MF', u'DF_Telecom', u'DF_PhoneBook'])

for x in range(0,4):
	DF_PhoneBook = (tree_item2.GetChild(x).text())
	app1.UntitledNotepad.Edit.type_keys(DF_PhoneBook)
	app1.UntitledNotepad.Edit.type_keys('{ENTER}')


ttreeview = tformmain[u'11']
tree_item2 = ttreeview.GetItem([u'Card', u'MF', u'DF_GSM'])

for x in range(0,25):
	DF_GSM = (tree_item2.GetChild(x).text())
	app1.UntitledNotepad.Edit.type_keys(DF_GSM)
	app1.UntitledNotepad.Edit.type_keys('{ENTER}')

app1.UntitledNotepad.SetFocus()
app1.UntitledNotepad.MenuSelect("File->SaveAs")
app1.SaveAs.edit1.SetText("Lineage2R.txt")
app1.SaveAs.Save.Click()

try:
	window = app1.Dialog
	window.Wait('ready')
	button = window[u'&Yes']
	button.Click()

except:
	print('Succeess ...')
	
app1.kill()

