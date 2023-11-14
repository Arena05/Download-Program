import customtkinter
import urllib.request
import os
from tkinter import filedialog
from PIL import Image, ImageTk
from pytube import YouTube, Search

# Download the tumbnail image
def dl_jpg(url, file_path, file_name) -> None:
    full_path = file_path + file_name + ".jpg"
    urllib.request.urlretrieve(url, full_path)

# Initial frame
def frames(frame1, frame2, frame3):
    # Opcions frame
    frame1.grid(row = 0, column = 0, padx = 5, pady = 5, sticky="ew", columnspan = 2)

    # Download frame
    
    frame2.grid(row = 1, column = 0, padx = 5, pady = 5, columnspan = 2)

    # Download section frame
    
    frame3.grid(row = 2, column = 0, padx = 5, pady = 5, columnspan = 2)

    
    # Adding a main image
    Image_path = os.path.join(os.path.dirname(__file__), "Images/image.jpeg")
    image = customtkinter.CTkImage(light_image = Image.open(Image_path), size = (250, 250))
    image_label = customtkinter.CTkLabel(master = frame2, image = image, text = "")
    image_label.grid(row = 0, column = 0, padx = 5, pady = 10)

    # First Comment
    Comment = customtkinter.CTkLabel(master = frame3, text = "Select an option above to continue", font = ("Arial Narrow", 20))
    Comment.grid(row = 1, column = 0, padx = 5, pady = 5)
    
    # Music option button
    buttonM = customtkinter.CTkButton(master=frame1, corner_radius= 15, text="Music", command=button_eventM)
    buttonM.grid(row = 0, column = 0, padx = 15, pady = 10)

    # Video option button
    buttonV = customtkinter.CTkButton(master=frame1, corner_radius= 15, text="Video", command = button_eventV)
    buttonV.grid(row = 0, column = 1, padx = 15, pady = 10)

    # Video with caption option button
    buttonC = customtkinter.CTkButton(master=frame1, corner_radius= 15, text="Video & Sub", command=button_eventC, state = "disabled")
    buttonC.grid(row = 0, column = 2, padx = 15, pady = 10)

    # Appearance mode
    def switch_event():
        print("switch toggled, current value:", switch_var.get())
        if switch_var.get()=="off":
            customtkinter.set_appearance_mode("light")
        else:
            customtkinter.set_appearance_mode("dark")

    # Appearance switch
    switch_var = customtkinter.StringVar(value="on")
    switch = customtkinter.CTkSwitch(master=frame1, text="Dark mode", command=switch_event,
                                    variable=switch_var, onvalue="on", offvalue="off")
    switch.grid(row = 0, column = 6, padx = 100)

    return frame1, frame2, frame3

# Video option button
def button_eventV() -> None:
    # Clear frame2
    for item in frame2.winfo_children():
        item.destroy()

    # Clear frame3
    for item in frame3.winfo_children():
        item.destroy()

    # Building the Video frame
    print("button Video pressed")
    # Label title
    LabelTV = customtkinter.CTkLabel(master = frame2, text="Download video")
    LabelTV.grid(row = 0, column = 0)

    # Input texbox
    global UrlV 
    UrlV = customtkinter.CTkEntry(master = frame2, width = 400, height = 35, placeholder_text = "YouTube link")
    UrlV.grid(row = 1, column = 0, padx = 5, pady = 5)

    # Search Button
    buttonS = customtkinter.CTkButton(master = frame2, text = "Search", command = Download)
    buttonS.grid(row = 2, column = 0)

    # Logo Image
    Image_path = os.path.join(os.path.dirname(__file__), "Images/Logo.jpeg")
    image =customtkinter.CTkImage(light_image = Image.open(Image_path), size = (50, 50))
    image_Label = customtkinter.CTkLabel(master = frame3, image = image, text = "")
    image_Label.grid(row = 0, column = 0, padx = 5, pady = 5)

# Music option button
def button_eventM() -> None:
    # Clear frame2
    for item in frame2.winfo_children():
        item.destroy()

    # Clear frame3
    for item in frame3.winfo_children():
        item.destroy()

    # Bulding the Music frame
    print("button Music pressed")
    # Label title
    LabelTM = customtkinter.CTkLabel(master = frame2, text="Download Music")
    LabelTM.grid(row = 0, column = 0)

    # Input texbox
    global UrlM
    UrlM = customtkinter.CTkEntry(master = frame2, width = 400, height = 35, placeholder_text = "YouTube link")
    UrlM.grid (row = 1, column = 0, padx = 5, pady = 5)

    # Search Button
    buttonS = customtkinter.CTkButton(master = frame2, text = "Search", command = DownloadM)
    buttonS.grid(row = 2, column = 0)

    # Logo Image
    Image_path = os.path.join(os.path.dirname(__file__), "Images/Logo.jpeg")
    image =customtkinter.CTkImage(light_image = Image.open(Image_path), size = (50, 50))
    image_Label = customtkinter.CTkLabel(master = frame3, image = image, text = "")
    image_Label.grid(row = 0, column = 0, padx = 5, pady = 5)

# Video with caption option button
def button_eventC() -> None:
    # Clear the frame
    for item in frame2.winfo_children():
        item.destroy()

    # Bulding the caption frame
    print("button Video with caption pressed")
    LabelTC = customtkinter.CTkLabel(master = frame2, text = "Download Video with subtitles")
    LabelTC.grid(row = 0, column = 0)

# Video Download Funtion
def Download() -> None:
    try:
        UrlV_var = UrlV.get()
        ytSearch = Search(UrlV_var)

        # Clear frame3
        for item in frame3.winfo_children():
            item.destroy()

        # Complete label
        Complete = customtkinter.CTkLabel(master = frame3, text = "")
        Complete.grid(row = 4, column = 0, columnspan = 3, padx = 5, pady = 5)

        if len(ytSearch.results) != 0:
            
            def on_progress(stream, chunk: bytes, bytes_remaining: int) -> None:
                total_size = stream.filesize
                bytes_downloaded = total_size - bytes_remaining
                percentage_of_completation = (bytes_downloaded / total_size) * 100
                per = str(int(percentage_of_completation))
                pPercentage.configure(text=per + " %")
                pPercentage.update()
                # Update progress bar
                progressBar.set(float(percentage_of_completation)/100)

            def openFile() -> None:
                try:
                    filepath = filedialog.askdirectory()
                    Path_label.configure(text = filepath)
                    video.download(output_path = filepath)
                    Complete.configure(text = "Download Complete")

                except:
                    Complete.configure(text = "Download Error")

            Yt = YouTube(UrlV_var)
            Yt.register_on_progress_callback(on_progress)
            video = Yt.streams.get_highest_resolution()

            # Thumbnail image 
            dl_jpg(Yt.thumbnail_url, "Images/", "Thumbnail")
            Thumbnail_path = os.path.join(os.path.dirname(__file__), "Images/Thumbnail.jpg")
            Thumbnail = customtkinter.CTkImage(light_image = Image.open(Thumbnail_path), size = (210, 118))
            Thumbnail_label = customtkinter.CTkLabel(master = frame3, image = Thumbnail, text = "")
            Thumbnail_label.grid(row = 0, column = 0, padx = 5, pady = 5)

            # Title label
            Title_label = customtkinter.CTkLabel(master = frame3, text = "")
            Title_label.configure(text = Yt.title)
            Title_label.grid(row = 1, column = 0)

            # Path label
            Path_label = customtkinter.CTkLabel(master = frame3, text = "")
            Path_label.grid(row = 0, column = 1, padx = 5, pady = 5)
            Path_Button = customtkinter.CTkButton(master = frame3, corner_radius = 10, text = "Save", command = openFile, width = 60)
            Path_Button.grid(row = 0, column = 2, padx = 5, pady = 5)

            # Progress percentage
            pPercentage = customtkinter.CTkLabel(master = frame3, text = "0 %")
            pPercentage.grid(row = 2, column = 0, columnspan = 3, padx = 5, pady = 5)

            # Progress Bar
            progressBar = customtkinter.CTkProgressBar(master = frame3, width = 400)
            progressBar.set(0)
            progressBar.grid(row = 3, column = 0, columnspan = 3, padx = 5, pady = 5)

        else:
            Complete.configure(text = "Video not found")
    except:
        # Invalid link label
        Invalid_link = customtkinter.CTkLabel(master = frame3, text = "Invalid link")
        Invalid_link.grid(row = 0, column = 0, padx = 5, pady = 5, rowspan = 7)

# Music Download Funtion     
def DownloadM() -> None:
    try:
        # Clear frame3
        for item in frame3.winfo_children():
            item.destroy()

        UrlM_Var = UrlM.get()
        ytSearch = Search(UrlM_Var)

        # Complete label
        Complete = customtkinter.CTkLabel(master = frame3, text = "")
        Complete.grid(row = 4, column = 0, columnspan = 3, padx = 5, pady = 5)

        if len(ytSearch.results) != 0:

            def on_progress(stream, chunk: bytes, bytes_remaining: int):
                total_size = stream.filesize
                bytes_downloaded = total_size - bytes_remaining
                percentage_of_completation = (bytes_downloaded / total_size) * 100
                per = str(int(percentage_of_completation))
                pPercentage.configure(text = per + " %")
                pPercentage.update()
                # Update progress bar
                progressBar.set(float(percentage_of_completation)/100)

            def openFile() -> None:
                try:
                    filePath = filedialog.askdirectory()
                    Path_Label.configure(text = filePath)
                    video.download(output_path = filePath)
                    Complete.configure(text = "Download Complete")

                except:
                    Complete.configure(text = "Download Error")

            Yt = YouTube(UrlM_Var)
            Yt.register_on_progress_callback(on_progress)
            video = Yt.streams.filter(only_audio = True).order_by("abr").last()

            # Thumbnail image 
            dl_jpg(Yt.thumbnail_url, "Images/", "Thumbnail")
            Thumbnail_path = os.path.join(os.path.dirname(__file__), "Images/Thumbnail.jpg")
            Thumbnail = customtkinter.CTkImage(light_image = Image.open(Thumbnail_path), size = (210, 118))
            Thumbnail_Label = customtkinter.CTkLabel(master = frame3, image = Thumbnail, text = "")
            Thumbnail_Label.grid(row = 0, column = 0, padx = 5, pady = 5)

            # Title Label
            Title_Label = customtkinter.CTkLabel(master = frame3, text = "")
            Title_Label.configure(text = Yt.title)
            Title_Label.grid(row = 1, column = 0)

            # Path Label
            Path_Label = customtkinter.CTkLabel(master = frame3, text = "")
            Path_Label.grid(row = 0, column = 1, padx = 5, pady = 5)
            Path_Button = customtkinter.CTkButton(master = frame3, corner_radius = 10, text = "Save", command = openFile, width = 60) 
            Path_Button.grid(row = 0, column = 2, padx = 5, pady = 5)

            # Progress Percentage
            pPercentage = customtkinter.CTkLabel(master = frame3, text = "0 %")
            pPercentage.grid(row = 2, column = 0, columnspan = 3, padx = 5, pady = 5)

            # Progress Bar
            progressBar = customtkinter.CTkProgressBar(master = frame3, width = 400)
            progressBar.set(0)
            progressBar.grid(row = 3, column = 0, columnspan = 3, padx = 5, pady = 5)
        
        else:
            Complete.configure(text = "Video not found")
    except:
        # Invalid link label 
        Invalid_Link = customtkinter.CTkLabel(master = frame3, text = "Invalid Link")
        Invalid_Link.grid(row = 0, column = 0, padx = 5, pady = 5, rowspan = 7)

# Principal window
app = customtkinter.CTk()
app.title("Video Downloader")
app.geometry("750x450")
app.resizable(False, False)
app.grid_columnconfigure((0, 1), weight=1)
customtkinter.set_appearance_mode("dark")
frame1 = customtkinter.CTkFrame(master = app, corner_radius = 10)
frame2 = customtkinter.CTkFrame(master = app, corner_radius = 10)
frame3 = customtkinter.CTkFrame(master = app, corner_radius = 10)
frames(frame1 = frame1, frame2 = frame2, frame3 = frame3)

app.mainloop()


