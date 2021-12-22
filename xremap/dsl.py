_xremap_config = { 'modmap': [], 'keymap': [] }

def define_modmap(modmap):
    global _xremap_config
    _xremap_config['modmap'].append({
        'name': 'xremap-python',
        'remap': modmap,
    })

def define_conditional_modmap(application, modmap):
    global _xremap_config
    _xremap_config['modmap'].append({
        'name': 'xremap-python',
        'remap': modmap,
        'application': application,
    })

def define_keymap(application, keymap, name):
    global _xremap_config
    entry = {
        'name': 'xremap-python',
        'remap': keymap,
    }
    if application:
        entry['application'] = application
    _xremap_config['keymap'].append(entry)

def xremap_config():
    global _xremap_config
    return _xremap_config
