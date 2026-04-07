__all__ = ['theme', 'build_custom_colors']
from pathlib import Path
import json

theme_path = Path('editor/theme/theme.json')
with open(theme_path) as f:
    theme = json.load(f)

def build_custom_colors():
    """Load the colors for the default theme"""
    return {
        'background': theme['background'],
        'foreground': theme['foreground'],
        'primary': theme['accent'],
        'border': theme['border'],
        'foreground>disabled': theme['foreground_disabled'],
        'foreground>disabledSelectionBackground': theme['background_active'],
        'primary>selection.background': theme['background_active'],
        'primary>button.activeBackground': theme['background_active'],
        'primary>button.hoverBackground': theme['background_active'],
        'primary>defaultButton.activeBackground': theme['accent_active'],
        'primary>defaultButton.hoverBackground': theme['accent_active'],
        'input.background': theme['background'],
        'inputButton.hoverBackground': theme['background_active'],
        'foreground>input.placeholder': theme['foreground_dark'],
        'list.hoverBackground': theme['background_active'],
        'tree.inactiveIndentGuidesStroke': theme['border'],
        'tree.indentGuidesStroke': theme['border'],
        'treeSectionHeader.background': theme['background_light'],
        'background>list': theme['background'],
        'primary>list.inactiveSelectionBackground': theme['background_active'],
        'primary>list.selectionBackground': theme['background_active'],
        'menubar.selectionBackground': theme['background_active'],
        'background>panel': theme['background_light'],
        'popupItem.checkbox.background': theme['background'],
        'popupItem.selectionBackground': theme['background_active'],
        'background>popup': theme['background'],
        'foreground>progressBar.disabledBackground': theme['accent_disabled'],
        'primary>progressBar.background': theme['accent'],
        'scrollbar.background': theme['background'],
        'scrollbarSlider.activeBackground': theme['accent_active'],
        'scrollbarSlider.background': theme['accent'],
        'scrollbarSlider.disabledBackground': theme['accent_disabled'],
        'scrollbarSlider.hoverBackground': theme['accent_active'],
        'foreground>slider.disabledBackground': theme['accent_disabled'],
        'foreground>sliderTrack.inactiveBackground': theme['accent_disabled'],
        'primary>sliderHandle.activeBackground': theme['accent_active'],
        'statusBar.background': theme['background'],
        'statusBarItem.activeBackground': theme['background_active'],
        'statusBarItem.hoverBackground': theme['background_active'],
        'tableSectionHeader.background': theme['background_light'],
        'background>table': theme['background'],
        'primary>table.selectionBackground': theme['background_active'],
        'primary>table.inactiveSelectionBackground': theme['background_active'],
        'tab.activeBackground': theme['background_active'],
        'tab.hoverBackground': theme['background_active'],
        'tabCloseButton.hoverBackground': theme['border'],
        'textarea.inactiveSelectionBackground': theme['background_active'],
        'background>textarea': theme['background'],
        'primary>textarea.selectionBackground': theme['background_active'],
        'background>title': theme['background'],
        'toolbar.activeBackground': theme['background_active'],
        'toolbar.background': theme['background'],
        'toolbar.hoverBackground': theme['background_active']
    }
