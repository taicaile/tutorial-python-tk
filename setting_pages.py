"""
https://www.youtube.com/watch?v=4hamShRNxgg
"""

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class Page(ttk.Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)


class LangagePage(Page):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.create_frame_content().pack(fill=tk.BOTH, expand=True)

    def create_frame_content(self) -> ttk.Frame:
        """create the widgets specific to this setting(Lnague)

        Returns:
            ttk.Frame: the frame
        """
        self.frame_content = ttk.Frame(self)
        lbl_title = ttk.Label(self.frame_content, text="This is the Language Page!")
        lbl_title.pack()
        return self.frame_content


class AudioPage(Page):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.create_frame_content().pack(fill=tk.BOTH, expand=True)

    def create_frame_content(self) -> ttk.Frame:
        """create the widgets specific to this setting(Lnague)

        Returns:
            ttk.Frame: the frame
        """
        self.frame_content = ttk.Frame(self)
        lbl_title = ttk.Label(self.frame_content, text="This is the Audio Page!")
        lbl_title.pack()
        return self.frame_content


class SettingsView(ttk.Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        # key: Setting Name
        # value: Page Object
        self.pages = {}

        # Give row 0 and column 1 as much as room it needs
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.create_frame_treeview().grid(row=0, column=0, sticky="ens")

        self.create_frame_page().grid(row=0, column=1)

    def create_frame_page(self) -> ttk.Frame:
        """Create the frame what will show the current setting page.

        Returns:
            ttk.Frame: the page
        """

        self.frame_page = ttk.Frame(self)
        return self.frame_page

    def create_frame_treeview(self) -> ttk.Frame:
        """create the frame that will hold the settings treeview widget
        and also instantiate the SettingsTreeview class.

        Returns:
            ttk.Frame: the frame
        """
        self.frame_treeview = ttk.Frame(self)
        self.treeview_settings = SettingsTreeView(self.frame_treeview)
        self.treeview_settings.bind(
            "<<TreeviewSelect>>", self.on_treeview_selection_changed
        )
        self.treeview_settings.pack(fill=tk.BOTH, expand=True)
        return self.frame_treeview

    def on_treeview_selection_changed(self, event):
        """Switch to the frame related to the newly selected setting.

        Args:
            event:
        """
        selected_item = self.treeview_settings.focus()
        setting_name = self.treeview_settings.item(selected_item).get("text")
        self.show_page(setting_name)

    def show_page(self, setting_name: str):
        """pack_forget() all pages and pack the given page name.

        Args:
            setting_name (str): the setting/page to show
        """

        for page_name in self.pages.keys():
            self.pages[page_name].pack_forget()

        self.pages[setting_name].pack(fill=tk.BOTH, expand=True)

    def add_page(self, image_path: str, setting_name: str, page):
        """Instantiate a page frame and add it to ghe pages dictionary

        Args:
            image_path (str): a path to an image file
            setting_name (str): the setting name
            page (Page): a Page Class
        """
        with Image.open(image_path) as img:
            # Convert it to a photo image
            photo_image = ImageTk.PhotoImage(img)

        # Add page to dictionary so we can show it when needed
        self.pages[setting_name] = page(self.frame_page)

        # Keep a reference to the image so that it doesn't get garbage collection
        self.pages[setting_name].image = photo_image

        # Insert the setting name into the settings treeview
        self.treeview_settings.add_setting(image=photo_image, section_text=setting_name)


class SettingsTreeView(ttk.Treeview):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.heading("#0", text="Settings")

    def add_setting(self, image, section_text: str):
        """insert a row

        Args:
            image (): the section photo image
            section_text (str): the section name
        """
        self.insert(parent="", index=tk.END, text=section_text, image=image)


if __name__ == "__main__":

    root = tk.Tk()
    root.geometry("640x480")

    settings = SettingsView(root, relief="flat")  #
    settings.add_page(
        image_path="language.png", setting_name="Language", page=LangagePage
    )

    settings.add_page(image_path="audio.png", setting_name="Audio", page=AudioPage)

    settings.pack(fill=tk.BOTH, expand=True)

    root.mainloop()
