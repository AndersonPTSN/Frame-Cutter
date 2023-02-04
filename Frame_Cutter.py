import PySimpleGUI as sg
import cv2

def Cutter(arquivo,ext):
	cap= cv2.VideoCapture(arquivo)
	i=1
	length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
	
	while(cap.isOpened()):
	    ret, frame = cap.read()
	    if ret == False:
	        break
	    cv2.imwrite('frames/frame_'+str(i)+ext,frame)
	    sg.OneLineProgressMeter('Progresso', i, length, 'single',orientation="h")
	    i = i + 1
	cap.release()
	cv2.destroyAllWindows()
	sg.popup("Concluído con sucesso!",title="AVISO")


sg.theme('DefaultNoMoreNagging') 
 
frame_layout = [
	[sg.FileBrowse("Selecionar vídeo",key="browse"), sg.Text("Somente arquivos AVI, MP4 ou GIF",key="texto")],
	[sg.Text("Selecione o formato de saida:"),sg.Radio('.png', "radio", default=True,key=".png"),sg.Radio('.jpg', "radio",key=".jpg")],
        [sg.Text("Suas imagens serão salvas na pasta frames")],
        [sg.Button('Cortar',key="button"), sg.Button('Cancel')] 
 ]

layout = [
          [sg.Frame('Frame Cutter', frame_layout, font='Any 16')],
         ]

window = sg.Window('Frame Cutter', layout)

while True:
    event, values = window.read()

    if event in (None, 'Cancel'):  
        break

    if event == "button":
    	ext = values["browse"][-3:len(values["browse"])]
    	if ext == "avi" or ext == "mp4" or ext == "gif":
    		values["texto"] = values["browse"]
    		caminho = values["texto"].split("/")
    		arquivo = caminho[-1]
    		if values[".png"] == True:
    			Cutter(values["browse"],".png")
    		else:
    			Cutter(values["browse"],".jpg")
    	else:
    		sg.popup("Somente arquivos AVI, MP4 ou GIF",title="AVISO")

window.close()
