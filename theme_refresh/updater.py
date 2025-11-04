import time, os

settings_file = open("C:/Users/keish/AppData/Roaming/VSCodium/User/settings.json", "w")
month_dict = {
  "01": "January",
  "02": "Febuary",
  "03": "March",
  "04": "April",
  "05": "May",
  "06": "June",
  "07": "July",
  "08": "August",
  "09": "September",
  "10": "October",
  "11": "November",
  "12": "December"
}

month_num = time.localtime().tm_mon if time.localtime().tm_mon >= 10 else f"0{time.localtime().tm_mon}"
text = "{\n" + f'   "workbench.colorTheme": "365 {month_num}-{month_dict[month_num]} High Contrast",\n'+"""      "workbench.colorCustomizations": {
        "[Vira*]": {
            "toolbar.activeBackground": "#B54DFF26",
            "button.background": "#B54DFF",
            "button.hoverBackground": "#B54DFFcc",
            "extensionButton.separator": "#B54DFF33",
            "extensionButton.background": "#B54DFF14",
            "extensionButton.foreground": "#B54DFF",
            "extensionButton.hoverBackground": "#B54DFF33",
            "extensionButton.prominentForeground": "#B54DFF",
            "extensionButton.prominentBackground": "#B54DFF14",
            "extensionButton.prominentHoverBackground": "#B54DFF33",
            "activityBarBadge.background": "#B54DFF",
            "activityBar.activeBorder": "#B54DFF",
            "activityBarTop.activeBorder": "#B54DFF",
            "list.inactiveSelectionIconForeground": "#B54DFF",
            "list.activeSelectionForeground": "#B54DFF",
            "list.inactiveSelectionForeground": "#B54DFF",
            "list.highlightForeground": "#B54DFF",
            "sash.hoverBorder": "#B54DFF80",
            "list.activeSelectionIconForeground": "#B54DFF",
            "scrollbarSlider.activeBackground": "#B54DFF80",
            "editorSuggestWidget.highlightForeground": "#B54DFF",
            "textLink.foreground": "#B54DFF",
            "progressBar.background": "#B54DFF",
            "pickerGroup.foreground": "#B54DFF",
            "tab.activeBorder": "#B54DFF",
            "notificationLink.foreground": "#B54DFF",
            "editorWidget.resizeBorder": "#B54DFF",
            "editorWidget.border": "#B54DFF",
            "settings.modifiedItemIndicator": "#B54DFF",
            "panelTitle.activeBorder": "#B54DFF",
            "breadcrumb.activeSelectionForeground": "#B54DFF",
            "menu.selectionForeground": "#B54DFF",
            "menubar.selectionForeground": "#B54DFF",
            "editor.findMatchBorder": "#B54DFF",
            "selection.background": "#B54DFF40",
            "statusBarItem.remoteBackground": "#B54DFF14",
            "statusBarItem.remoteHoverBackground": "#B54DFF",
            "statusBarItem.remoteForeground": "#B54DFF",
            "notebook.inactiveFocusedCellBorder": "#B54DFF80",
            "commandCenter.activeBorder": "#B54DFF80",
            "chat.slashCommandForeground": "#B54DFF",
            "chat.avatarForeground": "#B54DFF",
            "activityBarBadge.foreground": "#000000",
            "button.foreground": "#000000",
            "statusBarItem.remoteHoverForeground": "#000000"
        }
    },
    "viraTheme.accent": "Purple",
    "editor.fontSize": 16,
    "workbench.activityBar.location": "bottom"
}"""
settings_file.write(text)
