import wx
from Task4 import StringFormatter

class MyFrame(wx.Frame):
    def __init__(self, parent, title, style):
        super().__init__(parent, title=title, size=(500, 380), style=style)

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        f_box = wx.BoxSizer(wx.HORIZONTAL)
        s_box = wx.BoxSizer(wx.HORIZONTAL)
        t_box = wx.BoxSizer(wx.HORIZONTAL)
        fo_box = wx.BoxSizer(wx.HORIZONTAL)
        fi_box = wx.BoxSizer(wx.VERTICAL)
        si_box = wx.BoxSizer(wx.HORIZONTAL)

        self.st_string = wx.StaticText(panel, label='Строка:')
        self.tc_string = wx.TextCtrl(panel)
        f_box.Add(self.st_string, flag=wx.LEFT, border=10)
        f_box.Add(self.tc_string, proportion=1, flag=wx.LEFT, border=40)

        self.cb_del = wx.CheckBox(panel, label='Удалить слова размером меньше')
        self.cb_del.SetValue(True)
        s_box.Add(self.cb_del)
        self.sc_len = wx.SpinCtrl(panel, value='5', min=0, max=100)
        s_box.Add(self.sc_len, flag=wx.LEFT, border=10)
        self.Bind(wx.EVT_CHECKBOX, self.check_cb_del, self.cb_del)
        self.cb_change = wx.CheckBox(panel, label='Заменить все цифры на *')
        self.cb_change.SetValue(True)
        t_box.Add(self.cb_change, flag=wx.TOP, border=10)

        self.cb_spaces = wx.CheckBox(panel, label='Вставить по пробелу между символами')
        self.cb_spaces.SetValue(True)
        fo_box.Add(self.cb_spaces, flag=wx.TOP, border=10)

        self.cb_sort = wx.CheckBox(panel, label='Сортировать слова в строке')
        self.cb_sort.SetValue(True)
        fi_box.Add(self.cb_sort, flag=wx.TOP, border=10)
        self.rb_len = wx.RadioButton(panel, label='По размеру', style=wx.RB_GROUP)
        self.rb_lex = wx.RadioButton(panel, label='Лексикографически')
        self.but_format = wx.Button(panel, size=(400, 30), label='Форматировать')
        fi_box.Add(self.rb_len, flag=wx.LEFT, border=30)
        fi_box.Add(self.rb_lex, flag=wx.LEFT, border=30)
        fi_box.Add(self.but_format, flag=wx.EXPAND|wx.RIGHT|wx.TOP, border=20)
        self.but_format.Bind(wx.EVT_BUTTON, self.format)
        self.Bind(wx.EVT_CHECKBOX, self.check_cb_sort, self.cb_sort)

        self.st_res = wx.StaticText(panel, label='Результат:')
        self.tc_res = wx.TextCtrl(panel, style=wx.TE_READONLY)
        si_box.Add(self.st_res, flag=wx.LEFT, border=10)
        si_box.Add(self.tc_res, proportion=1, flag=wx.LEFT, border=20)

        vbox.Add(f_box, flag=wx.EXPAND|wx.TOP|wx.BOTTOM|wx.RIGHT, border=20)
        vbox.Add(s_box, flag=wx.LEFT, border=95)
        vbox.Add(t_box, flag=wx.LEFT, border=95)
        vbox.Add(fo_box, flag=wx.LEFT, border=95)
        vbox.Add(fi_box, flag=wx.LEFT, border=95)
        vbox.Add(si_box, flag=wx.EXPAND|wx.TOP|wx.RIGHT, border=20)

        panel.SetSizer(vbox)
        self.Show()
    def format(self, e):
        text = self.tc_string.GetValue()
        format_text = StringFormatter(text)
        if self.cb_del.IsChecked():
            format_text.del_words(self.sc_len.GetValue())
        if self.cb_change.IsChecked():
            format_text.change_num()
        if self.cb_spaces.IsChecked():
            format_text.add_spaces()
        if self.cb_sort.IsChecked():
            if self.rb_len.GetValue():
                format_text.sort_by_len()
            elif self.rb_lex.GetValue():
                format_text.sort_by_alph()

        self.tc_res.SetValue(format_text.string)
    def check_cb_del(self, e):
        if not self.cb_del.IsChecked():
            self.sc_len.Enabled = False
        else:
            self.sc_len.Enabled = True

    def check_cb_sort(self, e):
        if not self.cb_sort.IsChecked():
            self.rb_len.Enabled = False
            self.rb_lex.Enabled = False
        else:
            self.rb_len.Enabled = True
            self.rb_lex.Enabled = True

app = wx.App()
no_resize = wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
frame = MyFrame(None, 'StringFormatter Demo', style=no_resize)
app.MainLoop()