""" This module used to download the media from the Youtube """
import tkinter as tk
#from pytube import YouTube
import pytube
from functools import partial

class YoutubeDownloader(tk.Frame):
    """ This module used to download the media from the Youtube """
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title('YouTube Downloader')
        self.master.minsize(400, 400)
        self.media_type = tk.StringVar()
        #self.pack()
        self.create_initial_widget()

    def add_stream_radio(self, context):
        #https://www.youtube.com/watch?v=cH4E_t3m3xM
        int_row = int_column = int_count = 0
        for stream in context.streams.all():
            if hasattr(stream, 'resolution') and stream.resolution is not None:
                text = str(stream.mime_type) + ' ' + str(stream.resolution)
                int_column = int_count % 3
                if int_count % 3 == 0:
                    int_row += 1

                int_count += 1
                self.media_type.set(str(stream.itag))
                print(self.media_type)
                tk.Radiobutton(
                    text=text,
                    variable=self.media_type,
                    value=stream.itag
                ).grid(row=int_row, column=int_column)

    def download_media(self, yt):
        stream = yt.streams.get_by_itag(self.media_type.get())
        print(stream)
        stream.download()

    def add_download_button(self, yt):
        self.button_download = tk.Button()
        self.button_download['text'] = 'Download'
        self.button_download['command'] = partial(self.download_media, yt)
        self.button_download.grid(row=0, column=3, padx=(5), pady=(15))

    def get_stream(self):
        #print(self.url_text.get())
        yt = pytube.YouTube(self.url_text.get())
        self.add_stream_radio(yt)
        self.add_download_button(yt)

    def create_initial_widget(self):
        self.url_label = tk.Label()
        self.url_label['text'] = 'URL : '
        self.url_label.grid(row=0, column=0, padx=(15), pady=(15))

        self.url_text = tk.Entry()
        self.url_text.grid(row=0, column=1, padx=(5), pady=(15))

        self.button_analyze = tk.Button()
        self.button_analyze['text'] = 'Analyze'
        self.button_analyze['command'] = self.get_stream
        self.button_analyze.grid(row=0, column=2, padx=(5), pady=(15))


root = tk.Tk()
YouTube = YoutubeDownloader(master=root)
YouTube.mainloop()
