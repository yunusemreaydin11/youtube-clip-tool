from googleapiclient.discovery import build
from pytube import YouTube
from moviepy.editor import VideoFileClip
import os
import re



api_key = "AIzaSyCiIoV79oLcOakYpvvE2Hs1xXhPkppls0I"

youtube = build('youtube', 'v3', developerKey=api_key)

def get_video_id(url):
    video_id = url.split('v=')[1]
    return video_id


print("VİDEO URL GİRİNİZ")

url_1 = input("URL: ")


video_id = get_video_id(url_1) 

video_response = youtube.videos().list(
    part="snippet",
    id= video_id
). execute()


video_title = video_response['items'][0]['snippet']['title']

video_title_cleaned = re.sub(r'[^\w\s]', '', video_title)
video_title_cleaned = video_title_cleaned.replace(' ', '_')

downloaduser = YouTube(url_1)
downloaduser.streams.get_highest_resolution().download(filename="{}.mp4".format(video_title_cleaned))


indirilen_dosya_yolu = "{}.mp4".format(video_title_cleaned)
yeni_dosya_yolu = "C:/Users/yunus/Desktop/{}.mp4".format(video_title_cleaned)
os.rename(indirilen_dosya_yolu, yeni_dosya_yolu)


video_clip = VideoFileClip(yeni_dosya_yolu)
def convert_to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds


baslangic_saat = int(input("Başlangıç Saati: "))
baslangic_dakika = int(input("Başlangıç Dakikası: "))
baslangic_saniye = int(input("Başlangıç Saniyesi: "))

bitis_saat = int(input("Bitiş Saati: "))
bitis_dakika = int(input("Bitiş Dakikası: "))
bitis_saniye = int(input("Bitiş Saniyesi: "))


baslangic_sure_saniye = convert_to_seconds(baslangic_saat, baslangic_dakika, baslangic_saniye)
bitis_sure_saniye = convert_to_seconds(bitis_saat, bitis_dakika, bitis_saniye)

sub_clip = video_clip.subclip(baslangic_sure_saniye, bitis_sure_saniye)
sub_clip.write_videofile("{}.mp4".format(video_title_cleaned))

video_path = yeni_dosya_yolu
video_clip.close()
os.remove(video_path)

print("Video Başlığı:", video_title)


