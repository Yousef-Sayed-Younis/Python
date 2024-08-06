import pytube

def finish():
    print("Download Done.")

link = input("Enter The Vid. URL: ")

video = pytube.YouTube(link)

print(f"The video title is: \n{video.title} \n----------------")
print(f"The video duration is: \n{video.length} seconds \n----------------")

select = input("Enter v for Video & a for Audio: ")

if select == 'v':
    resolution = input("Enter The resolution: 720p, 480p, 360p, 240p, 144p")
    down = video.streams.get_by_resolution(resolution)
    if down == None: print("Try Another Resolution")

    video.streams.get_by_resolution(resolution).download(output_path="/Download")
    video.register_on_complete_callback(finish())

elif select == 'a':
    resolution = input("Enter The resolution: mp4, webm")
    down = video.streams.get_audio_only(resolution)
    if down == None: print("Try Another Resolution")
    
    video.streams.get_by_resolution(resolution).download(output_path="/Download")   
    video.register_on_complete_callback(finish())

else:
    print("Invalid Syntax, Please try again")
    exit(0)   

