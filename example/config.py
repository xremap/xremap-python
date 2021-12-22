from xremap.dsl import *

define_modmap({
    'CapsLock': 'Control_L',
})

define_conditional_modmap({ 'only': ['Gnome-terminal'] }, {
    'Control_R': 'Esc',
})


define_keymap({ 'only': ['Google-chrome'] }, {
    'C-M-j': 'C-Tab',
    'C-M-k': 'C-Shift-Tab',
}, 'Chrome')

define_keymap({}, {
    'C-b': 'left',
    'C-f': 'right',
    'C-p': 'up',
    'C-n': 'down',
}, 'Emacs-like keys')
