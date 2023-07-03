import cv2

def main():
    # Cambia el backend de captura de video a DirectShow (solo para Windows)
    # cv2.setPreferableBackend(cv2.CAP_DSHOW)

    # Inicializa los objetos de captura de video para cada cámara
    cap1 = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Primer cámara
    cap2 = cv2.VideoCapture(1, cv2.CAP_DSHOW)  # Segunda cámara

    # Comprueba si las cámaras se han abierto correctamente
    if not cap1.isOpened() or not cap2.isOpened():
        print("No se pudo abrir una o ambas cámaras.")
        exit()

    while True:
        # Lee los fotogramas de las cámaras
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        # Si no se pueden leer los fotogramas, sale del bucle
        if not ret1 or not ret2:
            print("No se pudo obtener un fotograma de una o ambas cámaras.")
            break

        # Redimensiona las imágenes para ajustarlas en un solo frame
        frame1 = cv2.resize(frame1, (320, 240))
        frame2 = cv2.resize(frame2, (320, 240))

        # Combina las imágenes en un solo frame
        combined_frame = cv2.hconcat([frame1, frame2])

        # Muestra el frame combinado
        cv2.imshow("Cámaras", combined_frame)

        # Espera la pulsación de la tecla 'q' para salir del bucle
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libera los recursos y cierra las ventanas
    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
