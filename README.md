# ponderada4
Este código detecta rostos em um vídeo usando a biblioteca OpenCV em Python. O classificador Haar Cascade é usado para detectar rostos nos quadros de vídeo. Os rostos são recortados dos quadros e salvos como imagens em uma pasta chamada 'detected_faces'.
 
Para usar este código, você precisa ter Python e OpenCV instalados em seu sistema. Você também precisa ter um arquivo de vídeo chamado 'arsene.mp4' no mesmo diretório do script Python.
 
Quando você executa o script, ele lê o arquivo de vídeo e percorre seus quadros. Para cada quadro, ele detectará rostos usando o classificador Haar Cascade e cortará os rostos dos quadros. Os rostos recortados são salvos como imagens na pasta 'detected_faces'. As imagens serão nomeadas como 'face0.jpg', 'face1.jpg' e assim por diante.
 
