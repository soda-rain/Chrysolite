# TODO: Add more shades of background and primary, as well as the colors for popups like qmenu. Also add colors for inherited, so that we know what the colors are.
BACKGROUND = '#181a1f' # Background for widgets, dark icon
BACKGROUND_LIGHT = '#24262b' # Background for things like cards and tree widget headers
PRIMARY = '#dadde5' # Accent Color and foreground. Color for light icon
PRIMARY_LIGHT = '#ffffff'
BORDER = '#3f4042'
SCROLLBAR = '#494c51'
SCROLLBAR_HOVER = '#5d6065'


def build_custom_colors():
    return {
        'background': BACKGROUND,
        'foreground': PRIMARY,
        'primary': PRIMARY,
        'border': BORDER,
        'input.background': BACKGROUND,
        'inputButton.hoverBackground': BACKGROUND_LIGHT,
        'tree.inactiveIndentGuidesStroke': BORDER,
        'tree.indentGuidesStroke': BORDER,
        'treeSectionHeader.background': BACKGROUND_LIGHT,
        'scrollbar.background': BORDER,
        'scrollbarSlider.activeBackground': SCROLLBAR_HOVER,
        'scrollbarSlider.background': SCROLLBAR,
        'scrollbarSlider.hoverBackground': SCROLLBAR_HOVER,
        'statusBar.background': BACKGROUND,
        'statusBarItem.activeBackground': BACKGROUND_LIGHT,
        'statusBarItem.hoverBackground': BACKGROUND_LIGHT,
        'tableSectionHeader.background': BACKGROUND_LIGHT,
        'tab.activeBackground': PRIMARY,
        'tab.hoverBackground': BACKGROUND_LIGHT,
        'tabCloseButton.hoverBackground': BORDER,
        'toolbar.activeBackground': BACKGROUND_LIGHT,
        'toolbar.background': BACKGROUND,
        'toolbar.hoverBackground': BACKGROUND_LIGHT
    }
